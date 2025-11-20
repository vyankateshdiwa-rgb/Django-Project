from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('reserved', 'Reserved'),
    ]

    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='books')
    description = models.TextField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    total_copies = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    available_copies = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    content_file = models.FileField(upload_to='book_content/', blank=True, null=True, help_text='Upload PDF or document file')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    def save(self, *args, **kwargs):
        # Auto-update status based on available copies
        # Only mark as 'borrowed' when no copies are available
        # Otherwise, mark as 'available' and show available copy count
        if self.available_copies == 0:
            self.status = 'borrowed'
        else:
            self.status = 'available'
        super().save(*args, **kwargs)


class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowings')
    borrower_name = models.CharField(max_length=200)
    borrower_email = models.EmailField()
    borrower_phone = models.CharField(max_length=20, blank=True, null=True)
    borrow_date = models.DateField(default=timezone.now)
    return_date = models.DateField(blank=True, null=True)
    due_date = models.DateField()
    is_returned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-borrow_date']

    def __str__(self):
        return f"{self.book.title} - {self.borrower_name}"

    def save(self, *args, **kwargs):
        if self.is_returned and not self.return_date:
            self.return_date = timezone.now().date()
            # Increase available copies when book is returned
            self.book.available_copies += 1
            self.book.save()
        super().save(*args, **kwargs)

