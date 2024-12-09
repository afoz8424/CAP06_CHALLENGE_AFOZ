import pytest

from func import es_primo

# Happy path
# Returns True for prime numbers like 2, 3, 5, 7
def test_returns_true_for_prime_numbers():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for number in prime_numbers:
        assert es_primo(number) is True

# Returns False for non-prime numbers like 4, 6, 8, 9
def test_returns_false_for_non_prime_numbers():
    non_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
    for number in non_prime_numbers:
        assert es_primo(number) is False

# Handles small prime numbers correctly
def test_handles_small_prime_numbers():
    small_primes = [2, 3, 5, 7]
    for prime in small_primes:
        assert es_primo(prime) is True

# Handles small non-prime numbers correctly
def test_returns_false_for_small_non_prime_numbers():
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10]
    for number in non_prime_numbers:
        assert es_primo(number) is False

# Edge cases
# Returns True for the smallest prime number, 2
def test_returns_true_for_smallest_prime_number():
    assert es_primo(2) == True

# Returns False for 1, which is not a prime number
def test_returns_false_for_one():
    assert es_primo(1) == False

# Handles negative numbers by returning False
def test_handles_negative_numbers():
    negative_numbers = [-1, -10, -100]
    for num in negative_numbers:
        assert es_primo(num) == False

# Handles very large prime numbers efficiently
def test_large_prime_number():
    # A known large prime number
    large_prime = 104729  # 10000th prime number
    assert es_primo(large_prime) == True

# Handles very large non-prime numbers efficiently
def test_large_non_prime_number():
    large_non_prime = 10**12  # A very large non-prime number
    assert es_primo(large_non_prime) == False

# Other cases
# Handles floating-point numbers by returning False
def test_returns_false_for_floating_point_numbers():
    floating_points = [2.5, 3.1, 5.7]
    for num in floating_points:
        assert es_primo(num) == False

# Handles non-integer inputs by raising an error or returning False
def test_non_integer_inputs():
    non_integer_inputs = ["string", 3.5, None, True, False, [], {}]
    for input_value in non_integer_inputs:
        assert es_primo(input_value) is False

# Handles the number 0 correctly as non-prime
def test_handles_zero_as_non_prime():
    assert es_primo(0) == False

# Handles with float numbers very close to integers
def test_handles_float_numbers_very_close_to_integers():
    assert es_primo(19.000000000000004) is True
    assert es_primo(23.000000000000004) is True
    assert es_primo(20.000000000000004) is False
