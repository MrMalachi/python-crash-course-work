# WEB APPLICATIONS PROJECT | CH. 18, 19, 20

## Glossary
* **Specification** - describing the project's goals in order to identify
                      manageable tasks to achieve those goals
* **Virtual Environment** - a place on your system where you can install
                            packages & isolate them from all other Python
                            packages
* **Migrating** - anytime someone modifies a database, we say we're migrating
                  the database
* **Localhost** - refers to a server that only processes requests on your
                  system; it doesn't allow anyone else to see the pages you're
                  developing

## Setting Up a Project
* When starting to work on something as significant as a web app, you first
  need to describe the project's goals in a _specification_, or _spec_

### *Writing a Spec*
* A full _spec_ details the project goals, describes the project's
  functionality, and discusses its appearance and user interfaces
* **Spec:**
  * Write a web app called Learning Log that allows users to log the topics
    they're interested in and make journal entries as they learn about each
    topic. The Learning Log home page will describe the site and invite users
    to either register or log in. Once logged in, a user can create new topics,
    add new entries, and read & edit existing entries.

### *Creating a Virtual Environment*
* `python3 -m venv *name_of_virtual_environment*`

### *Activating the Virtual Environment*
* `source *name_of_virtual_environment*/bin/activate`
* To stop using a virtual environment, enter _deactivate_
  * `deactivate`

### *Installing Django*
* Upgrade  pip - `pip install --upgrade pip`
* Install Django - `pip install django`

### *Creating a Project in Django*
* `django-admin startproject ll_project` - tells Django to set up a new project called ll_project. It also creates a 
  `manage.py` file, which is a short program that takes in commands and feeds them to the relevant part of Django
* `settings.py` file controls how Django interacts with your system and manage
   your project
* `urls.py` file tells Django which pages to build in response to browser
   requests
* `wsgi.py` (web server gateway interface) files helps Django serve the files 
   it creates

### *Creating the Database*
* Create a database that Django can work with:
  * `python3 manage.py migrate`
* Issuing the `migrate` command for the first time tells Django to make sure
  the database matches the current state of the project 

### *Viewing the Project*
* Make sure that Django has set up the project properly:
  * Enter the `python manage.py runserver` command to view the project in its current state
* http://127.0.0.1:8000/ - the URL indicates that the project is listening for
  requests on port 8000 on your computer, which is called a localhost