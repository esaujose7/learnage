# Project Context: learnage

This file contains a summary of the work done on the `learnage` project to provide context for future sessions.

## Project Overview
- **Technology Stack:** FastAPI, Python, uv, SQLAlchemy, Alembic, SQLite.
- **Project Structure:** The project follows a `src` layout, with the main application package located at `src/learnage`.

## Key Refactoring and Setup Steps:
1.  **`src` Layout:** The project was migrated from a flat layout to a `src` layout. All application code now resides in `src/learnage`.
2.  **API Routers:** Note-related API endpoints were moved from `main.py` to a dedicated router in `src/learnage/api/notes.py`.
3.  **Model Organization:** Models were moved from a single `models.py` file to a `models` package at `src/learnage/models/`.
4.  **Database Client:** The database connection logic was moved to `src/learnage/clients/database.py`.
5.  **Dependency Management:**
    - Dependencies (`fastapi`, `uvicorn[standard]`, `sqlalchemy`, `alembic`) were added to `pyproject.toml`.
    - A `requirements.txt` lock file was generated using `uv pip compile`.
6.  **Task Runner:** A `Makefile` was created to provide simple commands for common development tasks:
    - `make run`: Starts the development server.
    - `make lock`: Generates the `requirements.txt` lock file.
    - `make install`: Installs dependencies from the lock file.
    - `make migrate m="<message>"`: Creates a new database migration.
    - `make upgrade`: Applies pending database migrations.

## Important Notes:
- The project uses `uv` for package management.
- The `Makefile` is the primary interface for running development tasks.
- Alembic is configured to find the application models within the `src` directory.
