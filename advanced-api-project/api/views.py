from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book


class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    

class DetailView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field= 'pk'


class CreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field= 'pk'
    

class UpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field= 'pk'
    

class DeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    lookup_field= 'pk'
    