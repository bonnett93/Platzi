# Django_Basic_platzi_awards

In this directory I'm work on basics of Django making the Platzi Awards project
For more details see the Django oficial [tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)

### Django:
* Framework(Rules and code set make by third parts) to create web apps.
* Very popular: Instagram, Pinterest, NatGeo app, Platzi.
* Free and opensource

### Create venv and Instal Django:
* create vitural env and initialize it:

      sudo apt-get update

      supdo apt-get install python3.8-venv

      python3 -m venv venv

      source venv/bin/activate

* In the venv instal django

      (venv) pip install django

### Create new Django project with name platzi_awards:
    (venv) django-admin startproject platzi_awards_app

	A Django project is an application set, for example the project Instagram has some applications inside:
	* Insragram project:
		* Feed aplication
		* histories aplication
		* Reels aplicaion
		*...

	For this project for example we have the aplication pools, and this let us use as a portable module and use in another page like the oficial platzi page and make the pool there.

###### django-admin (startproject vs startapp):
  The startproject will create the main project directory, while the startapp will create the app directory. Both are also been passed a name to be used in generation. The startproject is the first command run when creating a new project, while the startapp is run inside the new project directory

#### Django created files:
* **platzi_awards directory root**: Is a container for the project and necesary files to make the project works. Django has no more link with this, you can rename it as you like.

  * **manage.py**: Command-lin utility that let you interact with this Django project in various ways. For example validates if django is correctly install, and show us commands available to make the project runs, this file creates a os envioremt variables too.

  * **platzi_awards** inner directory: Django afects it directly, and its the actual Django package of the project. You'll need to use this name to import anything inside it (e.g. mysite.urls).

    * __init__.py: Classic file to indicate a directory is a package

    * settings.py: Settings/configuration of our project. Remeber put DEBUG=False when production.

    * urls.py: The URL declarations for this Django project.

    * asgi.py - wsgi.py: An entry point for (ASGI or WSGI)compatible web server.

	ASGI(Asynchronous Server Gateway Interface) you define your application as a callable which is asynchronous by default and it's a successor of the successful WSGI. WSGI (Web Server Gateway Interface) framework is a standard interface which allows to seperate server code from the application code where you add your business logic. [more info](https://medium.com/analytics-vidhya/difference-between-wsgi-and-asgi-807158ed1d4c)

### Developtment server
We have to servers in our project
* **Developtment server**: The server deploy the project, we don´t work here, just push the changes. Remember pur DEBUG=False in settings.py file in production.
* **Local**: The computer we use to create the project, where we do and modify code.

Django give us the way to simulate production work in local server before push changes, to use it follow:
* In the platzi_awards directory root:

      python manage.py runserver

The ip:port where the project is deploy on 127.0.0.1:8000 (local host) by default

  * If we need change the run server we can specify it in the last of the line:

	    python manage.py runserver 8080

  * And even change ip. For exaple listen in all public IPs 0=0.0.0.0

	    python manage.py runserver 0:8080

###### Terminal deploy message details:

* **Watching for file** : Django automatically implements (if there is no conflict) every change to the project, without pausing and re-executing.
* **System check identified no issues** : No issues and 0 were silent.
* **You have 18 unapplied migration(s)**: You don't create a valid database (We can ignore if we haven't implement OMR or similar).
* **Using settings ‘plati_awards.settings’** : Use the settings.py file, and aply configuration variables.
* **Starting development** : Deployment state and Ip:Port

### Create new App named "polls" inside this project
With the virtual enviroment activate, go to plarzi_awards inner directory and write :
	python3 manage.py startapp polls

now we have new directory named polls:
	* Modify views.py to include a new view named index:
		from django.http import HttpResponse

		def index(request):
			return HttpResponse("Hello world")

	* Create a new file urls.py inside:
		from django.urls import path
		from . import views

		urlpatterns = [
			path("", views.index, name="index")
		]

	* Add the ulrs from polls to platzi_awards inner directory urls file.
		from django.urls import path, include

		urlpatterns = [
			path('admin/', admin.site.urls),
			path("polls/", include("polls.urls"))
		]

	* Write localhost/polls to see the changes in your browser. If there is an error, stop and run the project again.
