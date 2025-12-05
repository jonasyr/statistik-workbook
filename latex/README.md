# LaTeX Structure

This workbook uses a **modular LaTeX structure** to keep content organized and maintainable.

## File Structure

```
latex/
├── main.tex                    # Master document (preamble, formatting, structure)
├── sections/                   # Individual content sections
│   ├── 00_frontmatter.tex     # Erklärung, Danksagung, Abstracts
│   ├── 01_einleitung.tex      # Introduction & context
│   ├── 02_daten.tex           # Data description (ALLBUS overview)
│   ├── 03_block1_univariat.tex     # Tasks 1b-1d: Univariate analysis
│   ├── 04_block2_bivariat.tex      # Tasks 2a-2c: Bivariate analysis
│   ├── 05_block3_tests.tex         # Task 3: Confidence intervals & t-tests
│   ├── 06_block4_regression.tex    # Task 4: Correlation & regression
│   ├── 07_block5_anova.tex         # Task 5: ANOVA
│   ├── 08_diskussion.tex           # Discussion & reflection
│   └── 09_fazit.tex                # Conclusion
└── tables/                     # Auto-generated tables from Python
    └── (Python scripts export .tex tables here)
```

## Workflow

1. **Edit content**: Open individual section files in `sections/`
2. **Generate data**: Run Python scripts in `src/` to create tables/figures
3. **Compile**: Compile `main.tex` with LuaLaTeX

## Compilation

### VS Code with LaTeX Workshop
The LaTeX Workshop extension will automatically compile when you save `main.tex`.

### Manual Compilation
```bash
cd latex
lualatex main.tex
lualatex main.tex  # Run twice for TOC and references
```

### With Bibliography (when ready)
```bash
lualatex main.tex
biber main
lualatex main.tex
lualatex main.tex
```

## Key Features

- **All formatting preserved**: Arial font, APA7 style, spacing, etc.
- **Modular sections**: Each major block is in its own file
- **Python integration**: Tables and figures auto-generated
- **TODO markers**: Search for `TODO` to find placeholders
- **Clean main.tex**: Only structure and formatting, no content

## Editing Tips

### Adding Python-generated tables
In section files, use:
```latex
% \input{tables/table_name.tex}
```

Uncomment when Python script has generated the table.

### Adding figures
```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.85\textwidth]{../figures/block1/plot_name.pdf}
    \caption{Your caption here.}
    \source{Eigene Darstellung auf Basis ALLBUS 2021.}
    \label{fig:unique_label}
\end{figure}
```

### Updating metadata
Edit these lines in `main.tex`:
```latex
\newcommand{\authorname}{Vorname Nachname}  % TODO: Anpassen
\newcommand{\matno}{Matrikelnummer}         % TODO: Anpassen
\newcommand{\address}{Straße Hausnr., PLZ Ort}  % TODO: Anpassen
\newcommand{\submissiondate}{TT.MM.JJJJ}   % TODO: Anpassen
```

## Backup

Original template backup: `main.tex.backup`
