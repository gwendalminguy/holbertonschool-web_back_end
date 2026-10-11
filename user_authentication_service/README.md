## User Authentication Service

This project is about learning to implement a user authentication service.

### Files

* [app.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/user_authentication_service/app.py), the entry point of the API.
* [auth.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/user_authentication_service/auth.py), the Auth module.
* [db.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/user_authentication_service/db.py), the DB module.
* [main.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/user_authentication_service/main.py), a full integration test.
* [user.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/user_authentication_service/user.py), the User model definition.

### Installation

The project can be installed by running the following commands:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Run

To run the application:

```
$ python3 -m app
```

### Routes

- **INDEX**:
    - `GET /`: returns the status of the API

- **USERS**:
    - `GET /profile`: returns the authenticated user's profile
    - `POST /users`: creates a new user (JSON parameters: `email` and `password`)

- **AUTH**:
    - `POST /sessions`: starts an authentication session
    - `DELETE /sessions`: ends an authentication session
    - `POST /reset_password`: generates a reset password token
    - `PUT /reset_password`: updates a password
