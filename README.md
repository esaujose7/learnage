# learnage

A simple FastAPI application for managing notes, built with Python, SQLAlchemy, and Alembic.

This project is structured following the `src` layout and uses `uv` for package management and a `Makefile` for running common development tasks.

## Getting Started

### Prerequisites

- Python 3.13+
- `uv` (https://github.com/astral-sh/uv)
- `make`

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd learnage
    ```

2.  **Create a virtual environment:**
    ```bash
    uv venv
    ```

3.  **Install dependencies:**
    This will install all the exact package versions from the `requirements.txt` lock file.
    ```bash
    make install
    ```

## Available Commands

All common development tasks are managed through the `Makefile`.

| Command | Description |
| :--- | :--- |
| `make run` | Starts the development server with hot-reloading. |
| `make install` | Installs or syncs dependencies from the `requirements.txt` lock file. |
| `make lock` | Generates/updates the `requirements.txt` lock file from `pyproject.toml`. |
| `make migrate m="<message>"` | Generates a new database migration file. Remember to provide a descriptive message. |
| `make upgrade` | Applies all pending migrations to the database. |

### Development Workflow

1.  **Run the server:**
    ```bash
    make run
    ```
    The API will be available at `http://127.0.0.1:8000`.

2.  **Making database changes:**
    - Modify a model in `src/learnage/models/`.
    - Run `make migrate m="your descriptive message"`.
    - Run `make upgrade` to apply the changes to the database.
