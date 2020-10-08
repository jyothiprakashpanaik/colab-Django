# For data base
from django.db import models

# Create your models here.

# Creat categories of model
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title



# Creat Image Model
class Image(models.Model):
    title = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'images')
    issued = models.DateTimeField()
    discribe = models.TextField()
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
