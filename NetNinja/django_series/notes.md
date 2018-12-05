## What is Django?

Python web app framework. Helps with user auth, templating, routing... It provides a good ORM to deal with database queries.

Allows to easily creates dynamic web apps with Python.

## Install Django and prepare the project

`pip install django`, then create and go to the project's directory.

`django-admin startproject <PROJECT_NAME>`

## URLs

As ususal, browser makes a request, `urls.py` looks at it and fires the adequate function in `views.py`, which sends the response through `HttpResponse`.
