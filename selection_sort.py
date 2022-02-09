from random import randint
from typing import List
from copy import deepcopy

def get_min_index(array: List[int]) -> int:
    """
    get the smallest value's index in an array
    """

    min_number = array[0]
    min_index = 0

    for i in range(len(array)):
        if array[i] < min_number:
            min_number = array[i]
            min_index = i

    return min_index


def randlist(k: int) -> List[int]:
    """
    create a randomly generated list composed of numbers [0, 100)
    """

    return [randint(0, 100) for i in range(k)]


def selection_sort(array: List[int]) -> List[int]:
    """
    sort a list, O(n) complexity
    """

    array = deepcopy(array)
    sorted_array = []

    for i in range(len(array)):
        sorted_array.append(array.pop(get_min_index(array)))

    return sorted_array


def main() -> None:
    """
    main method: test selection_sort with randomly generated list
    """

    random_list = randlist(10)
    print(random_list)
    print(selection_sort(random_list))


if __name__ == "__main__":
    main()