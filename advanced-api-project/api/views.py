from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author']
    Ordering_fields = ['title', 'publication_year']


class DetailView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field= 'pk'


class CreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]
    

class UpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field= 'pk'
    permission_classes = [IsAuthenticated]
    

class DeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field= 'pk'
    permission_classes = [IsAuthenticated]
    