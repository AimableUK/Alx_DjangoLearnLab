from bookshelf.models import Book

# Create a Book instance
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)


# Expected output: Book instance is saved to the database
# No output is displayed in shell, but the object exists in DB
