def sum_square_diff(numbers):
    return square_of_sum(numbers) - sum_of_squares(numbers)


def sum_of_squares(numbers):
    """Calculate the sum of all the squares in the number set."""
    return sum(x**2 for x in xrange(1, numbers+1))


def square_of_sum(numbers):
    """Calculate the sum of the numbers and then square it."""
    return sum(x for x in xrange(1, numbers+1)) ** 2


class TestSumSquareDiff:

    def test_it_computes_the_example(self):
        assert sum_square_diff(numbers=10) == 2640

    def test_it_calculates_sum_of_squares(self):
        assert sum_of_squares(numbers=10) == 385

    def test_it_calculates_square_of_sum(self):
        assert square_of_sum(numbers=10) == 3025

    def test_it_answers_the_question(self):
        assert sum_square_diff(numbers=100) == 25164150
