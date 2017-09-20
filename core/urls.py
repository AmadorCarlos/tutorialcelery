from django.conf.urls import include, url
from django.contrib import admin
from .views import GenerateRandomUserForm

urlpatterns = [
    url(r'templates/$', GenerateRandomUserForm.as_view(), name='GenerateRandomUserForm'),
]
