# Codebase Structure

## Directory Layout

```
statistik-workbook/
├── .git/                   # Git repository
├── .serena/               # Serena memory files
├── .claude/               # Claude Code configuration
├── data/
│   ├── raw/               # Original ALLBUS data (Excel files, PDFs)
│   └── processed/         # Cleaned/processed CSV files
├── docs/                  # Task specifications and documentation
├── figures/               # Generated plots and visualizations (output)
├── latex/
│   ├── main.tex          # Master LaTeX document
│   ├── main.bib          # Bibliography
│   ├── main.pdf          # Compiled PDF output
│   ├── sections/         # Modular LaTeX content sections
│   └── tables/           # Auto-generated tables from Python (.tex files)
├── reports/              # Analysis reports (if any)
├── src/                  # Python source code
│   ├── config.py         # Central configuration (paths, constants)
│   ├── data_prep.py      # Data loading and preprocessing
│   ├── block1_univariat.py     # Task 1b-1d: Univariate analysis
│   ├── block2_bivariat.py      # Task 2a-2c: Bivariate analysis
│   ├── block3_tests.py         # Task 3: Hypothesis tests
│   ├── block4_regression.py    # Task 4: Regression analysis
│   ├── block5_anova.py         # Task 5: ANOVA
│   └── run_all.py        # Master script to run all analyses
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── README.md
└── requirements.txt
```

## Key Files

### Python Source (`src/`)
- **config.py**: Defines project paths (DATA_RAW, DATA_PROCESSED, FIGURES_DIR, TABLES_DIR), RANDOM_SEED, and utility function `ensure_directories()`
- **data_prep.py**: Loads raw Excel data, performs initial cleaning, saves to CSV
- **block1-5 scripts**: Each contains analysis functions for specific assignment tasks
- **run_all.py**: Orchestrates the complete analysis pipeline

### LaTeX (`latex/`)
- **main.tex**: Master document with preamble, formatting (Arial font, APA7 style), and structure
- **sections/**: 10 modular .tex files for different workbook sections (00_frontmatter through 09_fazit)
- **tables/**: Python scripts export statistical tables here as .tex files for inclusion

### Data Flow
1. Raw data in `data/raw/` (Excel format)
2. Python scripts process → `data/processed/` (CSV)
3. Analysis generates → `figures/` (plots) and `latex/tables/` (tables)
4. LaTeX compiles everything into `latex/main.pdf`

## Module Dependencies
- All block scripts import from `config.py`
- `run_all.py` imports and calls main() from other modules
- Modular design allows running blocks independently or together
