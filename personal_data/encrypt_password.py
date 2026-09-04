#!/usr/bin/env python3
"""
encrypt_password.py
Module containing the function filter_datum.
"""
from typing import ByteString

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash and salt a password.

    Parameters:
    - password: string to hash

    Return: the hashed password
    """
    encoded_password = password.encode(encoding="utf-8")

    salt = bcrypt.gensalt()

    return bcrypt.hashpw(encoded_password, salt)
