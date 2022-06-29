from __future__ import annotations
from typing import *

infinity = float("inf")

Graph = Dict[str, Any]
GraphCost = Dict[str, float]
GraphParents = Dict[str, Union[str, None]]

def dijkstras_algorithm(graph: Graph, start: str = "A") -> Tuple[GraphCost, GraphParents]:
    unvisited = list(graph.keys())
    visited = [start]

    # shortest distance from A
    costs: GraphCost = dict(zip(unvisited, [infinity] * len(unvisited)))
    costs[start] = 0

    parents: GraphParents = { start: None }

    def find_node():
        lowest_cost = infinity
        lowest_node = None

        for (node, cost) in costs.items():
            if cost < lowest_cost and node not in visited:
                lowest_cost = cost
                lowest_node = node

        return lowest_node

    current_node = start
    while current_node:
        neighbors = graph.get(current_node, {})
        cost = costs[current_node]

        for neighbor, distance in neighbors.items():
            new_cost = cost + distance
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = current_node

            if neighbor not in visited:
                current_node = neighbor

        visited.append(current_node)
        current_node = find_node()

    return costs, parents

def get_path(costs: GraphCost, parents: GraphParents, start: str) -> Tuple[str, List[str]]:
    # get closest node (without A, which has a distance of 0)
    closest_node = min({ key: value for key, value in costs.items() if key != start })

    # find path from parents dict
    child: Union[None, str] = closest_node
    path = []
    
    while child:
        path.append(child)
        child = parents.get(child)

    return closest_node, path

if __name__ == "__main__":
    graph = {
        "A": {
            "B": 4,
            "C": 2
        },
        "B": {
            "C": 1,
            "D": 2,
            "E": 3,
        },
        "C": {
            "B": 1,
            "D": 4,
            "E": 5
        },
        "E": {
            "D": 1
        },
        "D": {},
    }

    start = "A"
    costs, parents = dijkstras_algorithm(graph, start)
    closest_node, path = get_path(costs, parents, start)
    
    print(f"closest_node = {closest_node}")
    print(f"path = {', '.join(path)}")