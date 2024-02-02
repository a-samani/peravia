from tabnanny import verbose
from django.db.models import Q
from django.db import models
from django.urls import reverse
import os
from utilities.utils import *

# ----------------------------------------------------------


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


# ----------------------------------------------------------

def upload_file_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/characteristics/{final_name}"

# ----------------------------------------------------------


def upload_category_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"categories/{final_name}"

# ----------------------------------------------------------


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(is_active=True)

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(application__icontains=query) |
            Q(category__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, is_active=True).distinct()

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(category__title__iexact=category_name, is_active=True)

# ----------------------------------------------------------


class MainCategory(models.Model):
    title = models.CharField(max_length=100)
    persian_title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=300)
    persian_description = models.CharField(max_length=300, default="")
    class Meta:
        ordering = ['title']
        verbose_name = 'Main Category'
        verbose_name_plural = 'Main Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product:sub_category_list", args=[self.title])


# ----------------------------------------------------------

class Category(models.Model):
    title = models.CharField(max_length=100)
    persian_title = models.CharField(max_length=100, default="")
    slug = models.SlugField(max_length=100)
    image = models.ImageField(
        upload_to=upload_category_image_path, null=True, blank=True)
    main_category = models.ForeignKey(
        MainCategory, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['title']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_by_category', args=[self.slug])


# ----------------------------------------------------------

class Product(models.Model):
    title = models.CharField(max_length=150)
    persian_title = models.CharField(max_length=150, default="")
    slug = models.SlugField(max_length=150)
    application = models.CharField(max_length=250, default="")
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=False)
    persian_description = models.TextField(null=True, default="")
    main_application = models.TextField(null=False)
    caution = models.TextField(null=False)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True)
    characteristics = models.FileField(
        upload_to=upload_file_path, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    objects = ProductManager()

    class Meta:
        ordering = ['title']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:single_product', args=[str(self.id), self.slug.upper()])


# ----------------------------------------------------------

class Specification(models.Model):
    title = models.CharField(max_length=100)
    persian_title = models.CharField(max_length=100, default="")
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


# ----------------------------------------------------------

class Advantage(models.Model):
    title = models.TextField()
    persian_title = models.TextField(default="")
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.title
