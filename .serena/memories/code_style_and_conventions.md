# Code Style and Conventions

## Formatting Standards
- **Formatter**: black (version 25.11.0) - enforces PEP 8 style
- **Import sorting**: isort (version 7.0.0)
- **Linter**: ruff (version 0.14.8) with auto-fix enabled

## Code Conventions Observed

### Type Hints
- Functions use type hints for parameters and return types
- Examples: `-> pd.DataFrame`, `-> None`
- Import types from standard library or third-party packages

### Docstrings
- Written in **German** (not English)
- Use triple-quoted strings
- Simple explanatory style
- Example:
  ```python
  def ensure_directories():
      """
      Stellt sicher, dass alle wichtigen Verzeichnisse existieren.
      """
  ```

### Naming Conventions
- **Variables/Functions**: snake_case (lowercase with underscores)
- **Constants**: UPPER_SNAKE_CASE
- **Module names**: lowercase with underscores
- **Language**: German names for domain-specific variables (e.g., `VARIABLES_BLOCK1`, `quick_value_glimpse`)

### Import Organization
- Standard library imports first
- Third-party imports second
- Local imports last
- Example from block1_univariat.py:
  ```python
  import pandas as pd
  
  from config import DATA_PROCESSED
  ```

### Module Structure
- Configuration constants at the top
- Helper functions in the middle
- `main()` function at the bottom
- `if __name__ == "__main__":` guard for script execution

### Path Handling
- Use `pathlib.Path` for all file paths (not string concatenation)
- Centralized path configuration in `src/config.py`

### Comments
- Written in **German**
- Used for section headers and clarifications
- Example: `# Projektwurzel (z. B. .../statistik-workbook)`

### Code Organization
- Modular: separate files for each analysis block
- Each block has its own constants and functions
- Common configuration in `config.py`
- Master script `run_all.py` orchestrates the pipeline
