from django.contrib import admin
from .models import Books, Subjects

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'subject')  # Display these fields in the admin list view
    search_fields = ('title', 'author', 'isbn')  # Add search functionality for these fields
    list_filter = ('subject',)  # Add a filter for subjects

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the subject name in the admin list view
    search_fields = ('name',)  # Add search functionality for subjects