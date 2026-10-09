# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Prathmesh Lagdive, Vaibhav Aglave, Suraj Damre

"""Exact checks accompanying the analytic proof in the accompanying manuscript.

These checks cover finite instances and rational constants. The universal
quantifiers are justified by the induction and case split in the proof.
Run: python3 verify_127.py
"""

from fractions import Fraction
from math import comb
from pathlib import Path
import json


def main():
    constant = Fraction(383, 100)
    certificate = (constant**2 - 2)**2 - Fraction(120, 11) * constant**2
    assert certificate == Fraction(524329931, 1100000000)
    assert certificate > 0 and constant**2 > 2

    identity_dimensions = (1, 2, 5, 10, 15, 50, 100, 1000)
    for n in identity_dimensions:
        direct = sum(
            Fraction(comb(n, k), 2**n) * abs(Fraction(k) - Fraction(n, 2))
            for k in range(n + 1)
        )
        formula = Fraction(n * comb(n - 1, (n - 1) // 2), 2**n)
        assert direct == formula

    for k in range(2001):
        c = Fraction(comb(2*k, k), 4**k)
        assert c*c * (3*k + 1) <= 1
        assert ((2*k + 2)**2 * (3*k + 1)
                - (2*k + 1)**2 * (3*k + 4)) == k

    nontrivial_cases = 0
    trivial_cases = 0
    max_squared = Fraction(0)
    maximizer = None
    for n in range(1, 2001):
        b = Fraction(n * comb(n - 1, (n - 1) // 2), 2**n)
        for d in range(1, n + 1):
            if n * 10000 <= 383**2 * d*d:
                # This is exactly n <= C^2 d^2; I <= n proves this branch.
                trivial_cases += 1
                continue
            bound = min(Fraction(n), 8*d*b + 2*d*d, 10*d*b)
            squared = bound*bound / (d*d*n)
            assert squared <= constant*constant, (n, d, squared)
            nontrivial_cases += 1
            if squared > max_squared:
                max_squared = squared
                maximizer = [n, d]

    # Rational-grid checks of the pointwise inequalities used in the lemma.
    grid = [Fraction(k, 4) for k in range(-40, 41)]
    interval_checks = 0
    def g(t):
        return t*abs(t)/2
    for u in grid:
        for v in grid:
            if v <= u:
                continue
            difference = g(v) - g(u)
            assert (v-u)**2 / 4 <= difference
            assert difference <= (v-u) * (abs(u)+abs(v)) / 2
            interval_checks += 1

    result = {
        "constant": str(constant),
        "algebraic_certificate": str(certificate),
        "binomial_identity_dimensions": list(identity_dimensions),
        "central_binomial_checks": 2001,
        "maximum_dimension": 2000,
        "nontrivial_dimension_degree_cases": nontrivial_cases,
        "trivial_dimension_degree_cases": trivial_cases,
        "rational_interval_checks": interval_checks,
        "largest_squared_coefficient_in_nontrivial_cases": str(max_squared),
        "finite_maximizer": maximizer,
        "scope": "Exact finite checks; universal proof is in the accompanying manuscript.",
    }
    dest = Path(__file__).with_name("127-exact-verification.json")
    dest.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
