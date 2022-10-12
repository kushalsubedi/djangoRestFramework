from django.urls import URLPattern, path 
from . import views
from .views import api_home

urlpatterns=[
    path('',views.api_home),
]