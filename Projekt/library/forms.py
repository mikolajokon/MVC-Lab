from django import forms
from .models import Author, Book, Borrowing


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'birth_year']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'birth_year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1000, 'max': 2026}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'isbn', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'author': forms.Select(attrs={'class': 'form-select'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'required': True, 'min': 1000, 'max': 2026}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 13}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn', '')
        if isbn and not isbn.isdigit():
            raise forms.ValidationError("ISBN może zawierać tylko cyfry.")
        if isbn and len(isbn) not in (0, 10, 13):
            raise forms.ValidationError("ISBN musi mieć 10 lub 13 cyfr.")
        return isbn


class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['book', 'borrower_name', 'borrowed_date', 'returned_date']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-select'}),
            'borrower_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'borrowed_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': True}),
            'returned_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean(self):
        cleaned = super().clean()
        borrowed = cleaned.get('borrowed_date')
        returned = cleaned.get('returned_date')
        if borrowed and returned and returned < borrowed:
            raise forms.ValidationError("Data zwrotu nie może być wcześniejsza niż data wypożyczenia.")
        return cleaned
