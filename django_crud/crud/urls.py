from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='crud_index'),
    path('create', views.create, name='crud_create'),
]
