#!/usr/bin/env python3

"""
insert doc
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserting new doc"""
    return mongo_collection.insert_one(kwargs).inserted_id
