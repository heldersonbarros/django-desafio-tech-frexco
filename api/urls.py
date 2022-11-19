from django.urls import path
from .views import RegisterView, UserListView, UserXSLXView, UserCSVVIew
from rest_framework.authtoken import views

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', views.obtain_auth_token),
    path('users', UserListView.as_view()), 
    path('users/xlsx', UserXSLXView.as_view()),
    path('users/csv', UserCSVVIew.as_view()),
]