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

def main() -> None:
    print(factorial(5))

if __name__ == "__main__":
    main()