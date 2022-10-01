from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('info/', views.info, name="info"),
  path('about-us/', views.about_us, name="about_us"),
  path('contacts/', views.contact, name="contacts"),
  path('login/', views.login, name="login"),
  path('registration/', views.registration, name="registration"),
]