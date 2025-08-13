#!/usr/bin/env python3
"""
10-update_topics.py
Module containing the function update_topics.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school based on the name.
    """
    document = {'name': name}
    values = {'$set': {'topics': [topic for topic in topics]}}
    mongo_collection.update_many(document, values)
