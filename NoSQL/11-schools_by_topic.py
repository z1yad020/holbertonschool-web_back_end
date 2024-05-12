#!/usr/bin/env python3

"""
update specific topic on doc
"""


def schools_by_topic(mongo_collection, topic):
    """update doc"""
    return mongo_collection.find({'topics': topic})
