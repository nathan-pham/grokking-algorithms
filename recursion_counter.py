from __future__ import annotations
from typing import *

def countdown(i: int) -> None:
    # best case
    if i <= 0:
        return

    # recursive case    
    print(i)
    countdown(i - 1)

countdown(10)