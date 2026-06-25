# MVC-Laboratoria

This repository contains multiple sample web application projects built with different frameworks and platforms.

## Workspace structure

- `Dotnet/`
  - Contains an ASP.NET Core MVC sample application named `MvcMovie`.
  - Includes controllers, models, views, a database context, and EF Core migrations.

- `Projekt/`
  - Contains a Django project with an app named `library`.
  - Includes Django settings, models, views, templates, and a SQLite database file.

- `Python/`
  - Contains another Python web app sample, including a Django-style project with `mysite` and a `polls` app.

## How to use

Choose the project you want to open and work with from the root workspace.

### ASP.NET Core (`Dotnet/MvcMovie`)

1. Open the `Dotnet/MvcMovie` folder in your IDE.
2. Restore and build using the .NET SDK.
3. Run the application using `dotnet run` from the `Dotnet/MvcMovie` folder.

### Django project (`Projekt`)

1. Open the `Projekt` folder in your IDE.
2. Create and activate a Python virtual environment.
3. Install dependencies from `requirements.txt`.
4. Run migrations and start the Django development server.

### Python sample (`Python`)

1. Open the `Python` folder in your IDE.
2. Use the included `manage.py` for Django management commands.

## Notes

- The repository contains multiple sample applications and is organized by platform.
- Use the project folders directly for development, testing, and exploration.
