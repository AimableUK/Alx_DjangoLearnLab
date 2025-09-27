from django.urls import path, include
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('/book/', ListView.as_view()),
    path('/books/<int:pk>/', DetailView.as_view()),
    path('/books/<int:pk>/', CreateView.as_view()),
    path('/books/<int:pk>/', UpdateView.as_view()),
    path('/books/<int:pk>/', DeleteView.as_view()),   
]
