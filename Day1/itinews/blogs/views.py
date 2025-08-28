from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, ITI!")


def courses(request):
    
    courses_data = {
    'courses': 'python',
    'price': 1000
    }
    
    return render(request, 'blogs/courses.html', {'name': courses_data['courses'], 'price': courses_data['price']})

def tracks(request):
    tracks_data = ['python', 'Java', 'C#', 'Ai']
    return render(request, 'blogs/tracks.html', {'tracks': tracks_data})