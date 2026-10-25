#!/usr/bin/env python3
"""
Atom-by-Atom Pre-Modulus Phase-Coupled Microsimulation of a Detector Aperture
for Aperture Article 0002 (Revision 2.1 — 2026-10-24)

Physical Architecture (John M. Bramble, MD):
1. Individual Atoms in the Aperture (Not Aperture-Integrated Ports):
   Instead of collapsing each detector region/fringe into a single macroscopic port variable S
   (the "integral of the aperture"), the detector aperture consists of M_total individual
   absorbing atoms/electrons m = 1..M_total distributed across the interference pattern.
   Because any physical fringe illuminates many individual atoms (e.g., M_1 atoms in Region 1
   and M_2 atoms in Region 2), each individual atom initially holds a small amplitude
   |psi_m| << sqrt(theta), so NO single atom starts above the bandgap threshold gate theta
   (even when theta = 0.45!).

2. Surface-Conditioned Quantum Vacuum Phase & Three-Way Pre-Modulus Phase Coupling:
   - At the condensed-matter detector surface (or under an applied detector bias field E_bias),
     the local virtual vacuum modes V_m = |V_m| exp(i * phi_vac,m) have an altered, surface-
     conditioned phase distribution around a local surface reference phase phi_surf, rather than
     free-space uniform white noise.
   - During capture, the incident particle wave A_m = |A_m| exp(i * phi_inc,m), the individual
     detector atom's internal clock phase exp(i * phi_det,m), and the surface-conditioned
     virtual vacuum phase exp(i * phi_vac,m) couple BEFORE any modulus squared is evaluated.
   - Within each coherently illuminated patch/grain, the atom whose phase phi_det,m is closest
     to the incident particle phase phi_inc,m and virtual vacuum phase phi_vac,m becomes the
     dominant absorbing atom in that patch, pulling the local virtual vacuum phase into lock
     with itself and consolidating the complex wave amplitude of neighboring atoms.

3. Pairwise Pre-Modulus Complex Phase Interference Across the Aperture:
   - Active individual atoms m and n exchange complex amplitude through the shared psi-ontic
     wave and phase-pulled virtual vacuum mode via their explicit pre-modulus phase difference:
       Delta_phi_{mn}(t) = (phi_det,m(t) - phi_vac,m(t)) - (phi_det,n(t) - phi_vac,n(t)) + xi_{mn}(t),
     where the cross-term transfer is evaluated from the real part of the complex product
       2 * Re(psi_m^* * psi_n * exp(i * xi_{mn})) = 2 * |psi_m| * |psi_n| * cos(Delta_phi_{mn}(t)),
     BEFORE taking the modulus squared s_m(t) = |psi_m(t)|^2 to check whether any single
     individual atom m* has crossed the single-quantum absorption threshold!
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


def run_atom_by_atom_aperture_sim(
    s_region1=0.5,
    n_atoms_region1=10,
    n_atoms_region2=10,
    theta=0.45,
    sigma=0.25,
    commit_rate=0.02,
    surface_vac_eps=0.0,
    n_trials=20000,
    max_steps=8000,
    seed=20261024,
):
    """
    Simulates an aperture of M_total = n_atoms_region1 + n_atoms_region2 individual atoms.
    - Region 1 ("Bright" or Port 1) has total wave intensity S = s_region1 distributed across
      n_atoms_region1 individual atoms, so each atom m in Region 1 has incident wave amplitude
      |A_m| = sqrt(s_region1 / n_atoms_region1).
    - Region 2 ("Dim" or Port 2) has total wave intensity 1 - S distributed across
      n_atoms_region2 individual atoms, so each atom n in Region 2 has incident wave amplitude
      |A_n| = sqrt((1 - s_region1) / n_atoms_region2).

    Notice the crucial physical difference from an aperture-integrated model:
    Even when S = 0.50 and theta = 0.45, with n_atoms_region1 = 10 individual atoms in Region 1,
    each individual atom in Region 1 starts with intensity |A_m|^2 = 0.50 / 10 = 0.050 << 0.45!
    Thus NO atom starts above theta = 0.45 at t = 0. An individual atom can only cross theta = 0.45
    after pre-modulus phase alignment with the incident wave and surface vacuum makes it a dominant
    absorbing atom that consolidates amplitude from the rest of the aperture!

    Pre-modulus phase dynamics at each step:
    - Each atom m carries explicit phase phi_det[m] and modulus r_m = |psi_m| (with s_m = r_m^2).
    - The surface-conditioned virtual vacuum phase phi_vac is pulled toward the amplitude-weighted
      dominant atomic phase in each local region, plus surface fluctuations.
    - When two active atoms (m, n) interact via the shared wave + virtual vacuum, their explicit
      phase difference Delta_phi = phi_det[m] - phi_det[n] + phi_vac_pull determines the sign and
      magnitude of the pre-modulus cross-term 2 * Re(psi_m^* psi_n exp(i * xi)).
    """
    rng = np.random.default_rng(seed)
    M1 = n_atoms_region1
    M2 = n_atoms_region2
    M_tot = M1 + M2

    # 1. Pre-modulus initial complex amplitudes at each individual atom m = 0..M_tot-1:
    # Incident phase phi_inc, initial atomic clock phase phi_det, and surface-biased vacuum phase phi_vac
    phi_inc = rng.uniform(0.0, 2.0 * np.pi, size=(n_trials, M_tot))
    phi_det = rng.uniform(0.0, 2.0 * np.pi, size=(n_trials, M_tot))
    # Surface-conditioned vacuum phase: narrowed around local surface bias (von Mises / Gaussian around phi_surf)
    phi_surf = rng.uniform(0.0, 2.0 * np.pi, size=(n_trials, 1))
    phi_vac = phi_surf + rng.normal(0.0, 0.5, size=(n_trials, M_tot))

    # Pre-modulus 3-way phase alignment factor at capture within each iso-intensity fringe:
    # Atoms whose phase phi_det is closer to (phi_inc + phi_vac)/2 within the same fringe
    # capture a slightly larger share of that fringe's wave amplitude (dominant atom seeding),
    # while preserving the exact total wave intensity S in Region 1 and (1-S) in Region 2:
    align_score = 1.0 + 0.25 * np.cos(phi_det - 0.5 * (phi_inc + phi_vac))
    w1 = align_score[:, :M1]
    w1 = w1 / np.sum(w1, axis=1, keepdims=True)
    w2 = align_score[:, M1:]
    w2 = w2 / np.sum(w2, axis=1, keepdims=True)

    S = np.zeros((n_trials, M_tot), dtype=float)
    S[:, :M1] = s_region1 * w1
    S[:, M1:] = (1.0 - s_region1) * w2

    active = np.ones(n_trials, dtype=bool)
    winner_atom = np.full(n_trials, -1, dtype=int)
    steps = np.zeros(n_trials, dtype=int)

    for _ in range(1, max_steps + 1):
        idx = np.where(active)[0]
        if len(idx) == 0:
            break
        cur_S = S[idx]
        cur_phi = phi_det[idx]
        cur_vac = phi_vac[idx]
        K = len(idx)
        steps[idx] += 1

        # Check individual-atom threshold gate: does any SINGLE atom m have s_m > theta?
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

        # Update explicit atomic and vacuum phases (dominant absorbing atoms pull the vacuum phase):
        # Dominant atom in each trial pulls the local surface vacuum phase toward its own phase
        dom_atom = np.argmax(cur_S, axis=1)
        dom_phi = cur_phi[np.arange(K), dom_atom][:, None]
        cur_vac = cur_vac + 0.3 * np.sin(dom_phi - cur_vac) + rng.normal(0.0, 0.4, size=(K, M_tot))
        # Atomic clock phases evolve with surface-vacuum coupling + thermal/phonon dephasing
        cur_phi = cur_phi + 0.15 * np.sin(cur_vac - cur_phi) + rng.uniform(-np.pi, np.pi, size=(K, M_tot))

        # Pairwise pre-modulus complex interference exchange between active individual atoms:
        perm = rng.permuted(np.tile(np.arange(M_tot), (K, 1)), axis=1)
        for p in range(0, M_tot - 1, 2):
            i_col = perm[:, p]
            j_col = perm[:, p + 1]
            si = cur_S[np.arange(K), i_col]
            sj = cur_S[np.arange(K), j_col]
            tot = si + sj
            act_pair = tot > 0.0
            u = np.where(act_pair, si / np.maximum(tot, 1e-30), 0.0)

            if surface_vac_eps != 0.0:
                du_vac = surface_vac_eps * np.sqrt(u * (1.0 - u)) * (np.sqrt(1.0 - u) - np.sqrt(u))
                u = np.where((u > 0.0) & (u < 1.0), u + du_vac, u)

            # Explicit pre-modulus phase difference between atom i and atom j coupled to vacuum:
            dphi = (cur_phi[np.arange(K), i_col] - cur_vac[np.arange(K), i_col]) - (
                cur_phi[np.arange(K), j_col] - cur_vac[np.arange(K), j_col]
            )
            signs = np.where(np.cos(dphi) >= 0.0, 1.0, -1.0)

            std = sigma * np.sqrt(u * (1.0 - u))
            min_side = np.minimum(u, 1.0 - u)
            du_int = signs * std

            rand_u = rng.random(K)
            a_low = (sigma ** 2) * (1.0 - u)
            p0_low = a_low / np.maximum(u + a_low, 1e-30)
            du_low = np.where(rand_u < p0_low, -u, a_low)

            v = 1.0 - u
            a_high = (sigma ** 2) * u
            p1_high = a_high / np.maximum(v + a_high, 1e-30)
            du_high = np.where(rand_u < p1_high, v, -a_high)

            near_low = (std > min_side) & (u <= 0.5) & (u > 0.0)
            near_high = (std > min_side) & (u > 0.5) & (u < 1.0)
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

    # Region 1 wins if the winning individual atom m* is in 0 .. M1-1
    win_region1 = (winner_atom >= 0) & (winner_atom < M1)
    return {
        "p_region1": round(float(np.mean(win_region1)), 4),
        "s_region1_born": round(float(s_region1), 4),
        "bias": round(float(np.mean(win_region1) - s_region1), 4),
        "mean_steps": round(float(np.mean(steps)), 2),
        "n_timeouts": n_timeouts,
        "M1_atoms": M1,
        "M2_atoms": M2,
        "max_initial_atom_share": round(float(max(s_region1 / M1, (1.0 - s_region1) / M2)), 4),
    }


def main():
    results = {}

    # 1. Compare Aperture-Integrated (1 giant "atom" per region) vs. Multi-Atom Aperture
    #    at theta = 0.45 and theta = 0.72!
    #    In the 10-site test of v1.0, Region 1 ("Bright fringe") had Born weight 0.5000 concentrated
    #    on ONE single giant site (M1 = 1, so s_0(0) = 0.50 > theta = 0.45!), while Region 2 ("Dim
    #    background") had 0.5000 spread across M2 = 9 sites (s_i(0) = 1/18 = 0.0556 << theta = 0.45).
    #    What happens when the Bright fringe is resolved into M1 = 9 individual atoms (each with
    #    initial intensity 0.50 / 9 = 0.0556, or M1 = 5 atoms each with 0.10, or M1 = 9 atoms with
    #    higher local density) vs M2 = 9 or 18 dim atoms, so NO single atom starts above theta = 0.45?
    results["theta_045_aperture_resolution_test"] = {
        "lumped_1_bright_vs_9_dim_no_vac": run_atom_by_atom_aperture_sim(
            s_region1=0.50, n_atoms_region1=1, n_atoms_region2=9, theta=0.45, commit_rate=0.02, surface_vac_eps=0.0, seed=1001
        ),
        "resolved_5_bright_vs_15_dim_no_vac": run_atom_by_atom_aperture_sim(
            s_region1=0.50, n_atoms_region1=5, n_atoms_region2=15, theta=0.45, commit_rate=0.02, surface_vac_eps=0.0, seed=1002
        ),
        "resolved_5_bright_vs_15_dim_with_surface_vac": run_atom_by_atom_aperture_sim(
            s_region1=0.50, n_atoms_region1=5, n_atoms_region2=15, theta=0.45, commit_rate=0.02, surface_vac_eps=0.008, seed=1003
        ),
        "resolved_10_bright_vs_10_dim_no_vac": run_atom_by_atom_aperture_sim(
            s_region1=0.50, n_atoms_region1=10, n_atoms_region2=10, theta=0.45, commit_rate=0.02, surface_vac_eps=0.0, seed=1004
        ),
    }

    # 2. Nine-angle sweep (S in 0.1 .. 0.9) on a 20-atom detector aperture
    #    (M1 = 10 individual atoms in Detector Arm 1, M2 = 10 individual atoms in Detector Arm 2)
    #    at BOTH theta = 0.72 and theta = 0.45!
    #    Notice that even at S = 0.90, each individual atom in Arm 1 starts with average share
    #    0.90 / 10 = 0.090 << theta = 0.45!
    s_grid = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    p_20atom_disc = []
    p_20atom_th072_novac = []
    p_20atom_th072_vac = []
    p_20atom_th045_novac = []
    p_20atom_th045_vac = []

    for i, s0 in enumerate(s_grid):
        r_d = run_atom_by_atom_aperture_sim(
            s_region1=s0, n_atoms_region1=10, n_atoms_region2=10, theta=1.0, commit_rate=0.0, surface_vac_eps=0.0, n_trials=12000, seed=2000 + i
        )
        r_72_0 = run_atom_by_atom_aperture_sim(
            s_region1=s0, n_atoms_region1=10, n_atoms_region2=10, theta=0.72, commit_rate=0.02, surface_vac_eps=0.0, n_trials=12000, seed=2100 + i
        )
        r_72_v = run_atom_by_atom_aperture_sim(
            s_region1=s0, n_atoms_region1=10, n_atoms_region2=10, theta=0.72, commit_rate=0.02, surface_vac_eps=0.006, n_trials=12000, seed=2200 + i
        )
        r_45_0 = run_atom_by_atom_aperture_sim(
            s_region1=s0, n_atoms_region1=10, n_atoms_region2=10, theta=0.45, commit_rate=0.02, surface_vac_eps=0.0, n_trials=12000, seed=2300 + i
        )
        r_45_v = run_atom_by_atom_aperture_sim(
            s_region1=s0, n_atoms_region1=10, n_atoms_region2=10, theta=0.45, commit_rate=0.02, surface_vac_eps=0.006, n_trials=12000, seed=2400 + i
        )
        p_20atom_disc.append(r_d["p_region1"])
        p_20atom_th072_novac.append(r_72_0["p_region1"])
        p_20atom_th072_vac.append(r_72_v["p_region1"])
        p_20atom_th045_novac.append(r_45_0["p_region1"])
        p_20atom_th045_vac.append(r_45_v["p_region1"])

    s_arr = np.array(s_grid)
    results["twenty_atom_aperture_sweep"] = {
        "s_grid": s_grid,
        "M1_atoms_per_port": 10,
        "M2_atoms_per_port": 10,
        "n_trials_per_point": 12000,
        "discrete_theta_1": {
            "p_region1": p_20atom_disc,
            "rms_vs_born": round(float(np.sqrt(np.mean((np.array(p_20atom_disc) - s_arr) ** 2))), 5),
        },
        "gated_theta_072_no_vac": {
            "p_region1": p_20atom_th072_novac,
            "rms_vs_born": round(float(np.sqrt(np.mean((np.array(p_20atom_th072_novac) - s_arr) ** 2))), 5),
        },
        "gated_theta_072_vac_0006": {
            "p_region1": p_20atom_th072_vac,
            "rms_vs_born": round(float(np.sqrt(np.mean((np.array(p_20atom_th072_vac) - s_arr) ** 2))), 5),
        },
        "gated_theta_045_no_vac": {
            "p_region1": p_20atom_th045_novac,
            "rms_vs_born": round(float(np.sqrt(np.mean((np.array(p_20atom_th045_novac) - s_arr) ** 2))), 5),
        },
        "gated_theta_045_vac_0006": {
            "p_region1": p_20atom_th045_vac,
            "rms_vs_born": round(float(np.sqrt(np.mean((np.array(p_20atom_th045_vac) - s_arr) ** 2))), 5),
        },
    }

    out_path = CODE_DIR / "atom_by_atom_aperture_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
