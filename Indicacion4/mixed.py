import threading

from Excercise8.excercise8 import binary_search_recursive


def advanced_search(search_list: list, target_list: list) -> list:
    try:
        return list(map(lambda x: binary_search_recursive(search_list, x), target_list))
    except Exception as e:
        print(e)
        raise ValueError(e)


def advanced_search_threads(search_list: list, target_list: list) -> list:
    try:
        results = [None] * len(target_list)
        threads = []

        # Define a function to run in each thread
        def search_thread(index):
            results[index] = binary_search_recursive(search_list, target_list[index])

        # Create a thread for each target in the list
        for i in range(len(target_list)):
            thread = threading.Thread(target=search_thread, args=(i,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        return results

    except Exception as e:
        print(e)
        raise ValueError(e)


def test_advanced_search():
    # Unit test empty list
    assert advanced_search([], []) == []

    # Unit test 2 list
    assert advanced_search([2, 5, 6], [2, 4, 6, 8]) == [True, False, True, False]

def test_advanced_search_threads():
    # Unit test empty list
    assert advanced_search_threads([], []) == []

    # Unit test 2 list
    assert advanced_search_threads([2, 5, 6], [2, 4, 6, 8]) == [True, False, True, False]


test_advanced_search()
