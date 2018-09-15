from django.shortcuts import render
from django.http import HttpResponse
from django import template

posts = [
    {
        'author': 'Maria Bell',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',

    },
    {
        'author': 'Ben Dover',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2018',
        }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
