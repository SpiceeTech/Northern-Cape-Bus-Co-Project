from django.contrib import admin
from django.urls import path, include
from registration_app.views import registration
from login_app.views import login
from loyal_users_app.views import loyal_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('registration/', registration),
    path('login/', login),
    path('loyal_users/', loyal_users),
]
