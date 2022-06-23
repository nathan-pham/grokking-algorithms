from __future__ import annotations
from typing import *

# types
Class = Dict[Any, Any]
Classes = List[Class]

classes: Classes = [
    { "name": "art",        "start": "9 am",      "end": "10 am" },
    { "name": "english",    "start": "9:30 am",   "end": "10:30 am" },
    { "name": "math",       "start": "10 am",     "end": "11 am" },
    { "name": "cs",         "start": "10:30 am",  "end": "11:30 am" },
    { "name": "music",      "start": "11 am",     "end": "12 pm" },
]

def parse_time(time: str) -> float:
    """Convert time in string form into decimal format

    Args:
        time (str): A standard digital time (ie: 10:30 am)

    Returns:
        float: time in number form (ie: 10.5)
    """
    
    time, am_pm = time.lower().split(' ')
    hrs, *_mins = [int(unit) for unit in time.split(':')]
    mins = 0 if len(_mins) == 0 else _mins[0]

    if (am_pm == "pm" and hrs != 12) or (am_pm == "am" and hrs == 12):
        hrs += 12

    return hrs + (mins / 60)

def classes_min(classes: Classes, last_time: int) -> Union[None, Class]:
    """Get the class that starts the earliest (while also not overlapping with other classes)

    Args:
        classes (Classes): Classes with parsed times
        last_time (int): Last ending time in schedule

    Returns:
        Union[None, Class]: Minimum class (if found)
    """

    min_class = None

    for c in classes:
        # class must start as early as possible while starting later than the first class
        if c["start"] >= last_time and c["start"] <= (min_class or { "start": 24 })["start"]:
            min_class = c
    
    return min_class

def classroom_scheduling(classes: Classes) -> Classes:
    """Return a list of the maximum number of classes that can be taken without overlap

    Args:
        classes (Classes): full list of available classes

    Returns:
        Classes: compiled schedule
    """

    classes_parsed: Classes = [
        {
            "name": c["name"], 
            "start": parse_time(c["start"]), 
            "end": parse_time(c["end"])
        } for c in classes
    ]

    schedule = []
    last_time = 0

    for _ in range(len(classes)):
        min_class = classes_min(classes_parsed, last_time)
        if min_class is None: break

        schedule.append(min_class)
        last_time = min_class["end"]

    return schedule

print(classroom_scheduling(classes))
