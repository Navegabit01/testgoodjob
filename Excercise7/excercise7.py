PARAMS_MUST_BE_LIST = 'El parámetro debe ser una lista.'
NO_HASHED_ELEMENTS = 'La lista contiene elementos no hashables.'


def remove_duplicates(lst: list):
    """
    This function accepts a list as a parameter and returns a new list with no duplicate elements.
    """
    try:
        return list(set(lst))
    except TypeError:
        raise TypeError(NO_HASHED_ELEMENTS)


# Unit Test
def test_remove_duplicates():
    # Unit test empty list
    assert remove_duplicates([]) == []

    # Unit test no duplicate elements
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    # Unit test duplicate elements
    assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3]


test_remove_duplicates()
