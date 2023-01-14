from django.urls import path
from . import views

urlpatterns = [
  path('', views.signUpView, name="signup"),
  path('login/', views.loginView, name="login-view"),
  path('complete_reg/', views.complete_reg, name="complete_reg"),
]