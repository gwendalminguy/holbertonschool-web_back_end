## Basic Authentication

This project is about working on a simple HTTP API for playing with `User` model.

### Files

* [`models/base.py`](), base of all models of the API (handle serialization to file).
* [`models/user.py`](), the user model.
* [`api/v1/app.py`](), the entry point of the API.
* [`api/v1/views/index.py`](), basic endpoints of the API (`/status` and `/stats`).
* [`api/v1/views/users.py`](), all users endpoints.

### Installation

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

### Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
