import pytest
from is_prime import is_prime

# Functional Tests
def test_is_prime_basic():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(10) == False
    assert is_prime(13) == True

def test_is_prime_negative():
    assert is_prime(-1) == False
    assert is_prime(-10) == False

def test_is_prime_zero_one():
    assert is_prime(0) == False
    assert is_prime(1) == False

def test_is_prime_large_prime():
    assert is_prime(104729) == True  # 10000th prime number

def test_is_prime_large_non_prime():
    assert is_prime(104728) == False

# Non-Functional Tests
def test_is_prime_performance():
    import time
    start_time = time.time()
    is_prime(2**31 - 1)  # A large prime number, 7th Mersenne prime
    duration = time.time() - start_time
    assert duration < 1  # Test should complete within 1 second

def test_is_prime_type_error():
    with pytest.raises(TypeError):
        is_prime("a string")

    with pytest.raises(TypeError):
        is_prime(None)

    with pytest.raises(TypeError):
        is_prime(5.5)

if __name__ == "__main__":
    pytest.main()
