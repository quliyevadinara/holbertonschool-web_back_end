#!/usr/bin/env python3
"""Module that returns the list of schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools having a specific topic.

    Args:
        mongo_collection: a pymongo collection object
        topic (str): the topic searched

    Returns:
        A list of schools that have the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))