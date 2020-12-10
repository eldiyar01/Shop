from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, null=False)


class Subcategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategories')
    title = models.CharField(max_length=100, null=False)


class Furniture(models.Model):
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE, related_name='furniture')
    title = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    description = models.TextField(null=False)
    date = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False, null=True)

    def get_absolute_url(self):
        return reverse('furniture:sng_furniture', kwargs={'pk': self.pk})


class Gallery(models.Model):
    image = models.ImageField(upload_to='furniture_img', blank=True, null=True)
    furniture = models.ForeignKey('Furniture', on_delete=models.CASCADE, related_name='images')
