#!/usr/bin/env python3
"""
auth.py
Auth module
"""
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User

import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hash a password with salt.
    """
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """
    Generate a random UUID.
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with an email and password.
        """
        try:
            existing_user = self._db.find_user_by(email=email)
        except NoResultFound:
            pass
        else:
            raise ValueError(f"User {email} already exists")

        hashed_password = _hash_password(password)

        self._db.add_user(
            email=email,
            hashed_password=hashed_password,
        )

    def valid_login(self, email: str, password: str) -> bool:
        """
        Check user credentials.
        """
        try:
            db_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        password_bytes = password.encode('utf-8')

        return bcrypt.checkpw(password_bytes, db_user.hashed_password)

    def create_session(self, email: str) -> str:
        """
        Create and store a session ID for a user.
        """
        try:
            db_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return "None"

        session_id = _generate_uuid()

        self._db.update_user(
            user_id=db_user.id,
            session_id=session_id
        )

        return session_id
