#!/usr/bin/env python3
"""insert a school document and return its id"""


from typing import Any


def insert_school(mongo_collection, **kwargs):
    """insert a new document using kwargs and return its id"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
