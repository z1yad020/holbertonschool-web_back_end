#!/usr/bin/env python3

"""
update doc
"""


def update_topics(mongo_collection, name, topics):
    """update doc"""
    mongo_collection.update_many({'name': name}, {'topics': topics})
