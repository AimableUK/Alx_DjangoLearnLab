from django.urls import path
from .views import (
    login, blogs, profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    posts_by_tag,
    search_posts
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
    path('post/<int:pk>/comments/new/', CommentCreateView, name='create_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView, name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView, name='delete_comment'),
    path('tags/<slug:tag_slug>/', posts_by_tag, name='posts_by_tag'),
    path('search/', search_posts, name='search_posts'),
]