#!/usr/bin/env python3
"""finds schools by topic"""


from typing import Iterable, Dict, Any


def schools_by_topic(mongo_collection, topic: str):
    """returns schools where topics array contains a specific topic"""
    return mongo_collection.find({"topics": topic})
