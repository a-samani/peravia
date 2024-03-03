from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.db.models import Q
from django.utils import tree
from peravia_accounts.models import CustomUser
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from utilities.utils import *

# ----------------------------------------------------------


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"blog/{final_name}"

# ----------------------------------------------------------


class BlogManager(models.Manager):
    def get_active_post(self):
        return self.get_queryset().filter(draft=False)

    def serach_article(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
        return self.get_queryset().filter(lookup).distinct()
# ----------------------------------------------------------


class BlogPost(models.Model):
    title = models.CharField(unique=True, max_length=250)
    persian_title = models.CharField(max_length=250, null=True, default="", blank=True)
    slug = models.SlugField(unique=True, max_length=250)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()
    updated_on = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False)
    post_image = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True)

    objects = BlogManager()

    class Meta:
        ordering = ['-updated_on']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[str(self.id), self.slug])
# ----------------------------------------------------------


class News(models.Model):
    title = models.CharField(unique=True, max_length=250)
    persian_title = models.CharField(unique=True, max_length=250, null=True, default="", blank=True)
    slug = models.SlugField(unique=True, max_length=250)
    summary = models.CharField(max_length=500)
    persian_summary = models.CharField(max_length=500, null=True, default="", blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField(null=True,)
    news_image = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True, default="")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:news_detail", args=[str(self.id),self.slug])
    
