from django.urls import path
from .views import (
    login, blogs, profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', login, name="register"),
    path('blogs/', blogs, name="blogs"),
    path('profile/', profile, name="profile"),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/edit/', CommentUpdateView, name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView, name='delete_comment'),

]