from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
# Create your views here.


class BooksListView(ListView):
    model = Book
    template_name = 'list_books.html'
    context_object_name = 'books'



class BookDetailView(DetailView):
    model = Book
    template_name = 'book_details.html'
    context_object_name = 'book'
    