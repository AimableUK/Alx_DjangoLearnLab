from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book


class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

# class BookDetailView(generics.De)