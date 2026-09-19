#!/usr/bin/env python3
"""
Auth Module
"""
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import List, TypeVar

import base64
import hashlib
import uuid


class SessionAuth(Auth):
    """
    SessionAuth Class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session ID and store it.
        """
        if (user_id is None
                or not isinstance(user_id, str)):
            return None

        session_id = uuid.uuid4()

        self.user_id_by_session_id[session_id] = user_id

        return session_id
        
