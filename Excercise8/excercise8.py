EMPTY_LIST_ERROR = 'La lista está vacía'
LIST_INT_ELEMENT_ERROR = 'La lista debe contener solo números enteros'


def binary_search_recursive(list1: list, target1: int) -> bool:
    if not arr:
        raise ValueError(EMPTY_LIST_ERROR)

    if not all(isinstance(x, int) for x in arr):
        raise TypeError(LIST_INT_ELEMENT_ERROR)
    return _binary_search_recursive(list1, target1, 0, len(arr) - 1)


def _binary_search_recursive(derivate_list: list, derivate_target: int, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if derivate_list[mid] == derivate_target:
        return True
    elif derivate_list[mid] < derivate_target:
        return _binary_search_recursive(derivate_list, derivate_target, mid + 1, right)
    else:
        return _binary_search_recursive(derivate_list, derivate_target, left, mid - 1)


arr = [1, 2, 5, 6, 8, 11, 32, 44, 66, 77]
target = 5

try:
    result = binary_search_recursive(arr, target)
    print(f"El número {target} {'está' if result else 'no está'} en la lista")
except Exception as e:
    print(f"Error: {e}")
