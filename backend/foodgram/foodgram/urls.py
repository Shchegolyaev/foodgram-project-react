from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('api/', include('users.urls')),
    path('api/', include('recipes.urls')),
    path('admin/', admin.site.urls),
]
