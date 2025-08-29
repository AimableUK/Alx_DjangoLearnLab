# Update the book's title
b.title = "Nineteen Eighty-Four"
b.save()

# Verify update
Book.objects.get(id=b.id).title
# Expected output:
# 'Nineteen Eighty-Four'
