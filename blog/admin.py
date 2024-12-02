from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'image', 'file')  # Displaying file in the list view
    search_fields = ('title', 'author', 'category')  # Adding search functionality for title, author, and category
    list_filter = ('category',)  # Adding filter for category
    fields = ('title', 'author', 'category', 'image', 'file')  # Adding fields to be displayed in the form

admin.site.register(Book, BookAdmin)
