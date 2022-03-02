from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_create, name='create-book'),
    path('list/', views.book_list, name='book-list')
]
