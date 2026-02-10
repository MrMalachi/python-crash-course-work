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
* **Django Project** - organized as a group of individual _apps_ that work together to make the project work as a whole
* **Model** - a _model_ (class) tells Django how to work with the data that will be stored in the app
* **CharField** - a piece of data that's made up of characters or text, used when you want to store a small amount of
                  text
* **DateTimeField** - a piece of data that will record a date & time
* **`makemigrations`** - a command that tells Django to figure out how to modify the database so it can store the data
                         associated with any new models we've defined
* **admin site** - Django makes it easy to work with your models through its _admin site_. It's only meant to be used by
                   the site's administrators; it's not meant for regular users
* **superuser** - a user who has all privileges available on the site
* **Privileges** - a user's _privileges_ control the actions they can take
* **Many-to-One Relationship** - a type of database relationship where multiple records in one table (many) are related
                                 to a single record in another table (one)
* **Key** - an attribute(s) used to uniquely identify records within a table
* **Foreign Key** - a reference to another record in a database
* **Cascading Delete** - refers to a database foreign key constraint that automatically deletes related rows in a child
                         table when the corresponding row in the parent table is deleted
* **Queryset** - a collection of objects (records) from a database, a core component of the Django ORM 
                 (Object-Relational Model)
* 

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
* `django-admin startproject ll_project .` - tells Django to set up a new project called ll_project. It also creates a 
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

## Starting an App
* Activate the virtual environment, and then run the `startapp` command:
  1. `source ll_env/bin/activate`
  2. `python manage.py startapp learning_logs`
* The command _startapp_ tells Django to create the infrastructure needed tp build an app

### *Defining Models*
* The `models.py` files can be used to define the data we want to manage in our app
* A _model_ is a class; it has attributes and methods
* Here's the model for the topics users will store:
```python
from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
```
* `CharField` is used to store a small amount of text, and it is defined above to store a `max_length` of 200 characters
* `DateTimeField` - used to record a date & time, and is set above to the current date & time whenever the user creates
                    a new topic
* Tell Django how you want it to represent an instance of a model by creating a `__str__()` method
  * If a model has a `__str__()` method, Django calls that method whenever it needs to generate output referring to an 
    instance of that model

### *Activating Models*
* To use personal models, you habe to tell Django to include your app in the overall project

**settings.py**
```python
INSTALLED_APPS = [
    # My apps.
    "learning_logs",

    # Default Django apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
* Next, tell Django to modify the database so it can store information related to the model `Topic`

`(ll_env) malachibrown@Malachis-iMac learning_log % python manage.py makemigrations learning_logs`
```terminaloutput
Migrations for 'learning_logs':
  learning_logs/migrations/0001_initial.py
    + Create model Topic
```

* Apply this migration and have Django modify the database for us:

`(ll_env) malachibrown@Malachis-iMac learning_log % python manage.py migrate`
```terminaloutput
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0001_initial... OK
```
* Whenever you want to modify the data that Learning Log manages, follow three steps:
  1. Modify `models.py`
  2. Call `makemigrations` on `app_name`
  3. Tell Django to `migrate` the project

### *The Django Admin Site*
* Set up the admin site and use it to add some topics through the `Topic` model

#### Set Up a Superuser
* A _superuser_ is the absolute highest-privileged account (root user). A good administrator is careful with their 
  user's sensitive information, because users put a lot of trust into the apps they access
* Enter the following command to create a _superuser_:

`(ll_env) malachibrown@Malachis-iMac learning_log % python manage.py createsuperuser`
```terminaloutput
Username (leave blank to use 'malachibrown'): ll_admin
Email address: brownmnb11@yahoo.com
Password: 
Password (again): 
Superuser created successfully.
```
* Django ensures that each time you enter your password it becomes hashed as an extra layer of security

#### Registering a Model with the Admin Site
* Django includes some models in the admin site automatically, such as `User` and `Group`, but the models created need
  to be added manually by registering them:

```python
from django.contrib import admin

from .models import Topic

# Register your models here.
admin.site.register(Topic)
```
* This code first imports the model you want to register, `Topic`. The dot in from of `models` tell Django to look for
  _models.py_ in the same directory as _admin.py_
* The code `admin.site.register()` tells Django to manage our model through the admin site
* To use the superuser account to access the admin site, go to: http://localhost:8000/admin/
* This page allows you to add new users and groups, and change existing ones. You can also work with data related to the
  `Topic` model that we just defined

### *Defining the Entry Model*
* A _foreign key_ is what connects each entry to a specific topic
* Each topic is assigned a key (unique identifier) within a table when it's created
* (Cascading Delete) When a topic is deleted, all the entries associated with that topic should be deleted as well
```python
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()   # No size limit needed for individual entries.
    # Present entries in order they were created & place a timestamp next to each entry.
    date_added = models.DateTimeField(auto_now_add=True)    
    
    # Nested class with a special attribute telling Django to use `Entries` when needing to refer to more than one entry.
    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."   # Because an entry can be a long body of text, the method returns first 50 char.
```

### *Migrating the Entry Model*
* Migrate (modify) the database again and check the output by entering the following commands:

`(ll_env) malachibrown@Malachis-iMac learning_log % python manage.py makemigrations app_name`
```terminaloutput
Migrations for 'learning_logs':
  learning_logs/migrations/0002_entry.py
    + Create model Entry
```
`(ll_env) malachibrown@Malachis-iMac learning_log % python manage.py migrate`
```terminaloutput
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0002_entry... OK
```
* A new migration called _0002_entry.py_ is generated, which tells Django how to modify the database to store more
  information related to the model `Entry`

### *Registering Entry with the Admin Site*
* Registering the `Entry` model must be done through the admin:
```python
from django.contrib import admin

from .models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
```

### *The Django Shell*
* The Django shells allows you to examine data programmatically through an interactive terminal session:

`(ll_env) malachibrown@Malachis-iMac learning_log % python manage.py shell`
```terminaloutput
14 objects imported automatically (use -v 2 for details).

Python 3.14.2 (main, Dec  5 2025, 16:49:16) [Clang 17.0.0 (clang-1700.6.3.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
```
```shell
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
```
* The command `python manage.py shell`, run in an active virtual environment, launches a Python interpreter that you can
  use to explore the data stored in your project's database
* `from learning_logs.models import Topic` imports the model from the module
* `Topic.objects.all()` utilizes the method to get all instances of the model (class)
  * The list that's returned is a _queryset_
* Do the following to loop over a _queryset_ and see the ID that's been assigned to each topic object:
```shell
>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
... 
1 Chess
2 Rock Climbing
```
* In the previous code, you assigned the _queryset_ to `topics` and then print each topic's `id` attribute and the
  string representation of each topic
* If you know the ID of a particular object, you can use the method `Topic.objects.get()` to retrieve that object and
  examine any attribute the object has:
```shell
>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Topic' object has no attribute 'date'
>>> t.date_added
datetime.datetime(2026, 2, 10, 0, 43, 31, 241715, tzinfo=datetime.timezone.utc)
```
* To get data through a foreign key relationship, you use the lowercase name of the related model (class) followed by an
  underscore and the word `set`:
```shell
>>> t.entry_set.all()
<QuerySet [<Entry: The opening is the first part of the game, roughly...>, <Entry: In the opening phase of the game, it's important t...>]>`\
```
* Each time you modify your models, you'll need to restart the shell to see the effects of those changes (CTRL-D)
