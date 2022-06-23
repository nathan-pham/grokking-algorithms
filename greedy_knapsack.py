from __future__ import annotations
from typing import *

Item = Dict[str, Any]
Items = List[Item]

items: Items = [
    { "name": "stereo", "value": 3000, "weight": 30 },
    { "name": "laptop", "value": 2000, "weight": 20 },
    { "name": "guitar", "value": 1500, "weight": 15 }
]

def knapsack_min(items: Items, weight_left: int) -> Union[None, Item]:
    """Find the item with the highest value that still fits in the bag

    Args:
        items (Items): List of items
        weight_left (int): Space left in knapsack

    Returns:
        Union[None, Item]: Highest value item (if found)
    """

    max_value = None

    for item in items:
        fill_max_value = max_value or { "value": 0, "weight": 0 }
        if item["weight"] <= weight_left and item["value"] >= fill_max_value["value"]:
            max_value = item

    return max_value        

def knapsack(items: Items, max_weight: int = 35) -> Items:
    """Greedily find the most value items that will fit in the knapsack

    Args:
        items (Items): List of items
        max_weight (int, optional): Amount of weight the knapsack can carry. Defaults to 35.

    Returns:
        Items: List of items that can fit in the knapsack
    """
    
    weight_left = max_weight
    steal = []

    for _ in range(len(items)):
        min_item = knapsack_min(items, weight_left)
        if min_item is None: break

        steal.append(min_item)
        weight_left -= min_item["weight"]

    return steal

print(knapsack(items))