import pytest


def get_shortest_and_longest_word(string):
    word_length_dict = {}
    if len(string) > 0:
        for word in string.split():
            word_length_dict[word] = len(word)
            sorted_dict = sorted(word_length_dict, key=word_length_dict.__getitem__)

        # print(sorted_dict)
        short_word = sorted_dict[0]
        long_word = sorted_dict[-1]
        # print("the shortest word is '{0}', the longest is '{1}'".format(short_word, long_word))
        return short_word, long_word


def test_should_return_two_words_when_passed_a_string_of_words():
    result = get_shortest_and_longest_word('a cow jumped over the moon')
    print(result)
    assert len(result) == 2


def test_returns_the_short_word_as_a():
    result = get_shortest_and_longest_word('a cow jumped over the moon')
    assert result[0] == 'a'


def test_returns_the_long_word_as_jumped():
    result = get_shortest_and_longest_word('a cow jumped over the moon')
    assert result[1] == 'jumped'


def test_returns_same_word_for_short_and_long_single_word_string():
    result = get_shortest_and_longest_word('word')
    assert result[0] == 'word'
    assert result[1] == 'word'


def test_empty_string_should_return_none():
    result = get_shortest_and_longest_word('')
    assert result is None


def test_string_is_numbered_returns_error():
    with pytest.raises(Exception):
        result = get_shortest_and_longest_word(1234)
        error = "TypeError: object of type 'int' has no len()"
        print(result)
        raise Exception(error)
