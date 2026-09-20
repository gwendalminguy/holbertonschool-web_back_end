## Session Authentication

This project is about working on a simple HTTP API by improving an authentication system with a session mechanism, persistance, expiration, and with dedicated `login` and `logout` endpoints.

### Files

* [`models/base.py`](models/base.py), the base for all models.
* [`models/user.py`](models/user.py), the User model.
* [`models/user_session.py`](models/user_session.py), the UserSession model.
* [`api/v1/app.py`](api/v1/app.py), the entry point of the API.
* [`api/v1/auth/auth.py`](api/v1/auth/auth.py), the Auth module.
* [`api/v1/auth/basic_auth.py`](api/v1/auth/basic_auth.py), the BasicAuth module.
* [`api/v1/auth/session_auth.py`](api/v1/auth/session_auth.py), the SessionAuth module.
* [`api/v1/auth/session_db_auth.py`](api/v1/auth/session_db_auth.py), the SessionDBAuth module.
* [`api/v1/auth/session_exp_auth.py`](api/v1/auth/session_exp_auth.py), the SessionExpAuth module.
* [`api/v1/views/index.py`](api/v1/views/index.py), the basic endpoints (`/status` and `/stats`).
* [`api/v1/views/users.py`](api/v1/views/users.py), all users endpoints.
* [`api/v1/views/session_auth.py`](api/v1/views/users.py), all authentication endpoints.

### Installation

The project can be installed by running the following commands:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Run

To run the application with an authentication session duration of one hour persisted in a database file:

```
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_db_auth SESSION_NAME=session SESSION_DURATION=3600 python3 -m api.v1.app
```

### Routes

- **INDEX**:
    - `GET /api/v1/status`: returns the status of the API
    - `GET /api/v1/stats`: returns some stats of the API

- **USERS**:
    - `GET /api/v1/users`: returns the list of all users
    - `GET /api/v1/users/:id`: returns a user based on the ID
    - `GET /api/v1/users/me`: returns the current user
    - `DELETE /api/v1/users/:id`: deletes a user based on the ID
    - `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
    - `PUT /api/v1/users/:id`: updates a user based on the ID (JSON parameters: `last_name` and `first_name`)

- **AUTH**:
    - `POST /api/v1/auth_session/login`: starts an authentication session.
    - `DELETE /api/v1/auth_session/logout`: ends an authentication session.
