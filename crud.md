# Introduction

I’ve been meaning to write a series on Django which is a web application framework written in python. To follow this tutorial you don’t need to be a pro in python and have to know it inside-out. Just some basics will get you through it.

Before we start writing applications, we must know a little about what is Django. Django is a web application framework that acts more of an MTV pattern instead of MVC. Think it this way:

 - Model remains model
 - View has been replaced by Templates
 - Controller gets replaced by View

A simple Hello-world application is just a few lines of code in Django! But moving from this simple thing a full fledged application can be a daunting task in itself. There are other concepts that can help proceed further such as ORM, migrations etc that help in building a bigger application. But for this tutorial we’ll be building a simple CRUD( Create, Retrieve, Update and Delete ) application.

To get started with you need to have python and virtualenv installed on your machine. Python is already installed on the linux systems. But you'll need to install virtualenv. To install virtualenv follow the command:

```
sudo apt-get install python-pip
sudo pip install virtualenv
```
The first line will install a package called python-pip which is a very important utility as far as python based developments are concerned. The second instruction installs virtualenv. For those of you who don't know virtualenv, virtualenv is a tool for creating isolated Python environments containing their own copy of python , pip , and their own place to keep libraries installed from PyPI.

##  Application structure

Before we actually start writing code we need to get a hold of the application structure. We'll first execute several commands that are essential in django project development.

After installing virtualenv, we need to set the environment up.

`virtualenv venv`

We are setting a virtual environment of the name venv here. Now we need to activate it.

```
source venv/bin/activate
cd venv
```

Now that it has been activated. We need to start our project. Feed in the following command to start a project.

```
pip install django==1.11.8
mkdir app && cd app
django-admin startproject crudapp
```

The first line installs Django v1.11.8 and creates a directory named app in the parent directory. the third line starts a project named crudapp in the app directory.
The directory tree should look like

```
app
└── crudapp
    ├── crudapp
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
```

We'll see the meaning of each file and what it does one by one. But first, to test if you are going in the right directoion, run the following command.

`python manage.py runserver`

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

`python manage.py startapp blog_posts`

This will create the necessary files that we require.

First and foremost create the Model of our application.

```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class blog_posts(models.Model):
    title = models.CharField(max_length=400)
    tag = models.CharField(max_length=50)
    author = models.CharField(max_length=120)

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})

```


Now that we have our model ready, we'll need to migrate it to the database.

```
python manage.py makemigrations
python manage.py migrate
```

Now we create our Views where we define each of our CRUD definition.

```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from blog_posts.models import blog_posts
# Create your views here.

class PostsForm(ModelForm):
    class Meta:
        model = blog_posts
        fields = ['id', 'title', 'author']

def post_list(request, template_name='blog_posts/post_list.html'):
    posts = blog_posts.objects.all()
    data = {}
    data['object_list'] = posts
    return render(request, template_name, data)

def post_create(request, template_name='blog_posts/post_form.html'):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})

def post_update(request, pk, template_name='blog_posts/post_form.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})

def post_delete(request, pk, template_name='blog_posts/post_delete.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'object': post})


```

Now that we have our Views, we create mappings to URL in our `/crudapp/blog_posts/urls.py` file. Make a note that the following is our app specific mappings.

```
"""
crudapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import url
from django.contrib import admin
from blog_posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new$', views.post_create, name='post_new'),
    url(r'^edit/(?P<pk>\d+)$', views.post_update, name='post_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),
]

```
 Now we create project specific mappings in `/crudapp/crudapp/urls.py`.

 ```
 """crudapp URL Configuration

 The `urlpatterns` list routes URLs to views. For more information please see:
     https://docs.djangoproject.com/en/1.11/topics/http/urls/
 """
 from django.conf.urls import url, include
 from django.contrib import admin
 from crudapp.views import home

 urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^blog_posts/', include('blog_posts.urls', namespace='blog_posts')),
     url(r'^$', home, name='home' ),
 ]

 ```

 Now almost everything is done and all we need to do is create our templates to test the operations.

 Go ahead and create a `templates/blog_posts` directory in `crudapp/blog_posts/`.

- `templates/blog_posts/post_list.html`:

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
    <title>Django CRUD application!</title>
  </head>
  <body>
    <div class="container">
        <h1>Blog Post List!</h1>
        <ul>
          {% for post in object_list %}
          <li><p>Post ID: <a href="{% url "blog_posts:post_edit" post.id %}">{{ post.id }}</a></p>
          <p>Title: {{ post.title }}</p>
            <a href="{% url "blog_posts:post_delete" post.id %}">Delete</a>
          </li>
          {% endfor %}
        </ul>

        <a href="{% url "blog_posts:post_new" %}">New Blog post entry</a>
    </div>
  </body>
</html>
```

- `templates/blog_posts/post_form.html`

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
    <title>Django CRUD application!</title>
  </head>
  <body>
    <div class="container">
      <form  method="post">{% csrf_token %}
        {{ form.as_p }}
        <input class="btn btn-primary" type="submit" value="Submit" />
      </form>
    </div>
  </body>
</html>
```

- `templates/blog_posts/post_delete.html`

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css">
    <title>Django CRUD application!</title>
  </head>
  <body>
    <div class="container">
      <form method="post">{% csrf_token %}
        Are you sure you want to delete "{{ object }}" ?
        <input class="btn btn-primary" type="submit" value="Submit" />
      </form>
    </div>
  </body>
</html>
```

Now we have all the necessary files and code that we require.

The final project tree should look like following:

```
crudapp
├── blog_posts
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   │   └── blog_posts
│   │       ├── post_delete.html
│   │       ├── post_form.html
│   │       └── post_list.html
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── crudapp
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt

```

Execute `python manage.py runserver` and voila!! You have your Django app ready.
