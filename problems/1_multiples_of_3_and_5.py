def add_multiples(maximum):
    """Add all numbers that are multiples of 3 and 5 below the maximum."""
    total = 0
    for x in range(maximum):
        if x % 3 == 0 or x % 5 == 0:
            total += x

    return total


def test_multiples_under_ten():
    assert add_multiples(10) == 23


def test_multiples_under_1000():
    assert add_multiples(1000) == 233168
