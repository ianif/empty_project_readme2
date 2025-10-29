# empty_project_readme2
<!-- artemis testing -->

## Run commands

This repository includes a Makefile with common developer commands. It auto-detects typical Node.js and Python setups and uses available tools when present. If nothing is detected, the targets will print a helpful message and exit successfully.

Common targets:
- make help — list all targets and their descriptions
- make run — run the application (auto-detects Node or Python entry points)
- make test — run tests when configured
- make lint — run linters if configured
- make format — format code if configured
- make clean — remove common build and cache artifacts

Examples:
```
make help
make run
make test
```
<!-- artemis testing -->