# Runescape-Hiscores
A Django app for Runescape [Hiscores](http://services.runescape.com/m=hiscore/ranking)

### Live demo
http://hiscores.herokuapp.com/hiscores/overall/

### Requirements
* PostgreSQL 8.4+
* python 2.7
* python virtualenv

### How to setup
* Setup virtualenv

        $ virtualenv . 

* Activate virtual enviornment

        $ source bin/activate

* Install dependencies 
 
        $ pip install django
        $ pip install psycopg2

* Create your Django project

        $ django-admin startproject <projectname>

* CD into your project directory
 
        $ cd <projectname>

* Clone or extract [zip](https://github.com/RaghavPro/Runescape-Hiscores/archive/master.zip) into your project

        $ git clone https://github.com/RaghavPro/Runescape-Hiscores.git
        
* Open ```<projectname> > settings.py```
      In ```INSTALLED_APPS``` add 'hiscores' and 'django.contrib.humanize'

      In ```TEMPLATES``` change ```DIRS``` to ```[os.path.join(BASE_DIR, 'templates')]```
      
      It will look like this 

        'DIRS': [os.path.join(BASE_DIR, 'templates')],

      
      Replace ```DATABASE``` with this
      
        DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '<database>',
            'USER': '<user>',
            'PASSWORD': '<password>',
            'HOST': '',
            'PORT': '5432',
          }
        }
      
* Open ```urls.py``` and in ```urlpatterns``` add

        url(r'^hiscores/', include('hiscores.urls')),

      Go back to previous directory
        
        $ cd ..
      
      

* Now let's create tables for this app

        $ python manage.py migrate hiscores

* Run the development server

        $ python manage.py runserver

* Go to

        http://127.0.0.1:8000/hiscores/overall/

  If you did everything correctly you'll see the template. And I hope you do because it took some time to write these instructions.

### Screenshots
![Player](http://i.imgur.com/oMM4Otd.png)

![Skill](http://i.imgur.com/rCjdBre.png)

![Compare](http://i.imgur.com/ecocrN1.png)
