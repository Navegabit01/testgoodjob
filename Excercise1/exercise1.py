def merge_arrays(integer_list1: list, integer_list2: list) -> list:
    """
    Merge two list of integers and return the sorted list
    """
    merge_list: list = []
    try:
        merge_list = integer_list1 + integer_list2
        merge_list = list(map(int, merge_list))
        merge_list.sort()
    except Exception as errors:
        # Manage any errors maybe in sentry
        print(errors)
        raise ValueError(errors)
    finally:
        # Manage memory release
        del integer_list1, integer_list2
        return merge_list


print(merge_arrays([1, 2, 1], [3, 4]))

# Apply tests
# Test case 1
assert merge_arrays([1, 1, 2, 5], [3, 4, 5, 7]) == [1, 1, 2, 3, 4, 5, 5, 7]

# Test case 2
assert merge_arrays([], []) == []

# Test case 3
assert merge_arrays([1], [1]) == [1, 1]

# Test case 4
assert merge_arrays([1, 3], [2, 4, 6]) == [1, 2, 3, 4, 6]
