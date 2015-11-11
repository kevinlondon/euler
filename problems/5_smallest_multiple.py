def smallest_multiple(maximum):
    smallest_multiple = 1
    for x in xrange(1, maximum+1):
        smallest_multiple = least_common_multiple(x, smallest_multiple)

    return smallest_multiple


def least_common_multiple(a, b):
    return (a * b) / greatest_common_divisor(a, b)


def greatest_common_divisor(a, b):
    if a == b:
        return a
    elif a <= 0:
        return b
    elif b <= 0:
        return a

    divisor = 0

    while a % 2 == 0 and b % 2 == 0:
        a /= 2
        b /= 2
        divisor += 1

    while a != b:
        if a % 2 == 0:
            a /= 2
        elif b % 2 == 0:
            b /= 2
        elif a > b:
            a = (a - b) / 2
        else:
            b = (b - a) / 2

    return a * (2**divisor)


def is_multiple(current_number, maximum):
    for x in xrange(maximum, 0, -1):
        if current_number % x != 0:
            print current_number
            return False
    else:
        return True


class TestGreatestDivisor:

    def test_greatest_common_divisor(self):
        assert greatest_common_divisor(18, 84) == 6


class TestLeastCommonMultiple:

    def test_least_common_multiple(self):
        assert least_common_multiple(21, 6) == 42


class TestSmallestMultiple:

    def test_smallest_multiple_2(self):
        assert smallest_multiple(maximum=2) == 2

    def test_smallest_multiple_3(self):
        assert smallest_multiple(maximum=3) == 6

    def test_smallest_multiple_4(self):
        assert smallest_multiple(maximum=4) == 12

    def test_smallest_multiple_answer(self):
        assert smallest_multiple(maximum=20) == 232792560
