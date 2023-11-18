from django.urls import path, include
from .views import about

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', about, name='about')
]
