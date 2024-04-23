from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q

# Create your views here.


class BooksListView(ListView):
    model = Book
    template_name = 'list_books.html'
    context_object_name = 'books'



class BookDetailView(DetailView):
    model = Book
    template_name = 'book_details.html'
    context_object_name = 'book'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'search_results.html'

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query))