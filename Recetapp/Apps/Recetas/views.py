from django.shortcuts import render


# Create your views here.

def index(request):

    test = {}

    return render(request, "index.html", test)
