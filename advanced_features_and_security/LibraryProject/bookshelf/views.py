from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Post
from .models import Book, BookForm, ExampleForm
from .forms import BookSearchForm



def book_list(request):
    """
    View that returns a list of books.
    Exposes 'books' queryset and a search form.
    Uses Django ORM properly (no raw SQL with string interpolation).
    """
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            # Safe ORM filtering — parameterized by Django ORM (prevents SQL injection)
            # Using __icontains for case-insensitive containment search.
            books = books.filter(title__icontains=q) | books.filter(author__icontains=q)

    context = {"books": books, "form": form}
    return render(request, "bookshelf/book_list.html", context)


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # Example of using Django forms to validate input (use ModelForm in real app)
    if request.method == "POST":
        # Prefer using ModelForm -- not shown here for brevity
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect("book_list")
    return render(request, "bookshelf/form_example.html")

def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # safely access cleaned data
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            # here you would save or process the data
            return render(request, "bookshelf/form_example.html", {
                "form": ExampleForm(), 
                "success": True
            })
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/book_form.html", {"form": form})

# View posts
@permission_required('models.can_view', raise_exception=True)
def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})



# Create post
@permission_required('models.can_create', raise_exception=True)
def post_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect("post_list")
    return render(request, "posts/post_form.html")


# Edit post
@permission_required('models.can_edit', raise_exception=True)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("post_list")
    return render(request, "posts/post_form.html", {"post": post})


# Delete post
@permission_required('models.can_delete', raise_exception=True)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post_list")
