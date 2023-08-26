
from django.contrib import admin
from django.urls import path, include
from vehiculos import views, urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('vehiculos.urls')),
    path("accounts/", include("django.contrib.auth.urls"))
]
