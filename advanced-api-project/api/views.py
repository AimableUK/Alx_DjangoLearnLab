from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated, AllowAny


class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny]


class DetailView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field= 'pk'


class CreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field= 'pk'
    permission_classes = [IsAuthenticated]
    

class UpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field= 'pk'
    permission_classes = [IsAuthenticated]
    

class DeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    lookup_field= 'pk'
    permission_classes = [IsAuthenticated]
    