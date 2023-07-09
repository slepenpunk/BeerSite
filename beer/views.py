from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    title = 'Main page'
    return render(request, 'beer/index.html', {
        'title': title
    })


def about(request):
    title = 'About'
    return render(request, 'beer/about.html', {
        'title': title
    })


def contacts(request):
    title = 'Contacts'
    return render(request, 'beer/contacts.html', {
        'title': title
    })


def reviews(request):
    title = 'All reviews'
    beers = Beer.objects.all()
    return render(request, 'beer/reviews.html', {
        'title': title,
        'beers': beers
    })
