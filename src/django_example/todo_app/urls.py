from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_book, name='add_book'),
    path('read/<int:book_id>/', views.mark_read, name='mark_read'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]