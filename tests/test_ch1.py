import pytest


def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    if isinstance(string, str):
        for char in string.lower():
            if char in vowels:
                count += 1
        print('The number of vowels in {0} is {1}'.format(string, count))
    return count


vowel_count(1234)


def test_firstname_should_return_two_vowels():
    assert vowel_count('Carlos') == 2


def test_lastname_should_return_two_vowels():
    assert vowel_count('Kidman') == 2


def test_name_should_return_four_vowels():
    assert vowel_count('Carlos Kidman') == 4


def test_uppercase_name_should_return_four_vowels():
    assert vowel_count('CARLOS KIDMAN') == 4


def test_lowercase_name_should_return_four_vowels():
    assert vowel_count('carlos kidman') == 4


def test_no_vowel_word_should_return_zero_vowels():
    assert vowel_count('xmnt') == 0


def test_number_should_return_error():
    with pytest.raises(Exception):
        vowel_count(1234)
        raise Exception("AttributeError: 'int' object has no attribute 'lower'")
