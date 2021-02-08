from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='crud_index'),
    path('index', views.index2, name='api_index'),
    path('create', views.createPage, name='create_page'),
    path('create_post', views.create, name='crud_create'),
    path('edit/<int:id>', views.editPage, name='edit_page'),
    path('update/<int:id>', views.update, name='crud_update'),
    path('delete/<int:id>', views.delete, name='crud_delete'),
]
