from __future__ import annotations
from typing import *

def min_idx(elements: List[int]) -> int:
    """Find the index of the smallest element in the array

    Args:
        elements (List[int]): List of elements to process

    Returns:
        int: Index of smallest element
    """

    smallest = elements[0]
    smallest_idx = 0

    for i in range(len(elements)):
        if elements[i] < smallest:
            smallest = elements[i] 
            smallest_idx = i

    return smallest_idx

def selection_sort(elements: List[int]) -> List[int]:
    """Sort a list of elements

    Args:
        elements (List[int]): List of elements to sort

    Returns:
        List[int]: List of sorted elements
    """

    elements = elements.copy() # prevent modifications to original array
    sorted = []

    for _ in range(len(elements)):
        sorted.append(elements.pop(min_idx(elements)))

    return sorted

def main() -> None:
    print(selection_sort([34, 23, 10, 57, 42, 89]))

if __name__ == "__main__":
    main()