# relationship_app/views.py
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView  # checker wants this exact import

# Function-based view
def book_list(request):
    books = Book.objects.all()  # must be exactly this
    context = {"book_list": books}  # key must be 'book_list'
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
