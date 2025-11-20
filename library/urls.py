from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Home
    path('', views.home, name='home'),
    
    # Books
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:pk>/view/', views.book_content_view, name='book_content_view'),
    path('books/<int:pk>/download/', views.book_content_download, name='book_content_download'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    
    # Authors
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/add/', views.author_create, name='author_create'),
    
    # Genres
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/add/', views.genre_create, name='genre_create'),
    
    # Borrowings
    path('borrowings/', views.borrowing_list, name='borrowing_list'),
    path('borrowings/add/', views.borrowing_create, name='borrowing_create'),
    path('borrowings/add/<int:book_pk>/', views.borrowing_create, name='borrowing_create_book'),
    path('borrowings/<int:pk>/return/', views.borrowing_return, name='borrowing_return'),
]

