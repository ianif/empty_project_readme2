# Makefile - common developer commands
# Use `make help` to see available targets.

SHELL := /bin/bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

# Optional PROJECT variables
PROJECT ?= artemis-project
PY ?= python3

# Detect tools
HAS_NPM := $(shell command -v npm >/dev/null 2>&1 && echo 1 || echo 0)
HAS_PNPM := $(shell command -v pnpm >/dev/null 2>&1 && echo 1 || echo 0)
HAS_YARN := $(shell command -v yarn >/dev/null 2>&1 && echo 1 || echo 0)
HAS_PYTEST := $(shell command -v pytest >/dev/null 2>&1 && echo 1 || echo 0)
HAS_RUFF := $(shell command -v ruff >/dev/null 2>&1 && echo 1 || echo 0)
HAS_FLAKE8 := $(shell command -v flake8 >/dev/null 2>&1 && echo 1 || echo 0)
HAS_BLACK := $(shell command -v black >/dev/null 2>&1 && echo 1 || echo 0)
HAS_ESLINT := $(shell command -v eslint >/dev/null 2>&1 && echo 1 || echo 0)
HAS_PRETTIER := $(shell command -v prettier >/dev/null 2>&1 && echo 1 || echo 0)

.DEFAULT_GOAL := help

help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "\n%s\n\n", "Available targets:"} \
	/^[a-zA-Z0-9_-]+:.*##/ { printf "  %-18s %s\n", $$1, $$2 } \
	END {print "\nTip: run \"make <target>\""}' $(MAKEFILE_LIST)

run: ## Run the app (auto-detect Node or Python)
	@if [ -f package.json ]; then \
	  if [ $(HAS_PNPM) -eq 1 ]; then pnpm run start; \
	  elif [ $(HAS_NPM) -eq 1 ]; then npm run start; \
	  elif [ $(HAS_YARN) -eq 1 ]; then yarn start; \
	  else echo "No Node package manager found (pnpm/npm/yarn)."; fi; \
	elif [ -f main.py ] || [ -f app.py ]; then \
	  $(PY) main.py 2>/dev/null || $(PY) app.py; \
	else \
	  echo "No known entrypoint found (package.json, main.py, app.py)."; \
	fi

install: ## Install dependencies when applicable
	@if [ -f package.json ]; then \
	  if [ $(HAS_PNPM) -eq 1 ]; then pnpm install; \
	  elif [ $(HAS_NPM) -eq 1 ]; then npm install; \
	  elif [ $(HAS_YARN) -eq 1 ]; then yarn install; \
	  else echo "No Node package manager found (pnpm/npm/yarn)."; fi; \
	elif [ -f requirements.txt ]; then \
	  $(PY) -m pip install -r requirements.txt; \
	else \
	  echo "No dependency manifest found (package.json or requirements.txt)."; \
	fi

test: ## Run tests if configured
	@if [ -f package.json ]; then \
	  if [ $(HAS_PNPM) -eq 1 ]; then pnpm test || pnpm run test; \
	  elif [ $(HAS_NPM) -eq 1 ]; then npm test || npm run test; \
	  elif [ $(HAS_YARN) -eq 1 ]; then yarn test; \
	  else echo "No Node package manager found (pnpm/npm/yarn)."; fi; \
	elif [ $(HAS_PYTEST) -eq 1 ]; then \
	  pytest -q; \
	else \
	  echo "No test runner detected."; \
	fi

lint: ## Run linters if configured
	@if [ -f package.json ] && [ $(HAS_ESLINT) -eq 1 ]; then \
	  npx --yes eslint .; \
	fi; \
	if [ $(HAS_RUFF) -eq 1 ]; then \
	  ruff check .; \
	elif [ $(HAS_FLAKE8) -eq 1 ]; then \
	  flake8 .; \
	else \
	  echo "No linter configured or installed."; \
	fi

format: ## Format code if configured
	@if [ -f package.json ] && [ $(HAS_PRETTIER) -eq 1 ]; then \
	  npx --yes prettier . --write; \
	fi; \
	if [ $(HAS_BLACK) -eq 1 ]; then \
	  black .; \
	elif [ $(HAS_RUFF) -eq 1 ]; then \
	  ruff format .; \
	else \
	  echo "No formatter configured or installed."; \
	fi

clean: ## Remove build/cache artifacts
	@echo "Cleaning..."
	@rm -rf node_modules dist build coverage .pytest_cache .ruff_cache .mypy_cache __pycache__ *.egg-info
	@echo "Done."

.PHONY: help run install test lint format clean
