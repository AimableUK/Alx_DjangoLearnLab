from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, PostForm, CommentForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from taggit.models import Tag
from django.db.models import Q


User = get_user_model()



def login(request):
    
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('pswd', '')
        print(username, password)
        errors = []
        
        if not username:
            errors.append("username required")
        if not password:
            errors.append('Password is required') 
            
        if not errors:
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                redirect('/')
            else:
                errors.append("Invalid username or password.")
        
        context = {
            'errors': errors,
            'username': username,
        }
        return render(request, 'blog/login.html', context)
    
    return render(request, 'blog/login.html')

def register(request):
    
    return render(request, 'blog/register.html', )


def blogs(request):
    
    
    
    return render(request, 'blog/blogs.html', )


@login_required
def profile(request):
    user = request.user
    if request.user == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
        else:
            form = UserEditForm(instance=user)
        
    
        context = {
            'form': form,
            'user': user,
        }
    context = {}
    return render(request, 'blog/profile.html', context)


# list posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    
# post details
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    
# class Based view for comment
"""
# Create a new comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = ''
    form_class = CommentForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Update an existing comment
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = ''
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Delete a comment
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = ''
    success_url = reverse_lazy('post-list')
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
"""

# function Based view for comment
def CommentCreateView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def CommentUpdateView(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form})

@login_required
def CommentDeleteView(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    post_id = comment.post.pk
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=post_id)
    return render(request, 'blog/delete_comment.html', {'comment': comment})


class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')
        return Post.objects.filter(tags__name__iexact=tag_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs.get('tag_name')
        return context
    
    
def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.all()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})