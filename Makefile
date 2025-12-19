.PHONY: help install install-dev build clean test run uninstall

help:
	@echo "Steam Offline Client - Build Commands"
	@echo ""
	@echo "Available targets:"
	@echo "  make install      - Install the package"
	@echo "  make install-dev  - Install in development mode"
	@echo "  make build        - Build distribution packages"
	@echo "  make clean        - Remove build artifacts"
	@echo "  make run          - Run the application (show help)"
	@echo "  make test         - Run tests"
	@echo "  make uninstall    - Uninstall the package"

install:
	pip install .

install-dev:
	pip install -e .

build:
	pip install build
	python -m build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

test:
	python3 steam_offline_client.py --help
	python3 steam_offline_client.py --version
	@echo "Basic tests passed!"

run:
	python3 steam_offline_client.py --help

uninstall:
	pip uninstall -y steam-offline-client
