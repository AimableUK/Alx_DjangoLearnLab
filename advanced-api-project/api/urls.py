from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('/book/', ListView.as_view()),
    path('/books/detail/<int:pk>/', DetailView.as_view()),
    path('/books/create/', CreateView.as_view()),
    path('/books/update/<int:pk>/', UpdateView.as_view()),
    path('/books/delete/<int:pk>/', DeleteView.as_view()),   
]
