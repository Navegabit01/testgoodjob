import math
import multiprocessing
import threading

from Excercise8.excercise8 import binary_search_recursive


def advanced_search(search_list: list, target_list: list, result: list) -> None:
    result.extend(list(map(lambda x: binary_search_recursive(search_list, x), target_list)))


def advanced_search_threads(search_list: list, target_list: list) -> list:
    """
    Function to use only threads equal to the numbers of cores of the machine to divide the target list
    """
    try:

        if not search_list or not target_list:
            return []
        num_cores = multiprocessing.cpu_count()  # set the number of cores to use
        sublist_size = math.ceil(len(target_list) / num_cores)  # calculate the size of each sublist
        sublist = [target_list[i:i + sublist_size] for i in range(0, len(target_list), sublist_size)]
        threads = []  # create a list to hold the threads
        results = []
        for sublist in sublist:
            thread = threading.Thread(target=advanced_search, args=(search_list, sublist, results))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

        return results

    except Exception as e:
        print(e)
        raise ValueError(e)


def test_advanced_search_threads():
    # Unit test empty list
    assert advanced_search_threads([], []) == []

    # Unit test 2 list
    assert advanced_search_threads([2, 5, 6], [2, 4, 6, 8]) == [True, False, True, False]


test_advanced_search_threads()
