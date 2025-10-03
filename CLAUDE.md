# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python package with utilities for working with Ufora (university educational platform). Currently includes tools for processing class scores into CSV format suitable for Ufora upload. The package can be installed via pipx and is designed to be extensible for additional Ufora-related utilities.

## Installation and Usage

Install with pipx:
```bash
pipx install .
```

Use the console script:
```bash
convert-scores input.csv score_column_name --id ID_column --max 10
```

## Commands

- **Install in development mode**: `pip install -e .`
- **Install with pipx**: `pipx install .`
- **Run linting**: `ruff check .`
- **Run formatting**: `black .`
- **Run tests**: `pytest` (when tests are added)

## Package Structure

- `ufora_scores/cli.py`: Main CLI module with console script entry point
- `ufora_scores/__init__.py`: Package initialization
- `pyproject.toml`: Project configuration and dependencies

## Core Functionality

The CLI tool converts CSV files with student scores to Ufora-compatible format:

- **Input**: CSV file with student ID column and score column
- **Output**: Formatted CSV to stdout with OrgDefinedId, score column, and end-of-line indicator
- **Key transformation**: Student IDs are formatted as "#0{id}" for Ufora compatibility
- **Dependencies**: pandas for CSV processing

## Architecture

- Modern Python package structure with pyproject.toml
- Console script entry point for easy installation
- Uses pandas for CSV manipulation
- Command-line interface with argparse
- Outputs directly to stdout for shell redirection
- Configured for code quality tools (black, ruff)

## Development Notes

- Uses hatchling as build backend
- Supports Python 3.8+
- Score formatting follows Ufora's specific requirements: "ColumnName Points Grade <Numeric MaxPoints:N>"
- Ready for expansion with additional Ufora utilities and helpers