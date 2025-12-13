# Suggested Commands

## Python Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running Analyses

### Data Preparation
```bash
# Process raw data into cleaned CSV
python src/data_prep.py
```

### Run Complete Pipeline
```bash
# Run all analysis blocks in sequence
python src/run_all.py
```

### Run Individual Blocks
```bash
# Run specific analysis blocks
python src/block1_univariat.py
python src/block2_bivariat.py
python src/block3_tests.py
python src/block4_regression.py
python src/block5_anova.py
```

### Configuration Check
```bash
# Verify paths and create necessary directories
python src/config.py
```

## Code Quality Tools

### Formatting
```bash
# Format all Python files with black
black .

# Sort imports with isort
isort .

# Run both formatters
black . && isort .
```

### Linting
```bash
# Check code with ruff (no changes)
ruff check .

# Check and auto-fix issues
ruff check --fix .
```

### Pre-commit Hooks
```bash
# Install pre-commit hooks (one-time setup)
pre-commit install

# Run hooks on all files manually
pre-commit run --all-files

# Run hooks on staged files only
pre-commit run
```

## LaTeX Compilation

### Change to LaTeX directory
```bash
cd latex
```

### Compile Document
```bash
# Basic compilation (run twice for TOC)
lualatex main.tex
lualatex main.tex

# With bibliography
lualatex main.tex
biber main
lualatex main.tex
lualatex main.tex

# Return to project root
cd ..
```

## Git Operations
```bash
# Standard git workflow
git status
git add .
git commit -m "descriptive message"
git push

# View recent commits
git log --oneline -5

# Check current branch
git branch
```

## File System (Linux)
```bash
# List files
ls -la

# Navigate
cd <directory>
cd ..  # parent directory

# Find files
find . -name "*.py"

# Search in files
grep -r "search_term" src/

# View file
cat filename
less filename  # for long files
```

## Useful Combinations

### After making code changes
```bash
# Format, lint, and check quality
black . && isort . && ruff check --fix .
```

### Complete workflow
```bash
# 1. Ensure environment is ready
python src/config.py

# 2. Process data
python src/data_prep.py

# 3. Run analyses
python src/run_all.py

# 4. Compile LaTeX
cd latex && lualatex main.tex && lualatex main.tex && cd ..
```
