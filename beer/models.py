from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Beer(models.Model):
    nickname = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=False, verbose_name='URL')
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    rating = models.IntegerField()
    content = models.TextField(blank=True, verbose_name='Description')
    photo = models.ImageField(upload_to='beer/images', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('beer', kwargs={'beer_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Beer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Beer'
        verbose_name_plural = 'Beers'
