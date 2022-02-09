from typing import Optional, List


# binary search algorithm
def binary_search(array: List[int], element: int) -> Optional[int]:
    # define a "field of view" where we want to search
    low = 0
    high = len(array) - 1

    while low <= high:
        # guess the midpoint
        i = (low + high) // 2
        guess = array[i]

        # guessed to low!
        if guess < element:
            low = i + 1

        # guessed to high!
        elif guess > element:
            high = i - 1

        # guessed just right!
        else:
            return i

    # element could not be found
    return None
    

if __name__ == "__main__":
    array = list(range(1, 10001))
    i = binary_search(array, 768)
    print(f"found: {array[i]}" if i else "could not find element")