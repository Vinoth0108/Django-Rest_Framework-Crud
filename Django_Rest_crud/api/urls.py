from django.urls import path
from . import views

urlpatterns = [
    path('', views.getdata),
    path('add/', views.addItem),
    path('delete/<int:pk>/', views.deleteItem, name='delete_item'),
     path('update/<int:pk>/', views.updateItem, name='update_item')
]