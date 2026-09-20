#!/usr/bin/env python3
"""
SessionExpAuth Module
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from flask import request
from models.user import User
from typing import List, TypeVar

import base64
import hashlib
import os
import uuid


class SessionExpAuth(SessionAuth):
    """
    SessionAuth Class
    """

    def __init__(self):
        """
        Initialize a SessionExpAuth instance.
        """
        SESSION_DURATION = os.getenv("SESSION_DURATION")

        try:
            SESSION_DURATION = int(SESSION_DURATION)
        except ValueError:
            SESSION_DURATION = 0

        self.session_duration = SESSION_DURATION

    def create_session(self, user_id=None) -> str:
        """
        ...
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now(),
        }

        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        ...
        """
        if (session_id is None
                or session_id not in self.user_id_by_session_id.keys()):
            return None

        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id].get("user_id")

        if "created_at" not in self.user_id_by_session_id[session_id].keys():
            return None

        created_at = self.user_id_by_session_id[session_id].get("created_at")
        delta = timedelta(seconds=self.session_duration)

        if created_at + delta < datetime.now():
            return None

        return self.user_id_by_session_id[session_id].get("user_id")
