## Quickstart ##

It's project generated using [my cookiecutter](https://github.com/dimka2014/cookiecutter-django-rest).\
First create and activate your virtualenv, you can use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
cd to your project and install the dependencies

    pip install -r requirements/development.txt

You should configure project using environment variables. I prefer to do it using `.env` file
There are plugins or utilities which fill your environment from `.env` file:
- [Env File for PyCharm](https://plugins.jetbrains.com/plugin/7861-env-file)
- [autoenv for command line](https://github.com/kennethreitz/autoenv)

The example configuration is in env.example file

To start project you need to run migrations and command which save OWM locations to database 


    python manage.py migrate
    python manage.py save_locations_to_database

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver

## How to use it ##

### Settings ###

Settings are divided by environments: production.py, development.py, test.py.
By default it uses development.py, if you want to change the environment set a environment variable:

    export DJANGO_SETTINGS_MODULE="config.settings.production"

or you can use the `settings` param with runserver:

    python manage.py runserver --settings=config.settings.production


