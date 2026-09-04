#!/usr/bin/env python3
"""
filtered_logger.py
Module containing the function filter_datum.
"""
from typing import List

import re


def filter_datum(
    fields: list[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscate data using a given redation.

    Parameters:
    - fields: list of keys whose values must be obfuscated
    - redaction: string to use for obfuscation
    - message: concatenated string of key-value pairs with a separator
    - separator: string indicating the delimiter used

    Return: result as a concatenated string obfuscated
    """
    p = r"=.*?(?=" + re.escape(separator) + r")"

    for item in fields:
        message = re.sub(re.escape(item) + p, f"{item}={redaction}", message)

    return message
