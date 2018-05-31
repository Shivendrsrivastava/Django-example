from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def other(request):
    return render(request, 'simple_app/other.html')


def index(request):
    return render(request, 'simple_app/index.html')

def relative(request):
    return render(request, 'simple_app/relative_url.html')
