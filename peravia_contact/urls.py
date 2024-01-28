from django.urls import path
from .views import contact_us_page, write_us

# ----------------------------------------------------------
app_name = 'contact'
# ----------------------------------------------------------
urlpatterns = [
    path('contact-us/', contact_us_page, name='contact_page'),
    path('write-us/', write_us, name='write_us_fun'),
]
