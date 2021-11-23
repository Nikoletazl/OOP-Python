import functools


def is_vowel(ch):
    return ch in ("eyuoa" + "eyuoa".upper())


def vowel_filter(function):
    @functools.wraps(function)
    def wrapper():
        result = function()
        return [ch for ch in result if is_vowel(ch)]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
