#!/usr/bin/env python3

"""
list all docs
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """listing all docs"""
    return mongo_collection.find()
