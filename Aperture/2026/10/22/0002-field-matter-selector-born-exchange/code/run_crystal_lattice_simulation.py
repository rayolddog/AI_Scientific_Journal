#!/usr/bin/env python3
"""
2D Condensed-Matter Crystal Lattice & Surface-Conditioned Vacuum Phase Simulation
for Aperture Article 0002 (Revision 2.1 — 2026-10-24)

Tests whether the atom-by-atom pre-modulus phase mechanism holds up when the absorber
sites are placed on a physical 2D condensed-matter crystal lattice:
1. Spatial 2D Lattice Geometry:
   - Each detector region/fringe is a 2D square crystal lattice of size L_x x L_y
     (e.g., 4 x 4 = 16 lattice atoms in Patch 1 and 4 x 4 = 16 lattice atoms in Patch 2,
     total M_total = 32 lattice atoms).
2. Coherent Incident Bloch/Wavevector Phase Across Lattice Sites:
   - The incident wave has a physical spatial wavevector phase across the lattice:
     phi_inc(x, y) = phi_0 + k_x * x + k_y * y (not independent random phases!).
3. Surface-Conditioned Quantum Vacuum Phase Distribution (Casimir-Polder + Bias Field E_bias):
   - Near the condensed-matter surface under bias field E_bias, the virtual vacuum phase
     phi_vac(x, y, t) is:
     (a) pinned/narrowed around the surface Fresnel/bias reference phase phi_surf with
         concentration parameter kappa_surf (von Mises / squeezed surface distribution),
     (b) spatially correlated across neighboring lattice sites with correlation length xi_vac,
     (c) dynamically pulled toward the phase of the dominant absorbing lattice atom(s).
4. Lattice Phonon Dephasing & Two-Tier Lattice + Shared-Vacuum Exchange:
   - Within each crystal patch, atoms exchange energy with their 2D lattice nearest neighbors
     (local exciton/polaron consolidation on the lattice) AND across the shared wave/vacuum
     bus connecting the active lattice sites.
"""

from pathlib import Path
import json
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CODE_DIR = Path(__file__).resolve().parent


def build_2d_lattice_neighbors(Lx, Ly):
    """
    Returns array of lattice coordinates (M, 2) and list of nearest-neighbor pairs
    for a 2D Lx x Ly crystal lattice patch.
    """
    coords = []
    for ix in range(Lx):
        for iy in range(Ly):
            coords.append((ix, iy))
    coords = np.array(coords, dtype=float)
    M = len(coords)
    nn_pairs = []
    for a in range(M):
        for b in range(a + 1, M):
            dist2 = np.sum((coords[a] - coords[b]) ** 2)
            if np.isclose(dist2, 1.0) or np.isclose(dist2, 2.0):  # 1st and 2nd nearest neighbors on 2D lattice
                nn_pairs.append((a, b))
    return coords, nn_pairs


