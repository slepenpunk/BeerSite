from django.contrib import admin
from .models import *


# Register your models here.

class BeerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Beer, BeerAdmin)
admin.site.register(Category, CategoryAdmin)
