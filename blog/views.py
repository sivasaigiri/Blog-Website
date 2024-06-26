from django.shortcuts import render
from django.http import HttpResponse
posts=[
    {
        'author':'coreyms',
        'title':'blogpost',
        'content':'firstpostcontent',
        'date_posted':'August 27,2024'
    },
    {
        'author':'ssg',
        'title':'combine the forces',
        'content':'second on',
        'date_posted':'August 28,2024'
    }
]
    
# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
