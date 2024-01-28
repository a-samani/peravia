from django.urls import path
from .views import LoginUser, RegisterUser, LogoutUser

# ----------------------------------------------------------
app_name = 'accounts'
# ----------------------------------------------------------
urlpatterns = [
    path('login', LoginUser, name='login_user'),
    path('register', RegisterUser, name='register_user'),
    path('logout', LogoutUser, name='logout_user'),
]
