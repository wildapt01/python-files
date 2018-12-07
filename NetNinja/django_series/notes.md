## What is Django?

Python web app framework. Helps with user auth, templating, routing... It provides a good ORM to deal with database queries.

Allows to easily creates dynamic web apps with Python.

## Install Django and prepare the project

`pip install django`, then create and go to the project's directory.

`django-admin startproject <PROJECT_NAME>`

####The general structure of a Django project is made of apps which each have their own urls.py, views.py and templates folder. Each app controls a portion of the project.

## URLs

As usual, browser makes a request, `urls.py` looks at it and fires the adequate function in `views.py`, which sends the response through `HttpResponse` or `render(request, 'my-page.html'`. The `render()` is imported from `django.shortcuts`.

The HTML templates are in the templates folder, and pointed to via the `settings.py` file.

## Apps

Django works in a modular way with apps. Each app takes charge of and controls a part of the project. Add an app with `python manage.py startapp <APP_NAME>` in the console opened in the main project folder. The first child folder in the project folder, which has the same name, is already a django app and serves also as the central hub for the different apps composing the project.

To be validly invoked, each app needs to be registered in INSTALLED APP object in `<PROJECT_NAME>/<PROJECT_NAME>/settings.py`. The main app file `url.py` gets a new line as include points to the new app `urls.py` file.

## Models and django's ORM

In the new app articles, the `models.py` files holds the models(s) for this app. Each one is a class representing a DB table, each property of that class is a field. As with Sequelize, the properties describe the field content and can have options. Check Doc for field list. They are all properties of the `models` module in `django.db`.
