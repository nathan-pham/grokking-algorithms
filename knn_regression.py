from __future__ import annotations
from typing import * 

def read_csv(filename: str) -> Tuple[List[str], List[List[Any]]]:
    """read a csv and parse data into integers

    Args:
        filename (str): file you want to read from

    Returns:
        Tuple[List[str], List[any]]: headings, data
    """

    with open(filename) as file:
        lines = file.read().split('\n')
        headings, *data = [line.split(',') for line in lines]

        return headings, data

def distance(a: List[int], b: List[int]) -> float:
    """determine the distance between two vectors

    Args:
        a (List[int]): A list representing a vector, must be the same length as b
        b (List[int]): A list representing a vector, must be the same length as a

    Raises:
        ValueError: if the length of a is not equal to b

    Returns:
        float: distance between vectors (or similarity between points)
    """

    if len(a) != len(b):
        raise ValueError("length of vectors must be equal")

    # distance formula
    return sum([(a[i] - b[i]) ** 2 for i in range(len(a))]) ** 0.5


def knn_regression(data: List[List[int]], input: List[int], k: int = 4) -> float:
    """Applying KNN to a simple bakery dataset

    Args:
        data (List[List[int]]): Parsed data
        input (List[int]): A row data you want to make a prediction on
        k (int, optional): Amount of neighbors taken into consideration. Defaults to 4.

    Returns:
        float: predicted output
    """

    targets = [row[-1] for row in data]
    distances = [distance(row[:-1], input) for row in data]

    neighbors = []

    # find closest neighbor k times
    while k > 0:
        idx = distances.index(min(distances))
        neighbors.append(targets[idx])

        # remove min from targets & distances
        distances.pop(idx)
        targets.pop(idx)

        k -= 1

    return sum(neighbors) / len(neighbors)

_, data = read_csv("datasets/bakery.csv")
data_int = [list(int(cell) for cell in line) for line in data]

print(knn_regression(data_int, [4, 1, 0]))