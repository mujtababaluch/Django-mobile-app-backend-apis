from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import os


def get_image_path(instance, filename):
    return os.path.join("product_images", filename)

# Create your models here.

class Categories(models.Model):
    Category_name= models.CharField(max_length=250)

    def __str__(self):
          return self.Category_name

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class products(models.Model):
        product_name= models.CharField(max_length=250)
        product_desc=models.TextField()
        price=models.IntegerField()
    #     SIZE_CHOICES = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    #     ('XL', 'ExtraLarge'),
    # )
        color= models.CharField(max_length=250)
        product_picone = models.ImageField(upload_to=get_image_path)
        product_pictwo = models.ImageField(upload_to=get_image_path)
        product_picthree = models.ImageField(upload_to=get_image_path)
        product_picfour = models.ImageField(upload_to=get_image_path)
        Category_name = models.ForeignKey(Categories,on_delete=models.CASCADE)
        size_one = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products_with_size_one')
        size_two = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products_with_size_two', null=True, blank=True)
        size_three = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products_with_size_three', null=True, blank=True)
        size_four = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='products_with_size_four', null=True, blank=True)
        
        def __str__(self):
          return self.product_name


class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    # Override the groups field with a different related_name
    groups = models.ManyToManyField(Group, related_name='custom_users_group')
    # Override the user_permissions field with a different related_name
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permission')