def simulate_2d_crystal_lattice_aperture(
    s_patch1=0.5,
    Lx=4,
    Ly=4,
    theta=0.45,
    sigma=0.25,
    commit_rate=0.02,
    kappa_surf=2.5,
    surface_vac_eps=0.005,
    n_trials=12000,
    max_steps=8000,
    seed=20261024,
):
    """
    Simulates two 2D crystal lattice patches (each Lx x Ly = M_patch individual lattice atoms,
    total M_tot = 2 * M_patch atoms) or a single continuous 2D lattice with a bright/dim fringe.
    """
    rng = np.random.default_rng(seed)
    coords, nn_pairs = build_2d_lattice_neighbors(Lx, Ly)
    M_patch = Lx * Ly
    M_tot = 2 * M_patch

    # 1. Coherent incident wavevector phase across the 2D lattice: phi_inc(r) = phi_0 + k . r
    phi_0 = rng.uniform(0.0, 2.0 * np.pi, size=(n_trials, 1))
    kx, ky = 0.6, 0.4  # incident wavevector projection in lattice units
    k_dot_r = kx * coords[:, 0] + ky * coords[:, 1]
    phi_inc = np.tile(k_dot_r, (n_trials, 2)) + phi_0

    # 2. Surface-conditioned quantum vacuum phase distribution (von Mises with concentration kappa_surf):
    #    kappa_surf = 0 corresponds to unconditioned free space;
    #    kappa_surf > 0 corresponds to condensed-matter Casimir-Polder + bias-field phase squeezing
    phi_surf = rng.uniform(0.0, 2.0 * np.pi, size=(n_trials, 1))
    if kappa_surf > 0.0:
        phi_vac = phi_surf + rng.vonmises(0.0, kappa_surf, size=(n_trials, M_tot))
    else:
        phi_vac = rng.uniform(0.0, 2.0 * np.pi, size=(n_trials, M_tot))

    # 3. Initial atomic/electronic phases on the crystal lattice (thermal phonon randomized):
    phi_det = rng.uniform(0.0, 2.0 * np.pi, size=(n_trials, M_tot))

    # 4. Pre-modulus 3-way phase alignment within each crystal lattice patch:
    #    At each lattice atom m, the coherent pre-modulus capture amplitude is modulated by how
    #    closely the atom's phase phi_det[m] aligns with the incident Bloch phase phi_inc[m]
    #    and the surface-conditioned virtual vacuum phase phi_vac[m]:
    #      psi_m(0) ~ A_m * (1 + alpha_vac * exp(i*(phi_vac - phi_inc))) * exp(-i*phi_det)
    align_1 = 1.0 + 0.30 * np.cos(phi_det[:, :M_patch] - 0.5 * (phi_inc[:, :M_patch] + phi_vac[:, :M_patch]))
    align_2 = 1.0 + 0.30 * np.cos(phi_det[:, M_patch:] - 0.5 * (phi_inc[:, M_patch:] + phi_vac[:, M_patch:]))
    w1 = align_1 / np.sum(align_1, axis=1, keepdims=True)
    w2 = align_2 / np.sum(align_2, axis=1, keepdims=True)

    S = np.zeros((n_trials, M_tot), dtype=float)
    S[:, :M_patch] = s_patch1 * w1
    S[:, M_patch:] = (1.0 - s_patch1) * w2

    active = np.ones(n_trials, dtype=bool)
    winner_atom = np.full(n_trials, -1, dtype=int)
    steps = np.zeros(n_trials, dtype=int)

    # Pre-build lattice neighbor index arrays for fast vectorized intra-lattice hopping
    nn_arr = np.array(nn_pairs, dtype=int)
    n_nn = len(nn_arr)

    for step_idx in range(1, max_steps + 1):
        idx = np.where(active)[0]
        if len(idx) == 0:
            break
        cur_S = S[idx]
        cur_phi = phi_det[idx]
        cur_vac = phi_vac[idx]
        K = len(idx)
        steps[idx] += 1

        # Check individual lattice-atom bandgap threshold gate: s_m > theta
        if commit_rate > 0.0 and theta < 1.0:
            exp_mask = cur_S > theta
            if np.any(exp_mask):
                rates = np.where(exp_mask, commit_rate * cur_S, 0.0)
                r_tot = np.sum(rates, axis=1)
                committed = rng.random(K) < r_tot
                if np.any(committed):
                    c_idx = idx[committed]
                    c_rates = rates[committed]
                    c_rtot = r_tot[committed]
                    cum_probs = np.cumsum(c_rates / c_rtot[:, None], axis=1)
                    u_pick = rng.random(len(c_idx))[:, None]
                    winner_atom[c_idx] = np.argmax(u_pick < cum_probs, axis=1)
                    active[c_idx] = False
                    keep = ~committed
                    idx = idx[keep]
                    cur_S = cur_S[keep]
                    cur_phi = cur_phi[keep]
                    cur_vac = cur_vac[keep]
                    K = len(idx)
                    if K == 0:
                        break

        # Dominant lattice atom pulls the local surface-conditioned vacuum phase:
        dom_atom = np.argmax(cur_S, axis=1)
        dom_phi = cur_phi[np.arange(K), dom_atom][:, None]
        if kappa_surf > 0.0:
            cur_vac = cur_vac + 0.35 * np.sin(dom_phi - cur_vac) + rng.vonmises(0.0, kappa_surf, size=(K, M_tot)) * 0.25
        else:
            cur_vac = rng.uniform(0.0, 2.0 * np.pi, size=(K, M_tot))

        # Lattice acoustic/optical phonon thermal phase modulation on the crystal sites:
        cur_phi = cur_phi + 0.20 * np.sin(cur_vac - cur_phi) + rng.uniform(-np.pi, np.pi, size=(K, M_tot))

        # Tier A: Intra-lattice nearest-neighbor exciton/dipole consolidation within each 2D crystal patch
        # Pick a random subset of disjoint lattice-neighbor bonds in Patch 1 and Patch 2
        bond_idx = rng.integers(0, n_nn, size=K)
        a1 = nn_arr[bond_idx, 0]
        b1 = nn_arr[bond_idx, 1]
        a2 = a1 + M_patch
        b2 = b1 + M_patch
        for col_i, col_j in [(a1, b1), (a2, b2)]:
            si = cur_S[np.arange(K), col_i]
            sj = cur_S[np.arange(K), col_j]
            tot = si + sj
            u = np.where(tot > 0.0, si / np.maximum(tot, 1e-30), 0.0)
            dphi = (cur_phi[np.arange(K), col_i] - cur_vac[np.arange(K), col_i]) - (
                cur_phi[np.arange(K), col_j] - cur_vac[np.arange(K), col_j]
            )
            signs = np.where(np.cos(dphi) >= 0.0, 1.0, -1.0)
            std = sigma * np.sqrt(u * (1.0 - u))
            min_s = np.minimum(u, 1.0 - u)
            du_int = signs * std
            rand_u = rng.random(K)
            a_low = (sigma ** 2) * (1.0 - u)
            du_low = np.where(rand_u < a_low / np.maximum(u + a_low, 1e-30), -u, a_low)
            v = 1.0 - u
            a_high = (sigma ** 2) * u
            du_high = np.where(rand_u < a_high / np.maximum(v + a_high, 1e-30), v, -a_high)
            near_low = (std > min_s) & (u <= 0.5) & (u > 0.0)
            near_high = (std > min_s) & (u > 0.5) & (u < 1.0)
            in_open = (u > 0.0) & (u < 1.0)
            du = np.where(near_low, du_low, np.where(near_high, du_high, du_int))
            u_new = np.where(in_open, u + du, u)
            u_new = np.where(u_new <= 1e-15, 0.0, np.where(u_new >= 1.0 - 1e-15, 1.0, u_new))
            cur_S[np.arange(K), col_i] = u_new * tot
            cur_S[np.arange(K), col_j] = (1.0 - u_new) * tot

        # Tier B: Shared wave / virtual vacuum cross-term exchange across the aperture
        perm = rng.permuted(np.tile(np.arange(M_tot), (K, 1)), axis=1)
        for p in range(0, M_tot - 1, 2):
            i_col = perm[:, p]
            j_col = perm[:, p + 1]
            si = cur_S[np.arange(K), i_col]
            sj = cur_S[np.arange(K), j_col]
            tot = si + sj
            u = np.where(tot > 0.0, si / np.maximum(tot, 1e-30), 0.0)
            if surface_vac_eps != 0.0:
                du_vac = surface_vac_eps * np.sqrt(u * (1.0 - u)) * (np.sqrt(1.0 - u) - np.sqrt(u))
                u = np.where((u > 0.0) & (u < 1.0), u + du_vac, u)
            dphi = (cur_phi[np.arange(K), i_col] - cur_vac[np.arange(K), i_col]) - (
                cur_phi[np.arange(K), j_col] - cur_vac[np.arange(K), j_col]
            )
            signs = np.where(np.cos(dphi) >= 0.0, 1.0, -1.0)
            std = sigma * np.sqrt(u * (1.0 - u))
            min_s = np.minimum(u, 1.0 - u)
            du_int = signs * std
            rand_u = rng.random(K)
            a_low = (sigma ** 2) * (1.0 - u)
            du_low = np.where(rand_u < a_low / np.maximum(u + a_low, 1e-30), -u, a_low)
            v = 1.0 - u
            a_high = (sigma ** 2) * u
            du_high = np.where(rand_u < a_high / np.maximum(v + a_high, 1e-30), v, -a_high)
            near_low = (std > min_s) & (u <= 0.5) & (u > 0.0)
            near_high = (std > min_s) & (u > 0.5) & (u < 1.0)
            in_open = (u > 0.0) & (u < 1.0)
            du = np.where(near_low, du_low, np.where(near_high, du_high, du_int))
            u_new = np.where(in_open, u + du, u)
            u_new = np.where(u_new <= 1e-15, 0.0, np.where(u_new >= 1.0 - 1e-15, 1.0, u_new))
            cur_S[np.arange(K), i_col] = u_new * tot
            cur_S[np.arange(K), j_col] = (1.0 - u_new) * tot

        max_s = np.max(cur_S, axis=1)
        done = max_s >= 1.0 - 1e-14
        if np.any(done):
            d_idx = idx[done]
            winner_atom[d_idx] = np.argmax(cur_S[done], axis=1)
            active[d_idx] = False

        S[idx] = cur_S
        phi_det[idx] = cur_phi
        phi_vac[idx] = cur_vac

    n_timeouts = int(np.sum(active))
    if n_timeouts > 0:
        a_idx = np.where(active)[0]
        winner_atom[a_idx] = np.argmax(S[a_idx], axis=1)

    win_patch1 = (winner_atom >= 0) & (winner_atom < M_patch)
    return {
        "p_patch1": round(float(np.mean(win_patch1)), 4),
        "s_patch1_born": round(float(s_patch1), 4),
        "bias": round(float(np.mean(win_patch1) - s_patch1), 4),
        "mean_steps": round(float(np.mean(steps)), 2),
        "n_timeouts": n_timeouts,
        "lattice_size_per_patch": f"{Lx}x{Ly}={M_patch}",
        "total_lattice_atoms": M_tot,
    }


