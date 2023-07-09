from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('about/', about, name='about'),
    path('about/contacts', contacts, name='contacts'),
    path('reviews/', reviews, name='reviews'),
]
