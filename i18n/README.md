## i18n

This project is about learning to parametrize translation with **i18n**.

### Files

* [*-app.py](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/i18n/0-app.py), the entry point of the API.
* [babel.cfg](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/i18n/babel.cfg), the Babel configuration file.
* [templates/](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/i18n/templates/), the templates directory.
* [translations/](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/i18n/translations/), the translations directory.
* [requirements.txt](https://github.com/gwendalminguy/holbertonschool-web_back_end/tree/main/i18n/requirements.txt), the requirements file.

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
$ python3 app.py
```

### API

- **Routes**:
    - `GET /`: returns the index HTML template

- **Query Parameters**:
    - `locale`: specify a locale (*en*, *fr*)
    - `timezone`: specify a timezone (*Europe/Paris*, ...)
    - `login_as`: simulate a user (*1*, *2*, *3*, *4*)
