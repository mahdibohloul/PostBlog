from django.shortcuts import render

posts = [
    {
        'author': 'Mahdi',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 30, 2020'
    },
    {
        'author': 'Erfan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 29, 2020'
    }

]


def home(request):
    context = {
        'posts': posts,
        'title': 'Home',
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'blog/about.html', context)