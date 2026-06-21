#!/usr/bin/env python3
"""Module that lists all documents in a collection"""


def list_all(mongo_collection):
    """List all documents in a collection.

    Args:
        mongo_collection: a pymongo collection object

    Returns:
        A list of all documents in the collection, or an empty list
        if there are none.
    """
    return list(mongo_collection.find())