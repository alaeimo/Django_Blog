
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

## Deploying the project to heroku

First, clone the repository to your local machine:

```bash
git clone https://github.com/alaeimono/django_blog.git
```

The "heroku create" CLI command creates a new empty application on Heroku, along with an associated empty Git repository. If you run this command from your app’s root directory, the empty Heroku Git repository is automatically set as a remote for your local repository.

```bash
heroku create <herokuappname>
```
You can use the git remote command to confirm that a remote named heroku has been set for your app:

```bash
git remote -v
```
### For an existing Heroku app

If you have already created your Heroku app, you can easily add a remote to your local repository with the heroku git:remote command. All you need is your Heroku app’s name:

```bash
heroku git:remote -a <herokuappname>
```
### Deploying code
To deploy your app to Heroku, you typically use the git push command to push the code from your local repository’s master or main branch to your heroku remote, like so:

```bash
git push heroku main
```
### Set Enviroment Varibles 
Go to the yourherokuapp dashboard/settings> Config Vars

then add these variables :
```bash
DISABLE_COLLECTSTATIC=1
EMAIL_USER = <YOUR_EMAIL_USER>
EMAIL_PASS = <YOUR_EMAIL_PASS>
SECRET_KEY = <YOUR_SECRET_KEY>
```

### PostgreSQL Database on heroku 
Create the database and run the development server:

```bash
cd django_school
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```