# Design Patterns and Guidelines

## Project-Specific Patterns

### 1. Centralized Configuration
- All paths and constants are defined in `src/config.py`
- Use `from config import DATA_PROCESSED, FIGURES_DIR, etc.`
- Never hardcode paths in individual scripts
- Path objects use `pathlib.Path` for cross-platform compatibility

### 2. Modular Analysis Blocks
- Each assignment task has its own Python module (block1-5)
- Each block is self-contained and can run independently
- Each block defines:
  - Constants (e.g., `VARIABLES_BLOCK1`)
  - Helper functions
  - A `main()` function
  - `if __name__ == "__main__":` guard

### 3. Data Flow Pattern
```
Raw Excel (.xlsx) → data_prep.py → Processed CSV
                                  ↓
                            block1-5.py → figures/ (plots)
                                       → latex/tables/ (.tex)
                                  ↓
                            LaTeX compilation → main.pdf
```

### 4. Script Execution Pattern
Each analysis script follows this pattern:
```python
# Imports
import pandas as pd
from config import RELEVANT_PATHS

# Constants
FILENAME = "..."
VARIABLES = [...]

# Helper functions
def load_data() -> pd.DataFrame:
    """German docstring"""
    ...

def analyze_data(...) -> None:
    """German docstring"""
    ...

# Main entry point
def main():
    df = load_data()
    analyze_data(df)

if __name__ == "__main__":
    main()
```

### 5. LaTeX Integration Pattern
- Python generates `.tex` table files → `latex/tables/`
- Python generates plots (PDF/PNG) → `figures/`
- LaTeX sections use `\input{tables/tablename.tex}`
- LaTeX sections use `\includegraphics{../figures/plotname.pdf}`

## General Guidelines

### Language
- **Code**: English for standard Python elements (function/variable names from libraries)
- **Domain-specific code**: German names (e.g., `quick_value_glimpse`, `VARIABLES_BLOCK1`)
- **Comments**: Always in German
- **Docstrings**: Always in German

### Error Handling
- Currently minimal error handling in the codebase
- Scripts assume data files exist and are well-formed
- When adding error handling, use informative German messages

### Output and Logging
- Use `print()` statements for progress tracking
- Format: descriptive German messages
- Example: `print("=== Schritt 1: Verzeichnisse prüfen ===")`

### Naming
- Use descriptive German names for domain concepts
- Keep standard library/package names in English
- Examples:
  - Good: `load_processed()`, `check_variables_exist()`
  - Good: `DATA_RAW`, `FIGURES_DIR`

### Code Organization
- Keep imports minimal and organized (isort handles this)
- Group related constants together
- Functions in logical order (data loading → processing → output)
- One blank line between functions (black handles this)

### Dependencies
- Prefer standard libraries when possible
- Use well-established packages (pandas, numpy, scipy, matplotlib)
- Document all dependencies in `requirements.txt`

### File Management
- Use `Path.mkdir(parents=True, exist_ok=True)` for directory creation
- Check file existence before operations when necessary
- Use relative paths from PROJECT_ROOT

## Academic Context

### Task-Oriented Development
- Each function/module maps to a specific assignment task
- Preserve traceability between code and task requirements
- Document which assignment section each analysis addresses

### Reproducibility
- Use RANDOM_SEED from config for any randomized operations
- Document data transformations clearly
- Save intermediate outputs for verification

### Documentation
- LaTeX comments with TODOs mark unfinished sections
- Python comments explain statistical reasoning
- README provides high-level task overview in German

## Pre-commit Integration
The project uses pre-commit hooks that automatically run:
1. **black** - reformats code
2. **isort** - sorts imports
3. **ruff** - lints and auto-fixes issues

This ensures consistency without manual intervention.
