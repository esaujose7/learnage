.PHONY: run install migrate upgrade

# Starts the development server
run:
	uvicorn --app-dir src learnage.main:app --reload

# Installs dependencies from the uv.lock file
install:
	uv sync

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