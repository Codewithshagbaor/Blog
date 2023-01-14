from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('create/', views.createPost, name="create_post"),
  path('logout/', views.logoutView, name="logout-view"),
  path('<str:slug>/', views.View_Post, name="view_post"),
  path('Profile/<str:username>/', views.view_user, name="view_user"),
]