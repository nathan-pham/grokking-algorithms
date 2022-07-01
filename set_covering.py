from __future__ import annotations
from typing import *

States = Set[str]

def set_covering(states: States, stations: Dict[str, States]) -> Set[str]:
    final_stations = set()
    
    while states:
        states_covered = set()
        best_station = None
        for station, station_states, in stations.items():
            covered = states & station_states

            if len(covered) > len(states_covered):
                states_covered = covered
                best_station = station

        states -= states_covered
        final_stations.add(best_station)

    return final_stations

if __name__ == "__main__":
    states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    stations = {
        "kone": set(["id", "nv", "ut"]),
        "ktwo": set(["wa", "id", "mt"]),
        "kthree": set(["or", "nv", "ca"]),
        "kfour": set(["nv", "ut"]),
        "kfive": set(["ca", "az"])
    }

    print(set_covering(states, stations))