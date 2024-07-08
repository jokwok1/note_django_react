"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# prebuilt views to help obtain our access and refresh tokens

urlpatterns = [
    path('admin/', admin.site.urls), # path are url to go to that performs specific operation
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    # dont forget trailing / at the end, call the view and make user
    path("api/token/", TokenObtainPairView.as_view(), name ="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")), # prebuilt URL from rest framework
    path("api/", include("api.urls"))

]
