from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    date_added = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.title} - {self.price}€"
