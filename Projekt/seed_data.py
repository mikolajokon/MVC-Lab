"""
Skrypt do załadowania przykładowych danych.
Użycie: python manage.py shell < seed_data.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
django.setup()

from library.models import Author, Book, Borrowing
from datetime import date

# Autorzy
a1 = Author.objects.get_or_create(first_name="Adam", last_name="Mickiewicz", defaults={"birth_year": 1798})[0]
a2 = Author.objects.get_or_create(first_name="Henryk", last_name="Sienkiewicz", defaults={"birth_year": 1846})[0]
a3 = Author.objects.get_or_create(first_name="Stanisław", last_name="Lem", defaults={"birth_year": 1921})[0]

# Książki
b1 = Book.objects.get_or_create(title="Pan Tadeusz", author=a1, defaults={"year": 1834, "isbn": "9788373271234"})[0]
b2 = Book.objects.get_or_create(title="Dziady", author=a1, defaults={"year": 1823})[0]
b3 = Book.objects.get_or_create(title="Quo Vadis", author=a2, defaults={"year": 1896, "isbn": "9788307032456"})[0]
b4 = Book.objects.get_or_create(title="Potop", author=a2, defaults={"year": 1886})[0]
b5 = Book.objects.get_or_create(title="Solaris", author=a3, defaults={"year": 1961, "isbn": "9780156027601"})[0]
b6 = Book.objects.get_or_create(title="Cyberiada", author=a3, defaults={"year": 1965})[0]

# Wypożyczenia
Borrowing.objects.get_or_create(book=b1, borrower_name="Jan Kowalski", defaults={"borrowed_date": date(2024, 3, 1), "returned_date": date(2024, 3, 15)})
Borrowing.objects.get_or_create(book=b3, borrower_name="Anna Nowak", defaults={"borrowed_date": date(2024, 6, 1)})
Borrowing.objects.get_or_create(book=b5, borrower_name="Piotr Wiśniewski", defaults={"borrowed_date": date(2024, 5, 10), "returned_date": date(2024, 5, 25)})

print("Dane przykładowe załadowane.")
