from Excercise8.excercise8 import binary_search_recursive


def advanced_search(search_list: list, target_list: list) -> list:
    try:
        return list(map(lambda x: binary_search_recursive(search_list, x), target_list))
    except Exception as e:
        print(e)
        raise ValueError(e)


def test_advanced_search():
    # Unit test empty list
    assert advanced_search([], []) == []

    # Unit test 2 list
    assert advanced_search([2, 5, 6], [2, 4, 6, 8]) == [True, False, True, False]


test_advanced_search()
