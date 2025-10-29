#!/usr/bin/env python3
"""list all docs in a collection."""


from typing import List, Dict, Any


def list_all(mongo_collection):
    """list all docs in a collection"""
    return list(mongo_collection.find())