def main():
    out = {}
    s_grid = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    p_lat_th072 = []
    p_lat_th045 = []
    steps_lat = []

    for i, s0 in enumerate(s_grid):
        r72 = simulate_2d_crystal_lattice_aperture(
            s_patch1=s0, Lx=4, Ly=4, theta=0.72, commit_rate=0.02, kappa_surf=2.5, surface_vac_eps=0.005, n_trials=10000, seed=5000 + i
        )
        r45 = simulate_2d_crystal_lattice_aperture(
            s_patch1=s0, Lx=4, Ly=4, theta=0.45, commit_rate=0.02, kappa_surf=2.5, surface_vac_eps=0.005, n_trials=10000, seed=6000 + i
        )
        p_lat_th072.append(r72["p_patch1"])
        p_lat_th045.append(r45["p_patch1"])
        steps_lat.append(r72["mean_steps"])

    s_arr = np.array(s_grid)
    out["2d_crystal_lattice_4x4_per_patch"] = {
        "s_grid": s_grid,
        "lattice_geometry": "Two 4x4 2D crystal lattice patches (16 atoms/patch, 32 atoms total) with nearest-neighbor exciton hopping + shared vacuum bus",
        "theta_072_p_patch1": p_lat_th072,
        "theta_072_rms_vs_born": round(float(np.sqrt(np.mean((np.array(p_lat_th072) - s_arr) ** 2))), 5),
        "theta_045_p_patch1": p_lat_th045,
        "theta_045_rms_vs_born": round(float(np.sqrt(np.mean((np.array(p_lat_th045) - s_arr) ** 2))), 5),
        "mean_steps_theta_072": steps_lat,
    }

    with open(CODE_DIR / "crystal_lattice_results.json", "w") as f:
        json.dump(out, f, indent=2)

    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
