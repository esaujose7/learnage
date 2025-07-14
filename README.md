# learnage

A simple FastAPI application for managing notes, built with Python, SQLAlchemy, and Alembic.

This project is structured following the `package` layout and uses `uv` for package management and a `Makefile` for running common development tasks.

## Getting Started

This guide will walk you through setting up the project for local development.

### Prerequisites

Before you begin, ensure you have the following tools installed:

-   Python (v3.13+)
-   [uv](https://github.com/astral-sh/uv)
-   `git`
-   `make`

### Installation & Setup

Follow these steps to get your development environment up and running:

1.  **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd learnage
    ```

2.  **Create and Activate the Virtual Environment**
    This command creates a local `.venv` directory for your project's dependencies.
    ```bash
    uv venv
    source .venv/bin/activate
    ```

3.  **Create Your Local Configuration**
    Copy the example environment file. This file provides the necessary environment variables, like the database URL.
    ```bash
    cp .env.example .env
    ```

4.  **Install Dependencies**
    This command reads the `uv.lock` file and installs the exact versions of all required packages into your virtual environment.
    ```bash
    make install
    ```

5.  **Run Database Migrations**
    This command creates the database and all necessary tables based on the current models.
    ```bash
    make upgrade
    ```

You are now ready to run the application!

## Development Workflow

### Running the Application
To start the development server with hot-reloading enabled, run:
```bash
make run
```
The API will be available at `http://127.0.0.1:8000`.

### Managing Dependencies
-   **To add a new dependency:** `uv add <package-name>`
-   **To remove a dependency:** `uv remove <package-name>`
-   **To install dependencies after a pull:** `make install`

### Database Migrations
When you change a model in `learnage/models/`, you must create a new migration and apply it.

1.  **Generate the migration file:**
    ```bash
    make migrate m="your descriptive message"
    ```
2.  **Apply the migration to the database:**
    ```bash
    make upgrade
    ```

## Available Commands

All common development tasks are managed through the `Makefile`.

| Command | Description |
| :--- | :--- |
| `make run` | Starts the development server with hot-reloading. |
| `make install` | Installs/syncs dependencies from the `uv.lock` file. |
| `make migrate m="..."` | Generates a new database migration file. Requires a message. |
| `make upgrade` | Applies all pending migrations to the database. |
