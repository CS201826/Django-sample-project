# django-sample-project

django-sample-project is a **minimal** sample application to start developing your web project immediately on [Django framework](https://www.djangoproject.com/). 

##Compatability

This project is compatible with Python 3

The sample project comes with:

* [Twitter Bootstrap](http://getbootstrap.com/)

Its current `requirements.txt` file is:

```
Django==1.11.9
django-debug-toolbar==1.9.1
mysqlclient==1.3.10
pytz==2017.3
sqlparse==0.2.4
```

## Installation

### 1. Create a virtual environment not required, but nice to have

$ virtualenv projectname

You should already know what is [virtualenv](http://www.virtualenv.org/)

Activate it using below commands

For Windows - $ source ./projectname/Scripts/activate

For Ubuntu - $ source ./projectname/bin/activate

You should see `(projectname) $` at your prompt

$ deactivate

to stop using virtualenv.

### 2. Download

Now, you need to create *sampleproject* folder in your workspace:

    $ cd /path/to/your/workspace/sampleproject
    $ git clone https://github.com/CS201826/Django-sample-project.git sampleproject && cd sampleproject

### 3. Requirements
Find the *requirements.txt* file in sampleproject folder. To install them, simply type:

`$ pip install -r requirements.txt`

#### SECRET_KEY

Create your secret key, copy it using http://www.miniwebtool.com/django-secret-key-generator/

Open your `sampleproject/settings.py`, find `SECRET_KEY` line, paste your secret key.

#### Configure the database
First set the database engine (PostgreSQL, MySQL, etc..) in your `sampleproject/settings.py` file

Install necessary database driver for your engine. Then define below credentials as well

'ENGINE': 'django.db.backends.mysql' #database engine

'NAME': 'databasename' #database name

'USER': 'root' #database user name

'PASSWORD': '' #database password

'HOST': 'localhost'

`./manage.py migrate`

### 4. Run the application

Type below command in `sampleproject` folder

`./manage.py runserver`

Open the browser for 

127.0.0.1:8000

127.0.0.1:8000/categories

127.0.0.1:8000/product

