from __future__ import annotations
from typing import *

from math import floor

def simple_search(elements: List[int], target: int) -> Union[None, int]:
    for i in range(len(elements)):
        if target == elements[i]:
            return i

    return None

def binary_search(elements: List[int], target: int) -> Union[None, int]:
    low = 0
    high = len(elements) - 1

    while low <= high:
        i = floor((low + high) / 2)
        guess = elements[i]

        if guess > target:
            high = i - 1
        elif guess < target:
            low = i + 1
        else:
            return i
        
    return None

def main() -> None:
    elements = [1, 20, 40, 60, 80]
    print(simple_search(elements, 60))
    print(binary_search(elements, 60))

if __name__ == "__main__":
    main()