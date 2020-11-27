from django.shortcuts import render

# Create your views here.

posts = [
    {'author': 'Ziad Sherif',
     'title': 'Post 1',
     'content': 'First post content',
     'date_posted': 'November 27, 2020'
    },
    {'author': 'John Doe',
     'title': 'Post 2',
     'content': 'Second post content',
     'date_posted': 'November 26, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html', context)

def about(request):
    
    return render(request, 'blog/about.html', {'title': 'About'})
