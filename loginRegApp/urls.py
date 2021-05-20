from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('signup/', views.signup),
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),
    path('addNote/', views.createNote),
]