# LAB - Class 33
## Project: Django Auth / Prod Server
#### Author: Faustino Marco Simpliciano

### Links and Resources
- Development server: http://127.0.0.1:8000/
- front-end application: "Carriers"

### Feature Tasks & Requirements 08/23
You have been supplied with two demos, each presenting a key new feature.
One demonstrates how to restrict access to portions of your APIs data.
The other demonstrates switching over to using postgres vs sqlite
Your job is to merge the functionality of both demos.
Customize your project to use different application features/models than what was used in demos.

### Typical Steps to Start Django Project
- create project
  - `django-admin startproject name_name_name .`
    - DON'T FORGET THE `.`
  - `mkdir templates`
    - `touch templates/snack_list.html`
  - `python manage.py runserver`
    - if working, now migrate
  - `python manage.py migrate`
- add app to project
  - `python manage.py startapp name_`
- define app
- update settings for app
  - settings
    - installed apps
      - add `#local`
        - add `app_name`
    - templates
      - DIRS
        - add into [] `BASE_DIR / "templates"`
- handle models
  -> models.py
    - make classes
    - `class N_ame(models.Model):`
      - name = models.CharField(max_length=256)
      - etc.
- handle views
  -> views.py
    - handle imports
    - `from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView`
    - `from .models import Carrier`
    - make classes
    - `class CarrierListView(ListView):`
      - `template_name = "carrier_list.html"`
      - `model = Carrier`
  - go to admin path to login on dev server
  - see admin.py
    - `from .models import Carrier`
    - `admin.site.register(Carrier)`
  - `python manage.py showmigrations`
    - `python manage.py makemigrations name_of_app`
    - repeat show migrations cmd
    - runserver
    - use cmd to apply new migration
- add urlpattern
  - create urls.py in app
    - copy over from urls.py in project dir?
    - from django.urls import path
    - from .views import all your views
    - create list of urlpatterns
      - path()
  - `python manage.py createsuperuser`
    - usrnm
    - email
    - pswd
  - populate admin.py
    - register models
      - `from .models import Carrier`
      - `admin.site.model(Carrier)`
- add tests

### Setup
<!-- .env requirements (where applicable) -->
- requirements.txt
- .gitignore populated using [this](https://www.toptal.com/developers/gitignore/api/python,windows) template.
<!-- 
- PORT - Port Number
- DATABASE_URL - URL to the running Postgres instance/db -->
- How to initialize/run your application (where applicable) e.g. python main.py
  - `python manage.py runserver`
- How to use your library (where applicable)
- Tests
  - How do you run tests?
    - `python manage.py test`
  - Any tests of note?
    - Homepage status code
    - About page status code
    - Homepage use of template
    - About page use of template
  - Describe any tests that you did not complete, skipped, etc
    - N/A
