from django.contrib import admin
from .models import Author, Book, Borrowing

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Borrowing)
