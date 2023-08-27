from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import *

# Create your views here.
menu = [
    {'text': 'About us', 'url_name': 'about'},
    {'text': 'Add a beer', 'url_name': 'add_beer'},
]


class BeerHome(ListView):
    model = Beer
    template_name = 'beer/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        return context


# def index(request):
#     title = 'Main page'
#
#     context = {
#         'title': title,
#         'menu': menu,
#     }
#     return render(request, 'beer/index.html', context)


def about(request):
    title = 'About'
    return render(request, 'beer/about.html', {
        'title': title,
        'menu': menu
    })


def contacts(request):
    title = 'Contacts'
    return render(request, 'beer/contacts.html', {
        'title': title,
        'menu': menu
    })


def add_beer(request):
    title = 'Add beer'
    if request.method == 'POST':
        form = EntryBeer(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = EntryBeer()
    return render(request, 'beer/add_beer.html', {
        'title': title,
        'form': form,
        'menu': menu
    })


def thanks(request):
    title = 'Thanks'
    return render(request, 'beer/thanks.html', {
        'title': title,
        'menu': menu
    })


def show_beer(request, beer_slug):
    beer_name = get_object_or_404(Beer, slug=beer_slug)
    title = beer_name
    return render(request, 'beer/show_more_about_beer.html', {
        'beer_name': beer_name,
        'menu': menu,
        'beer_slug': beer_slug,
        'title': title
    })


def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    beers = Beer.objects.filter(cat_id=cat[0].id)
    title = cat_slug.capitalize()
    if len(beers) == 0:
        raise Http404

    return render(request, 'beer/show_beers_in_category.html', {
        'beers': beers,
        'cat_slug': cat_slug,
        'menu': menu,
        'cat': cat,
        'title': title
    })
