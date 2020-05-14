from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Djange!")
# .shortcuts import render

# Create your views here.