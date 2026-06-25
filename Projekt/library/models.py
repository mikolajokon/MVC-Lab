from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    first_name = models.CharField("Imię", max_length=100)
    last_name = models.CharField("Nazwisko", max_length=100)
    birth_year = models.IntegerField(
        "Rok urodzenia",
        blank=True,
        null=True,
        validators=[MinValueValidator(1000), MaxValueValidator(2026)],
    )

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField("Tytuł", max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name="Autor",
    )
    year = models.IntegerField(
        "Rok wydania",
        validators=[MinValueValidator(1000), MaxValueValidator(2026)],
    )
    isbn = models.CharField("ISBN", max_length=13, blank=True, default="")
    description = models.TextField("Opis", blank=True, default="")

    class Meta:
        ordering = ['title']
        verbose_name = "Książka"
        verbose_name_plural = "Książki"

    def __str__(self):
        return f"{self.title} ({self.year})"

    @property
    def is_available(self):
        return not self.borrowings.filter(returned_date__isnull=True).exists()


class Borrowing(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='borrowings',
        verbose_name="Książka",
    )
    borrower_name = models.CharField("Imię i nazwisko wypożyczającego", max_length=200)
    borrowed_date = models.DateField("Data wypożyczenia")
    returned_date = models.DateField("Data zwrotu", blank=True, null=True)

    class Meta:
        ordering = ['-borrowed_date']
        verbose_name = "Wypożyczenie"
        verbose_name_plural = "Wypożyczenia"

    def __str__(self):
        status = "zwrócono" if self.returned_date else "wypożyczona"
        return f"{self.book.title} → {self.borrower_name} ({status})"
