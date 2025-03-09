import pytest
from primes_sk.prime_factors import compute_prime_factors

def test_prime_factors_of_1():
    assert compute_prime_factors(1) == []


def test_prime_factors_of_2():
    assert compute_prime_factors(2) == [2]


def test_prime_factors_of_3():
    assert compute_prime_factors(3) == [3]

@pytest.mark.parametrize("n, primes", [(1, []), (2, [2]), (3, [3]), (4, [2, 2]), (5, [5]), 
                                       (6, [2, 3]), (7, [7])])

def test_compute_prime_factors(n, primes):
    assert compute_prime_factors(n) == primes