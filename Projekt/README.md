# System zarządzania cyfrową biblioteką (Django)

Aplikacja webowa do zarządzania biblioteką — książkami, autorami i wypożyczeniami. Zbudowana we frameworku Django z wykorzystaniem wzorca architektonicznego MVC (MTV w nomenklaturze Django).

## Spis treści

- [Funkcjonalności](#funkcjonalności)
- [Struktura MVC](#struktura-mvc)
- [Wymagania](#wymagania)
- [Instalacja i uruchomienie](#instalacja-i-uruchomienie)
- [Docker](#docker)
- [Testy](#testy)
- [Przykładowe dane](#przykładowe-dane)

## Funkcjonalności

**Podstawowe (CRUD):**
- Dodawanie, edycja, usuwanie i przeglądanie książek
- Dodawanie, edycja, usuwanie i przeglądanie autorów
- Rejestrowanie i zarządzanie wypożyczeniami

**Rozszerzone:**
- **Dodatkowe modele z relacjami** — model `Author` (powiązany z `Book` relacją ForeignKey) oraz model `Borrowing` (powiązany z `Book`). Książka wyświetla status dostępności na podstawie aktywnych wypożyczeń.
- **Ostylowane widoki** — Bootstrap 5 + Bootstrap Icons: responsywne tabele, karty, badge'e statusów, nawigacja.
- **Walidacja serwer + klient** — Django Forms z walidatorami (format ISBN, zakres dat, wymagane pola) + atrybuty HTML5 (min, max, required, type=date).
- **Filtrowanie i wyszukiwanie** — wyszukiwanie książek po tytule, filtrowanie po autorze; wyszukiwanie autorów po nazwisku; filtrowanie wypożyczeń po statusie (aktywne/zwrócone).
- **Docker** — Dockerfile + docker-compose.yml do uruchomienia aplikacji w kontenerze.
- **Testy jednostkowe** — testy modeli, widoków i walidacji formularzy.

## Struktura MVC

| Warstwa | Django | Pliki |
|---------|--------|-------|
| Model | Models | `library/models.py` — Author, Book, Borrowing |
| Kontroler | Views | `library/views.py` — logika obsługi żądań HTTP |
| Widok | Templates | `templates/` — szablony HTML (Jinja-like) |
| Routing | URLs | `library/urls.py` — mapowanie URL → widok |

## Wymagania

- Python 3.10+
- Django 5.x

## Instalacja i uruchomienie

```bash
# 1. Klonowanie repozytorium
git clone <url-repozytorium>
cd django-library

# 2. Utworzenie wirtualnego środowiska (opcjonalne, ale zalecane)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Instalacja zależności
pip install -r requirements.txt

# 4. Migracje bazy danych
python manage.py migrate

# 5. (Opcjonalnie) Załadowanie przykładowych danych
python manage.py shell < seed_data.py

# 6. Uruchomienie serwera
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000

## Docker

```bash
# Budowanie i uruchomienie
docker-compose up --build

# Migracje (w osobnym terminalu)
docker-compose exec web python manage.py migrate

# Załadowanie danych przykładowych
docker-compose exec web python manage.py shell < seed_data.py
```

## Testy

```bash
python manage.py test library
```

## Przykładowe dane

Plik `seed_data.py` zawiera przykładowe dane: 3 autorów (Mickiewicz, Sienkiewicz, Lem), 6 książek i 3 wypożyczenia.
