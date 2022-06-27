from __future__ import annotations
from typing import *

from collections import deque

def breadth_first_search(graph: Dict[any], name: str) -> Union[None, str]:
    """Implementation of Breadth-First Search, a search algorithm for graphs. Checks if someone in nodes sells mangos. 

    Args:
        graph (Dict[any]): Graph
        name (str): Node to start from

    Returns:
        Union[None, str]: Name of mango seller
    """

    search_queue = deque()
    search_queue += graph.get(name, [])

    searched = []

    is_seller = lambda person : person.endswith("m")

    while search_queue:
        person = search_queue.popleft()
        if person not in searched and is_seller(person):
            return person
        
        search_queue += graph.get(person, [])
        searched.append(person)

    return None

def main() -> None:
    graph = {
        "you": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"]
    }

    mango_seller = breadth_first_search(graph, "you")
    print(f"{mango_seller} is a mango seller!")

if __name__ == "__main__":
    main()