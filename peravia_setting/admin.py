from django.contrib import admin
from .models import SiteSetting, SocialMedia, Client, Certificate

# ----------------------------------------------------------
admin.site.register(SiteSetting)
admin.site.register(SocialMedia)
admin.site.register(Client)
admin.site.register(Certificate)
