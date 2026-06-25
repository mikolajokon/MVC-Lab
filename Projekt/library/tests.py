from django.test import TestCase, Client
from django.urls import reverse
from .models import Author, Book, Borrowing
from datetime import date


class AuthorModelTest(TestCase):
    def test_str(self):
        author = Author.objects.create(first_name="Adam", last_name="Mickiewicz")
        self.assertEqual(str(author), "Adam Mickiewicz")


class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Adam", last_name="Mickiewicz")
        self.book = Book.objects.create(title="Pan Tadeusz", author=self.author, year=1834)

    def test_str(self):
        self.assertEqual(str(self.book), "Pan Tadeusz (1834)")

    def test_is_available_when_no_borrowings(self):
        self.assertTrue(self.book.is_available)

    def test_is_not_available_when_borrowed(self):
        Borrowing.objects.create(book=self.book, borrower_name="Jan Kowalski", borrowed_date=date.today())
        self.assertFalse(self.book.is_available)

    def test_is_available_when_returned(self):
        Borrowing.objects.create(
            book=self.book, borrower_name="Jan Kowalski",
            borrowed_date=date(2024, 1, 1), returned_date=date(2024, 1, 15),
        )
        self.assertTrue(self.book.is_available)


class BookViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(first_name="Henryk", last_name="Sienkiewicz")
        self.book = Book.objects.create(title="Quo Vadis", author=self.author, year=1896)

    def test_book_list_status(self):
        resp = self.client.get(reverse('book_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Quo Vadis")

    def test_book_list_search(self):
        resp = self.client.get(reverse('book_list'), {'q': 'Quo'})
        self.assertContains(resp, "Quo Vadis")

    def test_book_create(self):
        resp = self.client.post(reverse('book_create'), {
            'title': 'Potop', 'author': self.author.pk, 'year': 1886,
        })
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Book.objects.filter(title='Potop').exists())

    def test_book_detail(self):
        resp = self.client.get(reverse('book_detail', args=[self.book.pk]))
        self.assertEqual(resp.status_code, 200)

    def test_book_delete(self):
        resp = self.client.post(reverse('book_delete', args=[self.book.pk]))
        self.assertEqual(resp.status_code, 302)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())


class ValidationTest(TestCase):
    def test_book_form_invalid_isbn(self):
        from .forms import BookForm
        author = Author.objects.create(first_name="Test", last_name="Author")
        form = BookForm(data={
            'title': 'Test', 'author': author.pk, 'year': 2020, 'isbn': 'abc',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('isbn', form.errors)

    def test_borrowing_form_invalid_dates(self):
        from .forms import BorrowingForm
        author = Author.objects.create(first_name="T", last_name="A")
        book = Book.objects.create(title="T", author=author, year=2020)
        form = BorrowingForm(data={
            'book': book.pk, 'borrower_name': 'Jan',
            'borrowed_date': '2024-06-01', 'returned_date': '2024-05-01',
        })
        self.assertFalse(form.is_valid())
