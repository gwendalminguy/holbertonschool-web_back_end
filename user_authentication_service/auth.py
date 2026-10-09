#!/usr/bin/env python3
"""
auth.py
Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hash a password with salt.
    """
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password.encode('utf-8'), salt)
