from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# ----------------------------------------------------------
class Contact(models.Model):
    fullname = models.CharField(max_length=400)
    persian_fullname = models.CharField(max_length=400, null=True, default="", blank=True)
    email = models.EmailField('email address')
    phone_number = models.CharField(max_length=16)
    subject = models.TextField()
    persian_subject = models.TextField(null=True, default="", blank=True)
    enquiry = models.TextField()
    persian_enquiry = models.TextField(null=True, default="", blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.email


# ----------------------------------------------------------
class WriteUs(models.Model):
    fullname = models.CharField(max_length=400)
    phone = models.CharField(max_length=16)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_added']
