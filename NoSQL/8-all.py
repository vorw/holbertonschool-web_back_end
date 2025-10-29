#!/usr/bin/env python3
from pymongo import MongoClient
def list_all(mongo_collection):
    """list all docs in a collection"""
    return list(mongo_collection.find())
