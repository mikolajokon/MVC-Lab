from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Author, Book, Borrowing
from .forms import AuthorForm, BookForm, BorrowingForm


# --- Strona główna ---

def index(request):
    return render(request, 'library/index.html', {
        'book_count': Book.objects.count(),
        'author_count': Author.objects.count(),
        'borrowing_count': Borrowing.objects.filter(returned_date__isnull=True).count(),
    })


# --- Autorzy ---

def author_list(request):
    query = request.GET.get('q', '')
    authors = Author.objects.all()
    if query:
        authors = authors.filter(last_name__icontains=query) | authors.filter(first_name__icontains=query)
    return render(request, 'library/author_list.html', {'authors': authors, 'query': query})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'library/author_detail.html', {'author': author})


def author_create(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Autor został dodany.")
        return redirect('author_list')
    return render(request, 'library/author_form.html', {'form': form, 'title': 'Dodaj autora'})


def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    form = AuthorForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        messages.success(request, "Autor został zaktualizowany.")
        return redirect('author_list')
    return render(request, 'library/author_form.html', {'form': form, 'title': 'Edytuj autora'})


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        messages.success(request, "Autor został usunięty.")
        return redirect('author_list')
    return render(request, 'library/confirm_delete.html', {'object': author, 'cancel_url': 'author_list'})


# --- Książki ---

def book_list(request):
    query = request.GET.get('q', '')
    author_id = request.GET.get('author', '')
    books = Book.objects.select_related('author').all()
    if query:
        books = books.filter(title__icontains=query)
    if author_id:
        books = books.filter(author_id=author_id)
    authors = Author.objects.all()
    return render(request, 'library/book_list.html', {
        'books': books, 'query': query, 'authors': authors, 'selected_author': author_id,
    })


def book_detail(request, pk):
    book = get_object_or_404(Book.objects.select_related('author'), pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Książka została dodana.")
        return redirect('book_list')
    return render(request, 'library/book_form.html', {'form': form, 'title': 'Dodaj książkę'})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, "Książka została zaktualizowana.")
        return redirect('book_list')
    return render(request, 'library/book_form.html', {'form': form, 'title': 'Edytuj książkę'})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Książka została usunięta.")
        return redirect('book_list')
    return render(request, 'library/confirm_delete.html', {'object': book, 'cancel_url': 'book_list'})


# --- Wypożyczenia ---

def borrowing_list(request):
    status = request.GET.get('status', '')
    borrowings = Borrowing.objects.select_related('book', 'book__author').all()
    if status == 'active':
        borrowings = borrowings.filter(returned_date__isnull=True)
    elif status == 'returned':
        borrowings = borrowings.filter(returned_date__isnull=False)
    return render(request, 'library/borrowing_list.html', {
        'borrowings': borrowings, 'selected_status': status,
    })


def borrowing_create(request):
    form = BorrowingForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Wypożyczenie zostało zarejestrowane.")
        return redirect('borrowing_list')
    return render(request, 'library/borrowing_form.html', {'form': form, 'title': 'Dodaj wypożyczenie'})


def borrowing_update(request, pk):
    borrowing = get_object_or_404(Borrowing, pk=pk)
    form = BorrowingForm(request.POST or None, instance=borrowing)
    if form.is_valid():
        form.save()
        messages.success(request, "Wypożyczenie zostało zaktualizowane.")
        return redirect('borrowing_list')
    return render(request, 'library/borrowing_form.html', {'form': form, 'title': 'Edytuj wypożyczenie'})


def borrowing_delete(request, pk):
    borrowing = get_object_or_404(Borrowing, pk=pk)
    if request.method == 'POST':
        borrowing.delete()
        messages.success(request, "Wypożyczenie zostało usunięte.")
        return redirect('borrowing_list')
    return render(request, 'library/confirm_delete.html', {'object': borrowing, 'cancel_url': 'borrowing_list'})
