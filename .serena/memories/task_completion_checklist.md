# Task Completion Checklist

When completing a development task on this project, follow these steps:

## 1. Code Quality Checks

### Format Code
Run formatters to ensure consistent style:
```bash
black .
isort .
```

### Lint Code
Check for code quality issues:
```bash
ruff check --fix .
```

### Pre-commit Hooks (Optional but Recommended)
If pre-commit is installed, run all hooks:
```bash
pre-commit run --all-files
```

## 2. Functional Testing

### Test Individual Changes
If you modified a specific block, test it:
```bash
python src/block1_univariat.py  # or whichever block you changed
```

### Test Full Pipeline
Verify the complete workflow still works:
```bash
python src/run_all.py
```

## 3. Output Verification

### Check Generated Files
- Verify figures in `figures/` look correct
- Check tables in `latex/tables/` have proper formatting
- Ensure processed data in `data/processed/` is valid

### LaTeX Compilation
If you changed anything affecting the final document:
```bash
cd latex
lualatex main.tex
lualatex main.tex  # Run twice for TOC/references
cd ..
```
Verify `latex/main.pdf` compiles without errors.

## 4. Git Workflow

### Stage Changes
```bash
git add .
```

### Commit with Descriptive Message
```bash
git commit -m "feat: descriptive message about changes"
# or
git commit -m "fix: description of bug fix"
# or
git commit -m "doc: documentation update"
```

### Push to Remote (if applicable)
```bash
git push
```

## 5. Documentation Updates

### Update README (if needed)
- If you added new dependencies → update requirements.txt
- If you changed workflow → update README.md
- If you added new analysis blocks → document in README

### Update Comments
- Ensure German comments explain new/modified code
- Add docstrings to new functions

## Quick Checklist

- [ ] Code formatted (black, isort)
- [ ] Code linted (ruff)
- [ ] Individual module tested
- [ ] Full pipeline runs successfully
- [ ] Generated outputs verified (figures, tables)
- [ ] LaTeX compiles without errors (if applicable)
- [ ] Changes committed with clear message
- [ ] Documentation updated (if needed)

## Notes

- **No formal testing framework**: This project doesn't use pytest/unittest, so manual testing of scripts is necessary
- **Language**: Remember to use German for comments and docstrings
- **Pre-commit**: The pre-commit hooks will run black, isort, and ruff automatically on git commit if installed
