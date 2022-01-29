from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from babu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("babu.urls"))
]
