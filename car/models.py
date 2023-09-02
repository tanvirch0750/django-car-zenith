from django.db import models
from django.db.models import Avg, Count
from django.urls import reverse

from account.models import Account
from brand.models import Brand
from django.utils.text import slugify

# Create your models here.

class Car(models.Model):
    title           = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=1000, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/cars')
    color           = models.CharField(max_length=50)
    model           = models.CharField(max_length=50)
    is_available    = models.BooleanField(default=True)
    brand           = models.ForeignKey(Brand, on_delete=models.CASCADE)
    features        = models.TextField(max_length=500, blank=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    is_featured     = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('car_detail', args=[self.brand.slug, self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    


