.PHONY: run lock install

# Starts the development server
run:
	uvicorn --app-dir src learnage.main:app --reload

# Generates a requirements.txt lock file from pyproject.toml
lock:
	uv pip compile pyproject.toml -o requirements.txt

# Installs dependencies from the lock file
install:
	uv pip sync -r requirements.txt