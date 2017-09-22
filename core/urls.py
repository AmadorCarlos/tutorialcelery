from django.conf.urls import include, url
from django.contrib import admin
from .views import GenerateRandomUserForm
from .views import UsersListView

urlpatterns = [
    url(r'templates/$', GenerateRandomUserForm.as_view(), name='GenerateRandomUserForm'),
    url(r'users/$', UsersListView.as_view(), name='userlist'),
]
