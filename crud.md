# Introduction

I’ve been meaning to write a series on Django which is a web application framework written in python. To follow this tutorial you don’t need to be a pro in python and have to know it inside-out. Just some basics will get you through it.

Before we start writing applications, we must know a little about what is Django. Django is a web application framework that acts more of an MTV pattern instead of MVC. Think it this way:

 - Model remains model
 - View has been replaced by Templates
 - Controller gets replaced by View

A simple Hello-world application is just a few lines of code in Django! But moving from this simple thing a full fledged application can be a daunting task in itself. There are other concepts that can help proceed further such as ORM, migrations etc that help in building a bigger application. But for this tutorial we’ll be building a simple CRUD( Create, Retrieve, Update and Delete ) application.

To get started with you need to have python and virtualenv installed on your machine. Python is already installed on the linux systems. But you'll need to install virtualenv. To install virtualenv follow the command:

<script src="https://gist.github.com/nitinprakash96/d7f055698a12cf061e07d7bc0e5417a2.js"></script>

The first line will install a package called python-pip which is a very important utility as far as python based developments are concerned. The second instruction installs virtualenv. For those of you who don't know virtualenv, virtualenv is a tool for creating isolated Python environments containing their own copy of python , pip , and their own place to keep libraries installed from PyPI.

##  Application structure

Before we actually start writing code we need to get a hold of the application structure. We'll first execute several commands that are essential in django project development.

After installing virtualenv, we need to set the environment up.

<script src="https://gist.github.com/nitinprakash96/a3e392b0e615184ab2120a43fc4e0325.js"></script>

We are setting a virtual environment of the name venv here. Now we need to activate it.

<script src="https://gist.github.com/nitinprakash96/1604599745e3a33dc2370373fe8661a4.js"></script>

Now that it has been activated. We need to start our project. Feed in the following command to start a project.

<script src="https://gist.github.com/nitinprakash96/a05a104c87abc6db0694ca5028ca714a.js"></script>

The first line installs Django v1.11.8 and creates a directory named app in the parent directory. the third line starts a project named crudapp in the app directory.
The directory tree should look like

<script src="https://gist.github.com/nitinprakash96/2fe9f9cb7fcfdc4a6753658a5c8370fc.js"></script>

We'll see the meaning of each file and what it does one by one. But first, to test if you are going in the right directoion, run the following command.

<script src="https://gist.github.com/nitinprakash96/fb0ab15880bcf8e74f8572c842e4112e.js"></script>

If you get an output like below then you're doing it right.

![alt](/crud1.png)

Let's see what exactly the different files that we created mean.
- `__init__.py` : Acts as an entry point for your python project.

- `settings.py` : Describes the configuration of your Django installation and lets Django know which settings are available.

- `urls.py` : used to route and map URLs to their `views`.

- `wsgi.py` : contains the configuration for the Web Server Gateway Interface. The Web Server Gateway Interface (WSGI) is the Python platform standard for the deployment of web servers and applications.

## Writing the Application

Now this is where we start coding our app. For this operation we'll consider blog post as our entity. We'll be applying CRUD operations to blog posts.

The app in our project will be called blog_posts.

<script src="https://gist.github.com/nitinprakash96/2543f2059668aa48d4976e9a7b6b84d9.js"></script>

This will create the necessary files that we require.

First and foremost create the Model of our application.

<script src="https://gist.github.com/nitinprakash96/c56935f68d152b238584fcac0326dbbb.js"></script>


Now that we have our model ready, we'll need to migrate it to the database.

<script src="https://gist.github.com/nitinprakash96/de315804d7900dddf43a0da3c109ef9c.js"></script>

Now we create our Views where we define each of our CRUD definition.

<script src="https://gist.github.com/nitinprakash96/4f76e37389ca665acc13a25640330986.js"></script>

Now that we have our Views, we create mappings to URL in our `/crudapp/blog_posts/urls.py` file. Make a note that the following is our app specific mappings.

<script src="https://gist.github.com/nitinprakash96/99a10f9e04427c20dd89dc20f861b915.js"></script>

Now we create project specific mappings in `/crudapp/crudapp/urls.py`.

<script src="https://gist.github.com/nitinprakash96/e7c8d05800909c27f19c88480c7bdc88.js"></script>

 Now almost everything is done and all we need to do is create our templates to test the operations.

 Go ahead and create a `templates/blog_posts` directory in `crudapp/blog_posts/`.

- `templates/blog_posts/post_list.html`:

<script src="https://gist.github.com/nitinprakash96/b12e2e60f96cafa0f906810c1c55a153.js"></script>

- `templates/blog_posts/post_form.html`

<script src="https://gist.github.com/nitinprakash96/44d15bdfde8a3166d63daa00b9f06b61.js"></script>

- `templates/blog_posts/post_delete.html`

<script src="https://gist.github.com/nitinprakash96/19e30a53ecb699b2ada45f7b6203980a.js"></script>

Now we have all the necessary files and code that we require.

The final project tree should look like following:

<script src="https://gist.github.com/nitinprakash96/15f589def4f5128916e19d4973bd7922.js"></script>

Execute `python manage.py runserver` and voila!! You have your Django app ready.
