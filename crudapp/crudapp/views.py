
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Django CRUD Example</h1>
    <a href="/blog_posts/">Blog post CRUD example</a><br>
    """
    return HttpResponse(html)
