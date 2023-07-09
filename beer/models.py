from django.db import models

# Create your models here.
class Beer(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    rating = models.IntegerField()
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/',blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'