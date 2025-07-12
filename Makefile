.PHONY: run lock install migrate upgrade

# Starts the development server
run:
	uvicorn --app-dir src learnage.main:app --reload

# Generates a requirements.txt lock file from pyproject.toml
lock:
	uv pip compile pyproject.toml -o requirements.txt

# Installs dependencies from the lock file
install:
	uv pip sync -r requirements.txt

# Generates a new database migration file
# Usage: make migrate m="your migration message"
migrate:
	@if [ -z "$(m)" ]; then \
		echo "Usage: make migrate m=\"your migration message\""; \
		exit 1; \
	fi
	alembic revision --autogenerate -m "$(m)"

# Applies all pending migrations to the database
upgrade:
	alembic upgrade head

