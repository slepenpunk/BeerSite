from django.urls import path
from .views import *

urlpatterns = [
    path('', BeerHome.as_view(), name='main'),
    path('about/', about, name='about'),
    path('about/contacts', contacts, name='contacts'),
    path('add_beer/', add_beer, name='add_beer'),
    path('thanks/', thanks, name='thanks'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
    path('beer/<slug:beer_slug>/', show_beer, name='beer'),

]
