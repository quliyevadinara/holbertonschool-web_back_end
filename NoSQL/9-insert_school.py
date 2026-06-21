#!/usr/bin/env python3
"""Module that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection based on kwargs.

    Args:
        mongo_collection: a pymongo collection object
        **kwargs: the fields and values of the document to insert

    Returns:
        The new _id of the inserted document.
    """
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id