import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from django_models.relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # 1. Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in {library_name}:")
        for book in library.books.all():
            print(f"- {book.title}")

        # 3. Retrieve the librarian for a library
        if hasattr(library, "librarian") and library.librarian:
            print(f"\nLibrarian for {library_name}: {library.librarian.name}")
        else:
            print(f"\nNo librarian assigned to {library_name}")
    except Library.DoesNotExist:
        print(f"\nNo library found with name {library_name}")


if __name__ == "__main__":
    run_queries()
