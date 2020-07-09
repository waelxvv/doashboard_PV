# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('homepage/', views.homepage, name="homepage"),
    path('contact/', views.contact, name="contact"),
    path('conseils/', views.conseils, name="conseils"),
    path('supervision/', views.supervision, name="supervision"),
    path('blog/', views.blog, name="blog")
]
