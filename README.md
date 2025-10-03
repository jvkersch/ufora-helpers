# Ufora Helpers

A Python package with utilities for working with Ufora, the university educational platform. Currently includes tools for converting custom score formats to CSV format suitable for Ufora upload.

## Installation

Install globally with pipx (recommended):

```bash
pipx install .
```

Or install in development mode:

```bash
pip install -e .
```

## Score Conversion Tool

Convert scores from a CSV file to Ufora format:

```bash
convert-scores input.csv score_column_name --id ID_column --max 10
```

### Arguments

- `input.csv`: Path to the input CSV file containing student scores
- `score_column_name`: Name of the column containing the scores to convert
- `--id ID_column`: Name of the column containing student IDs (default: "ID")
- `--max N`: Maximum points for the assignment (default: 10)

### Example

```bash
convert-scores grades.csv "Assignment 1" --id StudentID --max 20
```

This reads `grades.csv`, extracts scores from the "Assignment 1" column, uses "StudentID" as the ID column, and sets the maximum points to 20.

## Output Format

The tool outputs a CSV file to stdout with the following columns:

- `OrgDefinedId`: Student IDs formatted as `#0{id}` for Ufora compatibility
- `{column_name} Points Grade <Numeric MaxPoints:{max}>`: The score column with Ufora-specific formatting
- `End-of-Line indicator`: Always "#" as required by Ufora

## Input Requirements

The input CSV should contain:
- A column with student IDs (numeric)
- A column with scores for the assignment
- Any rows with missing IDs will be filtered out

## Development

Install development dependencies:

```bash
pip install -e .[dev]
```

Run code quality tools:

```bash
black .          # Format code
ruff check .     # Lint code
pytest           # Run tests (when available)
```