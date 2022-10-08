from django.contrib import admin
from django.urls import path, include
from registration_app.views import registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('registration/', registration),
]
