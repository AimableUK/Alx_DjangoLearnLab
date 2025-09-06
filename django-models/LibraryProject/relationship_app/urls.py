from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, register_view

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    # Authentication
    path("login/", login_view.as_view(template_name="login"), name="login"),
    path("logout/", logout_view.as_view(template_name="logout"), name="logout"),
    path("register/", register_view, name="register"),
]
