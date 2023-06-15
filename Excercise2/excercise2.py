EMPTY_ARRAY = 'El array está vacío'
ELEMENT_NOT_INT = 'Los elementos del array deben ser enteros'


def find_median(arr):
    try:
        if not arr:
            return ValueError(EMPTY_ARRAY)
        arr.sort()
        total = len(arr)
        if total % 2 == 0:
            return (arr[total // 2 - 1] + arr[total // 2]) / 2
        else:
            return arr[total // 2]
    except TypeError:
        return TypeError(ELEMENT_NOT_INT)
    except Exception as error:
        raise ValueError(error)


def test_find_median():
    # Test case for odd length array
    assert find_median([1, 2, 3, 4, 5]) == 3

    # Test case for even length array
    assert find_median([1, 2, 3, 4]) == 2.5

    # Test case for empty array
    assert find_median([]).args == ValueError(EMPTY_ARRAY).args

    # Test case for unsorted array
    assert find_median([5, 3, 2, 4, 1]) == 3

    # Test case for non-integer elements in array
    assert find_median([1, "2", 3, 4]).args == TypeError(ELEMENT_NOT_INT).args
