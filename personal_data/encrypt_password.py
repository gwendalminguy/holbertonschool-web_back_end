#!/usr/bin/env python3
"""
encrypt_password.py
Module containing the function filter_datum.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash and salt a password.

    Parameters:
    - password: string to hash

    Return: the hashed password
    """
    encoded_password = password.encode(encoding="UTF-8")

    salt = bcrypt.gensalt()

    return bcrypt.hashpw(encoded_password, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a password matches a hash or not.

    Parameters:
    - hashed_password: ...
    - password: ...

    Return: whether the password is valid or not
    """
    encoded_password = password.encode(encoding="UTF-8")

    return bcrypt.checkpw(encoded_password, hashed_password)
