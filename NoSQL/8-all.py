#!/usr/bin/env python3
def list_all(mongo_collection):
    """list all docs in a collection"""
    return list(mongo_collection.find())
