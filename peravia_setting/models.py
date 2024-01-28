from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.utils.translation import gettext_lazy as _
from utilities.utils import *


# ----------------------------------------------------------
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"setting/{final_name}"
# ----------------------------------------------------------


def upload_certificate_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"certificate/{final_name}"
# ----------------------------------------------------------


def upload_file_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"certificate/pdf/{final_name}"


# ----------------------------------------------------------
class SiteSetting(models.Model):
    address = models.TextField()
    short_description = models.TextField(default='Short Description')
    phone = models.CharField(max_length=25)
    fax = models.CharField(max_length=25)
    support_email = models.EmailField(_('email address'))

    class Meta:
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return 'Peravia Setting'


# ----------------------------------------------------------
class SocialMedia(models.Model):
    title = models.CharField(max_length=20, default='Social Media')
    address = models.CharField(max_length=200)
    setting = models.ForeignKey(SiteSetting, on_delete=models.CASCADE)

    def __str__(self):
        return self.address


# ----------------------------------------------------------
class Client(models.Model):
    title = models.CharField(max_length=200)
    site_address = models.CharField(max_length=300)
    image = models.ImageField(
        upload_to=upload_image_path, blank=True, null=True)

    def __str__(self):
        return self.title

# ----------------------------------------------------------


class Certificate(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to=upload_certificate_image_path, blank=True, null=True)
    pdf_file = models.FileField(
        upload_to=upload_file_path, blank=True, null=True)
    
    def __str__(self):
        return self.title
