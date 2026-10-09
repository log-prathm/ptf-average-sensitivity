# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Prathmesh Lagdive, Vaibhav Aglave, Suraj Damre

"""Numerical checks, supplemental to the analytic and exact-arithmetic proof.

Uses NumPy 2.3.2 and SciPy 1.16.1. Run with a matching isolated environment.
LP outputs are floating-point exploration, not rigorous optimality certificates.
"""

from itertools import combinations
from math import comb, sqrt
from pathlib import Path
import json

import numpy as np
import scipy
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def coupling_case(n, d):
    pairs = [(u, v) for u in range(n+1) for v in range(n+1) if v-u <= d]
    u = np.array([pair[0] for pair in pairs])
    v = np.array([pair[1] for pair in pairs])
    k = len(pairs)
    mu = np.array([comb(n, i) / 2**n for i in range(n+1)])
    a = coo_matrix(
        (np.ones(2*k), (np.r_[u, n+1+v],
                       np.r_[np.arange(k), np.arange(k)])),
        shape=(2*(n+1), k),
    ).tocsr()
    objective = (u-v)**2
    sol = linprog(-objective.astype(float), A_eq=a, b_eq=np.r_[mu, mu],
                  bounds=(0, None), method="highs")
    if not sol.success:
        raise RuntimeError(sol.message)
    b = sum(abs(i-n/2)*mu[i] for i in range(n+1))
    maximum = -sol.fun
    bound = min(4*d*b + d*d, 5*d*b)
    assert maximum <= bound + 1e-6
    return {"n": n, "d": d, "lp_second_moment": float(maximum),
            "analytic_second_moment_bound": float(bound),
            "marginal_residual": float(np.max(np.abs(a @ sol.x - np.r_[mu, mu]))),
            "relaxed_influence_coefficient": min(n, 2*maximum)/(d*sqrt(n))}


def grading_case(n, d, rng):
    size = 2**n
    vertices = np.arange(size)
    x = np.array([1-2*((vertices >> i) & 1) for i in range(n)]).T
    subsets = [s for degree in range(n+1)
               for s in combinations(range(n), degree)]
    degree = np.array([len(s) for s in subsets])
    features = np.column_stack([
        np.prod(x[:, s], axis=1) if s else np.ones(size) for s in subsets
    ])
    coefficients = rng.normal(size=int(np.sum(degree <= d)))
    p = features[:, degree <= d] @ coefficients
    assert np.min(np.abs(p)) > 1e-10
    sign = np.where(p >= 0, 1, -1)
    h = np.prod(x, axis=1) * sign
    q, _ = np.linalg.qr(np.sqrt(np.abs(p))[:, None] * features)
    grading = (q * (degree-n/2)) @ q.T
    anticommutator = (h[:, None] + h[None, :]) * grading
    energy = float(np.sum(anticommutator**2) / size)
    influence = sum(np.mean(sign != sign[vertices ^ (1 << i)]) for i in range(n))
    blocks = q.T @ (h[:, None] * q)
    below_degree_constraint = degree[:, None] + degree[None, :] < n-d
    support_error = float(np.max(np.abs(blocks[below_degree_constraint]), initial=0))
    block_energy = float(np.sum((degree[:, None]+degree[None, :]-n)**2 * blocks**2)/size)
    deviation = sum(abs(i-n/2)*comb(n, i)/2**n for i in range(n+1))
    assert influence <= 2*energy + 1e-8
    assert abs(energy-block_energy) < 1e-8
    assert support_error < 1e-8
    assert energy <= min(4*d*deviation + d*d, 5*d*deviation) + 1e-8
    assert influence <= 3.83*d*sqrt(n) + 1e-8
    return {"n": n, "d": d, "influence": float(influence),
            "anticommutator_energy_per_vertex": energy,
            "forbidden_block_error": support_error,
            "block_energy_residual": abs(energy-block_energy)}


def main():
    rng = np.random.default_rng(127)
    couplings = [coupling_case(n, d) for n, d in
                 [(5, 1), (10, 1), (15, 1), (20, 2), (30, 3),
                  (50, 2), (80, 1), (80, 10)]]
    gradings = [grading_case(n, d, rng) for n in range(1, 7)
                for d in range(1, n+1) for _ in range(3)]
    results = {"numpy_version": np.__version__, "scipy_version": scipy.__version__,
               "random_seed": 127, "couplings": couplings, "gradings": gradings,
               "scope": "Numerical sanity checks; not a proof or exact LP certificate."}
    Path(__file__).with_name("127-numerical-checks.json").write_text(
        json.dumps(results, indent=2) + "\n")
    print(f"Checked {len(couplings)} coupling LPs and {len(gradings)} weighted gradings.")
    print(f"Maximum forbidden-block error: {max(r['forbidden_block_error'] for r in gradings):.3g}")


if __name__ == "__main__":
    main()
