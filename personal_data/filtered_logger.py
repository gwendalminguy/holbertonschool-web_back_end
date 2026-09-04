#!/usr/bin/env python3
"""
filtered_logger.py
Module containing the function filter_datum.
"""
import re


def filter_datum(
    fields: list[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscate every value in 'message' matching 'fields' keys with 'redaction'.
    """
    p = r"=.*?(?=" + re.escape(separator) + r")"

    for item in fields:
        message = re.sub(re.escape(item) + p, f"{item}={redaction}", message)

    return message
