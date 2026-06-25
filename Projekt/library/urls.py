from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Autorzy
    path('authors/', views.author_list, name='author_list'),
    path('authors/add/', views.author_create, name='author_create'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/<int:pk>/edit/', views.author_update, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),

    # Książki
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # Wypożyczenia
    path('borrowings/', views.borrowing_list, name='borrowing_list'),
    path('borrowings/add/', views.borrowing_create, name='borrowing_create'),
    path('borrowings/<int:pk>/edit/', views.borrowing_update, name='borrowing_update'),
    path('borrowings/<int:pk>/delete/', views.borrowing_delete, name='borrowing_delete'),
]
