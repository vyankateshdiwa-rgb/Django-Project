from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden, FileResponse, Http404
from django.conf import settings
import os
from .models import Book, Author, Genre, Borrowing
from .forms import BookForm, AuthorForm, GenreForm, BorrowingForm, SearchForm, CustomUserCreationForm


def is_admin(user):
    """Check if user is admin/staff"""
    return user.is_authenticated and user.is_staff


def register_view(request):
    """User registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'library/register.html', {'form': form})


def login_view(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'library/login.html')


@login_required
def logout_view(request):
    """User logout"""
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


def home(request):
    """Home page with statistics and recent books"""
    total_books = Book.objects.count()
    total_authors = Author.objects.count()
    total_genres = Genre.objects.count()
    borrowed_books = Borrowing.objects.filter(is_returned=False).count()
    available_books = Book.objects.filter(status='available').count()
    
    recent_books = Book.objects.all()[:6]
    
    context = {
        'total_books': total_books,
        'total_authors': total_authors,
        'total_genres': total_genres,
        'borrowed_books': borrowed_books,
        'available_books': available_books,
        'recent_books': recent_books,
    }
    return render(request, 'library/home.html', context)


def book_list(request):
    """List all books with search and filter"""
    form = SearchForm(request.GET)
    books = Book.objects.all()
    
    if form.is_valid():
        query = form.cleaned_data.get('query')
        genre = form.cleaned_data.get('genre')
        
        if query:
            books = books.filter(
                Q(title__icontains=query) |
                Q(author__name__icontains=query) |
                Q(isbn__icontains=query) |
                Q(description__icontains=query)
            )
        
        if genre:
            books = books.filter(genre=genre)
    
    # Pagination
    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get user's borrowed books for content access check
    user_borrowed_books = set()
    if request.user.is_authenticated and not request.user.is_staff:
        user_borrowed_books = set(
            Borrowing.objects.filter(
                borrower_email=request.user.email,
                is_returned=False
            ).values_list('book_id', flat=True)
        )
    
    context = {
        'page_obj': page_obj,
        'form': form,
        'genres': Genre.objects.all(),
        'user_borrowed_books': user_borrowed_books,
    }
    return render(request, 'library/book_list.html', context)


def book_detail(request, pk):
    """Book detail page"""
    book = get_object_or_404(Book, pk=pk)
    borrowings = Borrowing.objects.filter(book=book, is_returned=False)
    
    # Check if current user has borrowed this book
    user_has_borrowed = False
    if request.user.is_authenticated:
        if request.user.is_staff:
            user_has_borrowed = True  # Admins can always access
        else:
            user_has_borrowed = Borrowing.objects.filter(
                book=book,
                borrower_email=request.user.email,
                is_returned=False
            ).exists()
    
    context = {
        'book': book,
        'borrowings': borrowings,
        'user_has_borrowed': user_has_borrowed,
    }
    return render(request, 'library/book_detail.html', context)


@login_required
def book_content_view(request, pk):
    """View book content (PDF/document) - Only for users who borrowed the book"""
    book = get_object_or_404(Book, pk=pk)
    
    if not book.content_file:
        raise Http404("Book content not available")
    
    # Check if user has borrowed this book (not returned)
    # Admins can always access
    if not request.user.is_staff:
        has_borrowed = Borrowing.objects.filter(
            book=book,
            borrower_email=request.user.email,
            is_returned=False
        ).exists()
        
        if not has_borrowed:
            messages.error(request, 'You must borrow this book first to view its content.')
            return redirect('book_detail', pk=book.pk)
    
    file_path = book.content_file.path
    if not os.path.exists(file_path):
        raise Http404("File not found")
    
    # Determine content type
    content_type = 'application/pdf'
    if file_path.endswith('.doc') or file_path.endswith('.docx'):
        content_type = 'application/msword'
    elif file_path.endswith('.txt'):
        content_type = 'text/plain'
    elif file_path.endswith('.epub'):
        content_type = 'application/epub+zip'
    
    response = FileResponse(open(file_path, 'rb'), content_type=content_type)
    response['Content-Disposition'] = f'inline; filename="{book.content_file.name}"'
    return response


@login_required
def book_content_download(request, pk):
    """Download book content - Only for users who borrowed the book"""
    book = get_object_or_404(Book, pk=pk)
    
    if not book.content_file:
        raise Http404("Book content not available")
    
    # Check if user has borrowed this book (not returned)
    # Admins can always access
    if not request.user.is_staff:
        has_borrowed = Borrowing.objects.filter(
            book=book,
            borrower_email=request.user.email,
            is_returned=False
        ).exists()
        
        if not has_borrowed:
            messages.error(request, 'You must borrow this book first to download its content.')
            return redirect('book_detail', pk=book.pk)
    
    file_path = book.content_file.path
    if not os.path.exists(file_path):
        raise Http404("File not found")
    
    response = FileResponse(open(file_path, 'rb'))
    filename = os.path.basename(book.content_file.name)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


@user_passes_test(is_admin)
def book_create(request):
    """Create a new book - Admin only"""
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')
        # Form is invalid, will re-render with errors and preserved data
    else:
        form = BookForm()
    
    context = {'form': form, 'title': 'Add New Book'}
    return render(request, 'library/book_form.html', context)


@user_passes_test(is_admin)
def book_update(request, pk):
    """Update an existing book - Admin only"""
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_detail', pk=book.pk)
        # Form is invalid, will re-render with errors and preserved data
    else:
        form = BookForm(instance=book)
    
    context = {'form': form, 'book': book, 'title': 'Edit Book'}
    return render(request, 'library/book_form.html', context)


@user_passes_test(is_admin)
def book_delete(request, pk):
    """Delete a book - Admin only"""
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    
    context = {'book': book}
    return render(request, 'library/book_confirm_delete.html', context)


def author_list(request):
    """List all authors"""
    authors = Author.objects.all()
    
    paginator = Paginator(authors, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj}
    return render(request, 'library/author_list.html', context)


def author_detail(request, pk):
    """Author detail page"""
    author = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(author=author)
    
    context = {
        'author': author,
        'books': books,
    }
    return render(request, 'library/author_detail.html', context)


@user_passes_test(is_admin)
def author_create(request):
    """Create a new author - Admin only"""
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author added successfully!')
            return redirect('author_list')
        # Form is invalid, will re-render with errors and preserved data
    else:
        form = AuthorForm()
    
    context = {'form': form, 'title': 'Add New Author'}
    return render(request, 'library/author_form.html', context)


def genre_list(request):
    """List all genres"""
    genres = Genre.objects.all()
    
    context = {'genres': genres}
    return render(request, 'library/genre_list.html', context)


@user_passes_test(is_admin)
def genre_create(request):
    """Create a new genre - Admin only"""
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Genre added successfully!')
            return redirect('genre_list')
        # Form is invalid, will re-render with errors and preserved data
    else:
        form = GenreForm()
    
    context = {'form': form, 'title': 'Add New Genre'}
    return render(request, 'library/genre_form.html', context)


@login_required
def borrowing_list(request):
    """List all borrowings - Login required"""
    # Regular users see only their borrowings, admins see all
    if request.user.is_staff:
        borrowings = Borrowing.objects.all()
    else:
        borrowings = Borrowing.objects.filter(borrower_email=request.user.email)
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter == 'active':
        borrowings = borrowings.filter(is_returned=False)
    elif status_filter == 'returned':
        borrowings = borrowings.filter(is_returned=True)
    
    paginator = Paginator(borrowings, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'status_filter': status_filter,
    }
    return render(request, 'library/borrowing_list.html', context)


@login_required
def borrowing_create(request, book_pk=None):
    """Create a new borrowing - Login required"""
    book = None
    if book_pk:
        book = get_object_or_404(Book, pk=book_pk)
    
    if request.method == 'POST':
        form = BorrowingForm(request.POST)
        if form.is_valid():
            borrowing = form.save(commit=False)
            if book:
                borrowing.book = book
            # Auto-fill user info if not admin
            if not request.user.is_staff:
                borrowing.borrower_name = request.user.get_full_name() or request.user.username
                borrowing.borrower_email = request.user.email
            # Decrease available copies
            borrowing.book.available_copies -= 1
            borrowing.book.save()
            borrowing.save()
            messages.success(request, 'Book borrowed successfully!')
            return redirect('borrowing_list')
    else:
        form = BorrowingForm()
        if book:
            form.fields['book'].initial = book
        # Pre-fill user info for regular users
        if not request.user.is_staff:
            form.fields['borrower_name'].initial = request.user.get_full_name() or request.user.username
            form.fields['borrower_email'].initial = request.user.email
    
    context = {'form': form, 'title': 'Borrow Book', 'book': book}
    return render(request, 'library/borrowing_form.html', context)


@login_required
def borrowing_return(request, pk):
    """Mark a borrowing as returned - Login required"""
    borrowing = get_object_or_404(Borrowing, pk=pk)
    
    # Regular users can only return their own books
    if not request.user.is_staff and borrowing.borrower_email != request.user.email:
        messages.error(request, 'You can only return books you borrowed.')
        return redirect('borrowing_list')
    
    if request.method == 'POST':
        borrowing.is_returned = True
        borrowing.save()
        messages.success(request, 'Book returned successfully!')
        return redirect('borrowing_list')
    
    context = {'borrowing': borrowing}
    return render(request, 'library/borrowing_return.html', context)

