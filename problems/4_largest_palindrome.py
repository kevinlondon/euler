def find_palindromes(digits):
    max_number = int('9' * digits)
    max_palindrome = 0

    for x in xrange(max_number + 1):
        for y in xrange(max_number + 1):
            product = x * y
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product

    return int(max_palindrome)


def is_palindrome(product):
    product = str(product)
    midpoint = len(product) // 2

    first_section = product[:midpoint]
    if len(product) % 2 == 0:
        second_section = product[midpoint:]
    else:
        # Need to offset by 1
        second_section = product[midpoint+1:]

    return first_section == second_section[::-1]


def test_find_palindromes_with_2_digits():
    assert find_palindromes(digits=2) == 9009


def test_find_palindromes_with_3_digits():
    assert find_palindromes(digits=3) == 906609


def test_is_palindrome_even_digits():
    assert is_palindrome(9009)


def test_not_a_palindrome():
    assert not is_palindrome(9883)


def test_is_palindrome_odd_digits():
    assert is_palindrome(92329)
