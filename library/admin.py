from django.contrib import admin
from .models import Author, Genre, Book, Borrowing


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'created_at']
    search_fields = ['name', 'bio']
    list_filter = ['created_at']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'status', 'available_copies', 'total_copies', 'has_content', 'created_at']
    list_filter = ['status', 'genre', 'author', 'created_at']
    search_fields = ['title', 'isbn', 'author__name']
    readonly_fields = ['created_at', 'updated_at']
    
    def has_content(self, obj):
        return bool(obj.content_file)
    has_content.boolean = True
    has_content.short_description = 'Has Content'


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ['book', 'borrower_name', 'borrow_date', 'due_date', 'is_returned', 'return_date']
    list_filter = ['is_returned', 'borrow_date', 'due_date']
    search_fields = ['book__title', 'borrower_name', 'borrower_email']
    readonly_fields = ['created_at', 'updated_at']

