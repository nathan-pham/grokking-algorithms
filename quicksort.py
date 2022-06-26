from __future__ import annotations
from typing import *

def quicksort(elements: List[int]) -> List[int]:
    if len(elements) <= 1: return elements

    pivot = elements[0]
    left = [el for el in elements[1:] if el <= pivot]
    right = [el for el in elements[1:] if el > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

def main() -> None:
    print(quicksort([3, 5, 2, 1, 4]))

if __name__ == "__main__":
    main()