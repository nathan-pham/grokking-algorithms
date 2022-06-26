from __future__ import annotations
from typing import *

def factorial(n: int) -> int:
    """Compute the factorial of a number

    Args:
        n (int): Number to perform operation on

    Returns:
        int: Result of n!
    """

    if n == 1: return 1
    return n * factorial(n - 1)

def recursive_sum(*elements: int) -> int:
    elements = list(elements)

    if len(elements) == 0: return 0    
    if len(elements) == 1: return elements[0]
    
    return elements.pop() + recursive_sum(*elements)

def main() -> None:
    print(factorial(5))
    print(recursive_sum(1, 2, 3, 4, 5))

if __name__ == "__main__":
    main()