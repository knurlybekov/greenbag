# greenbag

A Django social-network web app with a custom user model, user profiles, posts, and follow/subscription relationships.

## Overview

greenbag is a server-rendered Django social platform. Users sign up with email, build a profile, create posts, and subscribe to other users. Authentication is handled with a custom `AbstractBaseUser` model and django-allauth.

## Features

- Custom email-based `User` model (`AbstractBaseUser` + `PermissionsMixin`)
- Sign-up, login, profile editing
- Create and view posts
- `UserSubscription` model for follower/following relationships
- django-allauth integration (account + social account scaffolding)
- Server-rendered templates (Bootstrap-style)

## Tech Stack

Python · Django 5 · django-allauth · SQLite (dev)

## Running Locally

```bash
pip install django django-allauth
python manage.py migrate
python manage.py runserver
```

## Project Structure

```
djangoProject/    # settings, root URLs, WSGI/ASGI
greenbag/         # app: views.py, forms.py, models.py, admin.py, templates/
```
