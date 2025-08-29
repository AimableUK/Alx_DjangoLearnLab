from bookshelf.models import Book

# Create a Book instance
b = Book(title="1984", author="George Orwell", publication_year=1949)
b.save()
# Expected output: Book instance is saved to the database
# No output is displayed in shell, but the object exists in DB

# Retrieve all books
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)

# Expected output:
# 1984 George Orwell 1949

# Update the book's title
b.title = "Nineteen Eighty-Four"
b.save()

# Verify update
Book.objects.get(id=b.id).title
# Expected output:
# 'Nineteen Eighty-Four'

# Delete the book instance
b.delete()

# Verify deletion
Book.objects.all()
# Expected output:
# <QuerySet []>

