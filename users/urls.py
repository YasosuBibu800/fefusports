from django.contrib import admin
from django.urls import path, include

from users.views import *

urlpatterns = [
    path("profile/", profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name="register"),
]
