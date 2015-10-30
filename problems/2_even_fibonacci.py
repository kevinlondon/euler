def add_even_fibonacci(maximum):
    fibonacci_sequence = [1, 2]
    current_term = 2
    even_total = 0

    while current_term <= maximum:
        if current_term % 2 == 0:
            even_total += current_term
        current_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(current_term)

    return even_total


def test_small_fibonacci_sequence():
    assert add_even_fibonacci(maximum=100) == 44


def test_fibonacci_sequence_max():
    assert add_even_fibonacci(maximum=4000000) == 4613732
