# Delete the book instance
b.delete()

# Verify deletion
Book.objects.all()
# Expected output:
# <QuerySet []>
