# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a utility project for processing class scores into CSV format suitable for upload to Ufora (university educational platform). The project contains Python scripts that convert custom score formats to Ufora's required format.

## Core Script: process-ufora.py

The main script converts CSV files with student scores to Ufora-compatible format:

- **Input**: CSV file with student ID column and score column
- **Output**: Formatted CSV to stdout with OrgDefinedId, score column, and end-of-line indicator
- **Key transformation**: Student IDs are formatted as "#0{id}" for Ufora compatibility
- **Dependencies**: pandas for CSV processing

### Usage Pattern
```bash
python process-ufora.py input.csv score_column_name --id ID_column --max 10
```

## Architecture

- Single-script architecture with potential for expansion
- Uses pandas for CSV manipulation
- Command-line interface with argparse
- Outputs directly to stdout for shell redirection
- No configuration files or complex dependencies

## Development Notes

- No package management files (requirements.txt, pyproject.toml) currently present
- No test framework configured
- Simple utility script design - functions are focused and single-purpose
- Score formatting follows Ufora's specific requirements: "ColumnName Points Grade <Numeric MaxPoints:N>"