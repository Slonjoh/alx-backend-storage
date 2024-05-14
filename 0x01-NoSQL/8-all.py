#!/usr/bin/env python3
"""
List All Documents in Collection
This script defines a function to list all documents in a MongoDB collection.
"""
def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        list: A list containing all documents in the collection.
    """
    return [each for each in mongo_collection.find()]
