from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display=['title','author', 'publication_year']
    list_filter = ('author',)
    search_fields = ['title']

# Register your models here.
admin.site.register(Book)


class CustomUserAdmin(UserAdmin):
    """Admin panel configuration for CustomUser."""

    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_of_birth")

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo", "is_staff", "is_active"),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
