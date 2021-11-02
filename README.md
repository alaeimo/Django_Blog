
# [Django Blog](https://alaeimoblog.herokuapp.com/)

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2-brightgreen.svg)](https://djangoproject.com)
## [demo](https://alaeimoblog.herokuapp.com/)

## Django and Bootstrap are used here to build a simple blog
![Django Blog Screenshot](https://github.com/alaeimono/django_blog/blob/main/media/screenshot.png)

### Features:
    - You can register an account on this blog
    - Update your email, and username
    - If you forget your password, receive an email and recover it
    - Post new post (similar to Twitter)
    - Update your posts
    - Filter and view other users' posts by their usernames

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/alaeimono/django_blog.git
```

Create Virtual Env and Install the requirements:

```bash
cd django_blog
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

Create the database and run the development server:

```bash
cd django_school
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The project will be available at http://127.0.0.1:8000