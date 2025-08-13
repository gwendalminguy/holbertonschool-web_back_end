#!/usr/bin/env python3
"""
101-students.py
Module containing the function top_students.
"""


def top_students(mongo_collection):
    """
    Finds all students sorted by average score.
    """
    cursor = mongo_collection.find()
    for element in cursor:
        grades = [topic['score'] for topic in element['topics']]
        avg = sum(grades) / len(grades)
        mongo_collection.update_one({'name': element['name']}, {'$set': {'averageScore': avg}})

    cursor = mongo_collection.find().sort('averageScore', -1)
    return cursor