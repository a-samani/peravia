from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# ----------------------------------------------------------
class Contact(models.Model):
    fullname = models.CharField(max_length=400)
    email = models.EmailField(_('email address'))
    phone_number = models.CharField(max_length=16)
    subject = models.TextField()
    enquiry = models.TextField()
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
