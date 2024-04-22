from django.urls import path
from .views import BooksListView, BookDetailView

urlpatterns = [
    path('', BooksListView.as_view(), name='list_books'),
    path('details/<uuid:pk>/', BookDetailView.as_view(), name='book_details'),
    
]
