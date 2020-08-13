from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Student/', include('Student.urls')),
    path('admin/', admin.site.urls),
]
