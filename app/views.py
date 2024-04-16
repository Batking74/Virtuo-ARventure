# The views.py file is where u define what data or files to serve to the client when they hit a specific route
from django.shortcuts import render
from django.http import HttpResponse

# Serving up Index Page View
def index(request, id):
    # Html goes in as an argument
    return HttpResponse("<h1>Hello World Naz! I got your parameter which was  %s</h1>" % id)


def home(request):
    return render(request, 'app/index.html')


def speechRecognition(request):
    return render(request, "app/speech_recognition.html", {})