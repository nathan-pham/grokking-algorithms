from __future__ import annotations
from typing import *

Station = Set[str]
Stations = Dict[str, Station]
StationsList = List[str]

stations: Stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
}

def find_stations(stations: Stations) -> Stations: 
    pass