from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookCreate.as_view(), name='create-book'),
    path('list/', views.BookList.as_view(), name='book-list'),
    path('list/<int:pk>', views.Book_detail.as_view())
]
