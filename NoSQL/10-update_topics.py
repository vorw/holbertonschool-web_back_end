#!/usr/bin/env python3
"""update the topics of a school document by name"""


from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """replaces topics with given name"""
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}},
            )
