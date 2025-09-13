# Update the book's title
book = Book.objects.get()
book.title = "the real Gen-Z
book.save()

# Verify update
Book.objects.get(id=b.id).title
# Expected output:
# 'Nineteen Eighty-Four'
