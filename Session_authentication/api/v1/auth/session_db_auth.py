#!/usr/bin/env python3
"""
SessionDBAuth Module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from flask import request
from models.user import User
from models.user_session import UserSession
from typing import List, TypeVar

import base64
import hashlib
import os
import uuid


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth Class
    """

    def create_session(self, user_id=None):
        """
        Overload method to store the session in DB.
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        db_session = UserSession(
            user_id=user_id,
            session_id=session_id,
        )

        db_session.save()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Overload method to retrieve session from DB.
        """
        if session_id is None:
            return None

        UserSession().load_from_file()

        results = UserSession().search({
            "session_id": session_id,
        })

        if len(results) != 1:
            return None

        user_session = results[0]

        if self.session_duration <= 0:
            return user_session.user_id

        created_at = user_session.created_at
        delta = timedelta(seconds=self.session_duration)

        if created_at + delta < datetime.utcnow():
            return None

        return user_session.user_id

    def destroy_session(self, request=None):
        """
        Delete an existing authentication session from DB.
        """
        session_id = self.session_cookie(request)

        if session_id is None:
            return False

        results = UserSession().search({
            "session_id": session_id,
        })

        if len(results) != 1:
            return False

        user_session = results[0]
        user_session.remove()

        return True
