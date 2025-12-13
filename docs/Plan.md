# Complete Execution Plan: Statistics Workbook WiSe 2025

## Project Overview

**Objective:** Complete a statistical analysis workbook based on ALLBUS 2021 survey data, demonstrating proficiency in univariate and bivariate descriptive statistics, inferential statistics, correlation/regression analysis, and ANOVA.

**Deliverables:**
1. Single PDF workbook (10-20 pages main content)
2. Python source files (sent via email)
3. All analyses reproducible and scientifically documented

**Source of Truth:** DS-Statistik2025WiSe-VC_Workbook_Aufgaben_OL_2025-11-03.pdf

**Assigned Variables:**
- Block 1: `mc04` (nominal), `ep04` (ordinal), `hhinc` (metric)
- Block 2a: `ep01`, `fe14` (both ordinal)
- Block 2b-c: `xt10`, `age` (both metric)
- Block 3: `lm02` (metric)
- Block 4: `age`, `hhinc` (both metric)
- Block 5: `hs01` (ordinal), `gd02` (metric)

---

## Phase 1: Foundation & Data Preparation

### 1.1 Update LaTeX Metadata - DONE
**Why:** Personalize the document with student information before starting content work.

**What to do:**
1. Open main.tex
2. Find and update the following lines:
   ```latex
   \newcommand{\authorname}{Vorname Nachname}  % Your full name
   \newcommand{\matno}{Matrikelnummer}         % Your matriculation number
   \newcommand{\address}{Straße Hausnr., PLZ Ort}  % Your address
   \newcommand{\submissiondate}{TT.MM.JJJJ}   % Submission date
   ```
3. Save the file

**Output:** Personalized LaTeX template ready for compilation

---

### 1.2 Implement Comprehensive Data Cleaning
**Why:** Create a clean, analysis-ready dataset with proper handling of missing values and data types. This is the foundation for all subsequent analyses.

**What to do in data_prep.py:**

1. **Load raw data:**
   ```python
   # Load full dataset
   df = pd.read_excel('data/raw/VERSION_2025-11-19_..._ALLBUS_..._Teildatensatz-aus-2021-nur-29-Variablen.xlsx')
   ```

2. **Select relevant variables:**
   ```python
   # All variables needed across all blocks
   needed_vars = [
       'mc04', 'ep01', 'ep04', 'fe14', 'xt10', 'age', 
       'lm02', 'hhinc', 'hs01', 'gd02', 'sex'
   ]
   df = df[needed_vars]
   ```

3. **Handle missing values systematically:**
   - Document missing value counts for Task 1a
   - For metric variables (`hhinc`, `lm02`, `gd02`, `xt10`, `age`): 
     - Negative values and special codes (e.g., -99, -42) → NaN
   - For ordinal/nominal variables:
     - Document category structure
     - Keep as categorical or convert to labeled integers
   
4. **Special transformations:**
   ```python
   # gd02: "Unter 1 Jahr" (coded as string or special value) → 0
   # Document this transformation clearly
   
   # Ensure numeric types
   numeric_vars = ['hhinc', 'lm02', 'gd02', 'xt10', 'age']
   for var in numeric_vars:
       df[var] = pd.to_numeric(df[var], errors='coerce')
   ```

5. **Create summary statistics for Task 1a:**
   ```python
   # Calculate:
   # - Total sample size (n)
   # - Missing counts per variable
   # - Variable types
   # Export summary table to latex/tables/data_overview.tex
   ```

6. **Save cleaned dataset:**
   ```python
   df.to_csv('data/processed/allbus_clean.csv', index=False)
   ```

**Expected output:**
- `data/processed/allbus_clean.csv` (clean dataset)
- `latex/tables/data_overview.tex` (summary statistics table)
- Console output documenting cleaning steps

**Validation:** Run and verify CSV has expected variables and reasonable values.

---

### 1.3 Write LaTeX Section: Dataset Description (Task 1a)
**Why:** Fulfill requirement to describe the entire dataset and establish context for all analyses.

**What to do in 02_daten.tex:**

1. **Introduction (2-3 paragraphs):**
   - ALLBUS background (German General Social Survey)
   - Survey year: 2021
   - Population: German-speaking residents aged 18+ in Germany
   - Sampling method: multi-stage probability sample
   - Citation: Proper reference to ALLBUS documentation

2. **Sample size (Task 1a-i):**
   - State total n from `data_overview.tex`
   - "Der vorliegende Workbook-Datensatz umfasst n = XXX Fälle."

3. **Missing values strategy (Task 1a-ii):**
   - Report missing counts per variable (table from `data_overview.tex`)
   - Explain strategy: "Für metrische Variablen wurden negative Kodierungen und Spezialwerte als fehlend behandelt (NaN). Bei den Analysen erfolgt listenweiser Fallausschluss (complete case analysis) für die jeweils betrachteten Variablen, um Verzerrungen zu minimieren."
   - Justify: No imputation due to manageable missing rates and workbook scope

4. **Measurement levels overview (Task 1a-iii):**
   - Create table listing all 29 variables with:
     - Variable name
     - Short description
     - Measurement level (nominal/ordinal/metric)
     - Brief justification
   - Example row: `age | Alter in Jahren | metrisch | natürliche Ordnung mit gleichabständigen Einheiten`

5. **Variable assignment (Task 1a-iv):**
   - Include screenshot of `Zuteilung_OL_2025Q4.csv` with your matriculation number
   - Create table listing your assigned variables by block:
     ```latex
     \begin{table}[h]
     \caption{Zugeteilte Variablen für die Aufgabenblöcke}
     \begin{tabular}{lll}
     Block & Aufgabe & Variablen \\
     \hline
     1 & Univariat & mc04 (nominal), ep04 (ordinal), hhinc (metrisch) \\
     2a & Bivariat ordinal & ep01, fe14 \\
     ...
     \end{tabular}
     \end{table}
     ```

**Expected output:** Complete Section 2 (3-4 pages) with all Task 1a requirements fulfilled

**Citation needed:** Add ALLBUS reference to bibliography (main.bib)

---

## Phase 2: Block 1 - Univariate Descriptive Statistics (Tasks 1b-1d)

### 2.1 Implement Block 1 Python Analysis
**Why:** Generate all statistical outputs and visualizations for univariate analyses.

**What to do in block1_univariat.py:**

#### **Task 1b Analysis: Measurement Levels**
*No computational output needed - this is theoretical explanation in LaTeX*

#### **Task 1c Analysis: `ep04` (ordinal)**

```python
# 1. Load clean data
df = pd.read_csv('data/processed/allbus_clean.csv')

# 2. Frequency table for ep04
ep04_freq = df['ep04'].value_counts(dropna=False).sort_index()
ep04_rel = df['ep04'].value_counts(dropna=False, normalize=True).sort_index()

# Combine into table
freq_table = pd.DataFrame({
    'Kategorie': ep04_freq.index,
    'Absolute Häufigkeit': ep04_freq.values,
    'Relative Häufigkeit': ep04_rel.values
})

# 3. Export to LaTeX
freq_table.to_latex(
    'latex/tables/ep04_frequencies.tex',
    index=False,
    float_format='%.3f',
    caption='Häufigkeitsverteilung ep04: Wirtschaftliche Lage in einem Jahr',
    label='tab:ep04_freq'
)

# 4. Calculate mode and median
mode_ep04 = df['ep04'].mode()[0]
median_ep04 = df['ep04'].median()
# Save to separate table or text file for LaTeX inclusion

# 5. Create bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ep04_freq.plot(kind='bar', ax=ax)
ax.set_xlabel('Einschätzung der wirtschaftlichen Lage')
ax.set_ylabel('Absolute Häufigkeit')
ax.set_title('Verteilung: Wirtschaftliche Lage Deutschlands in einem Jahr')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('figures/block1/ep04_distribution.pdf', bbox_inches='tight')
plt.close()
```

**Why bar chart:** Ordinal data has natural order but unequal intervals; bar chart preserves order while showing discrete categories.

#### **Task 1d Analysis: `hhinc` (metric)**

```python
# 1. Define income classes (justify choice in LaTeX)
bins = [0, 1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, np.inf]
labels = ['0-1k', '1-2k', '2-3k', '3-4k', '4-5k', '5-6k', '6-8k', '8-10k', '>10k']

# 2. Create class variable
df_hhinc = df['hhinc'].dropna()
hhinc_classes = pd.cut(df_hhinc, bins=bins, labels=labels)

# 3. Frequency table
hhinc_freq = hhinc_classes.value_counts().sort_index()
hhinc_rel = hhinc_classes.value_counts(normalize=True).sort_index()

class_table = pd.DataFrame({
    'Einkommensklasse (€)': hhinc_freq.index,
    'Absolute Häufigkeit': hhinc_freq.values,
    'Relative Häufigkeit': hhinc_rel.values,
    'Klassenmitte': [500, 1500, 2500, 3500, 4500, 5500, 7000, 9000, 11000]  # approximate
})

class_table.to_latex('latex/tables/hhinc_classes.tex', ...)

# 4. Calculate descriptive statistics
stats = {
    'Mittelwert': df_hhinc.mean(),
    'Standardabweichung': df_hhinc.std(),
    'Median': df_hhinc.median(),
    'Min': df_hhinc.min(),
    'Max': df_hhinc.max(),
    'n': len(df_hhinc)
}
stats_df = pd.DataFrame([stats])
stats_df.to_latex('latex/tables/hhinc_statistics.tex', ...)

# 5. Create histogram
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df_hhinc, bins=bins[:-1] + [df_hhinc.max()], edgecolor='black')
ax.set_xlabel('Haushaltsnettoeinkommen (€)')
ax.set_ylabel('Absolute Häufigkeit')
ax.set_title('Verteilung des Haushaltsnettoeinkommens')
plt.tight_layout()
plt.savefig('figures/block1/hhinc_histogram.pdf', bbox_inches='tight')
plt.close()

# 6. Also create frequency density version
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df_hhinc, bins=bins[:-1] + [df_hhinc.max()], 
        density=True, edgecolor='black')
ax.set_xlabel('Haushaltsnettoeinkommen (€)')
ax.set_ylabel('Häufigkeitsdichte')
ax.set_title('Verteilung des Haushaltsnettoeinkommens (Dichte)')
plt.tight_layout()
plt.savefig('figures/block1/hhinc_histogram_density.pdf', bbox_inches='tight')
plt.close()
```

**Why this matters:** Task requires discussing when frequency density is important (when class widths differ - visible in the ">10k" class).

**Expected outputs:**
- `latex/tables/ep04_frequencies.tex`
- `latex/tables/ep04_statistics.tex` (mode, median)
- `latex/tables/hhinc_classes.tex`
- `latex/tables/hhinc_statistics.tex`
- `figures/block1/ep04_distribution.pdf`
- `figures/block1/hhinc_histogram.pdf`
- `figures/block1/hhinc_histogram_density.pdf`

---

### 2.2 Write LaTeX Section: Block 1 Interpretation
**Why:** Fulfill all interpretation requirements and demonstrate understanding of measurement levels.

**What to do in 03_block1_univariat.tex:**

#### **Task 1b: Measurement Levels (1.5-2 pages)**

Write detailed explanation structured as:

1. **Nominal scale definition:**
   - Categories without natural order
   - Only equality/inequality comparisons possible
   - Example: `mc04` (foreigners in friend circle)
   - Appropriate statistics: Mode, frequencies
   - Appropriate visualizations: Bar/pie charts
   - Inappropriate: Mean, SD (meaningless)

2. **Ordinal scale definition:**
   - Categories with natural order but unequal intervals
   - Rank comparisons possible
   - Example: `ep04` (economic situation rating: wesentlich besser ... wesentlich schlechter)
   - Why ordinal: "besser" > "schlechter", but distance between "etwas besser" and "wesentlich besser" may differ from distance between other categories
   - Appropriate statistics: Mode, median, percentiles
   - Appropriate visualizations: Ordered bar charts
   - Inappropriate: Mean (assumes equal intervals)

3. **Metric scale definition:**
   - Numeric values with meaningful intervals and zero point (ratio scale)
   - All arithmetic operations meaningful
   - Example: `hhinc` (income in euros)
   - Why metric: €2000 - €1000 = €1000 has same meaning as €4000 - €3000
   - Appropriate statistics: All (mean, SD, variance, etc.)
   - Appropriate visualizations: Histograms, boxplots, scatter plots
   - Full range of parametric tests available

4. **Implications for analysis:**
   - Measurement level determines permissible operations
   - Using inappropriate methods yields meaningless results
   - Example: Mean of `ep04` (coding 1-5) is numerically possible but conceptually flawed

**Citation:** Reference course materials/textbook for measurement theory.

#### **Task 1c: `ep04` Analysis (1-1.5 pages)**

1. **Method description:**
   - "Für die ordinale Variable `ep04` wurde eine Häufigkeitstabelle erstellt..."
   - Brief Python/Excel workflow (1-2 sentences + optional screenshot)

2. **Present results:**
   - Include table: `\input{tables/ep04_frequencies.tex}`
   - Include figure: `\includegraphics[width=0.85\textwidth]{../figures/block1/ep04_distribution.pdf}`

3. **Report statistics:**
   - Modus: [value] (most frequent category)
   - Median: [value] (middle category when ordered)
   - Why these are appropriate for ordinal data

4. **Interpretation (2-3 paragraphs):**
   - What does the distribution show?
   - Is there a tendency toward optimism or pessimism about economic future?
   - How concentrated vs. spread is the distribution?
   - What does the median tell us about the "typical" respondent?
   - Any surprising findings?

5. **Visualization justification:**
   - "Ein Balkendiagramm wurde gewählt, weil es die natürliche Ordnung der Kategorien bewahrt und die Häufigkeiten klar darstellt. Ein Kreisdiagramm wäre weniger geeignet, da die Ordnung verloren ginge."

#### **Task 1d: `hhinc` Analysis (2-2.5 pages)**

1. **Class formation justification:**
   - "Für die metrische Variable `hhinc` wurden Einkommensklassen gebildet, um..."
   - Explain choice of bin widths (e.g., €1000 intervals up to €6000, then wider for sparse high incomes)
   - Why unequal widths make sense (few very high earners)

2. **Present results:**
   - Include class frequency table: `\input{tables/hhinc_classes.tex}`
   - Include statistics table: `\input{tables/hhinc_statistics.tex}`
   - Include histogram: `\includegraphics{../figures/block1/hhinc_histogram.pdf}`

3. **Histogram discussion:**
   - "Bei ungleichen Klassenbreiten ist die Häufigkeitsdichte auf der y-Achse essenziell, um visuelle Verzerrungen zu vermeiden..."
   - Compare frequency vs. density versions
   - When is density critical? When class widths vary (as in your open-ended top class)
   - When is it less critical? Equal-width classes

4. **Interpretation of descriptive statistics (3-4 paragraphs):**
   - Mean: €[X] - "Das durchschnittliche Haushaltsnettoeinkommen beträgt..."
   - SD: €[Y] - measure of spread
   - Median: €[Z] - robust to outliers
   - Compare mean vs. median: If mean > median, positive skew (few very high earners pull mean up)
   - Distribution shape: Right-skewed typical for income data
   - Outliers: Discuss if present
   - Practical meaning: What does this tell us about German household incomes?

5. **Method note:**
   - Brief description of Python/Excel approach (1-2 sentences)
   - Optional: Screenshot showing calculation

**Expected output:** Complete Section 3 (4-6 pages total for Block 1)

---

## Phase 3: Block 2 - Bivariate Descriptive Statistics (Tasks 2a-2c)

### 3.1 Implement Block 2a Python Analysis: Ordinal × Ordinal
**Why:** Analyze relationship between two ordinal variables using appropriate methods.

**What to do in block2_bivariat.py:**

```python
# Task 2a: ep01 × fe14 (both ordinal)

# 1. Load data
df = pd.read_csv('data/processed/allbus_clean.csv')
df_clean = df[['ep01', 'fe14']].dropna()

# 2. Create contingency table
crosstab = pd.crosstab(
    df_clean['ep01'], 
    df_clean['fe14'],
    margins=True,
    margins_name='Gesamt'
)

# Export absolute frequencies
crosstab.to_latex(
    'latex/tables/ep01_fe14_crosstab_abs.tex',
    caption='Kontingenztabelle: ep01 × fe14 (absolute Häufigkeiten)',
    label='tab:ep01_fe14_abs'
)

# 3. Relative frequencies (row percentages, column percentages, total percentages)
crosstab_row_pct = pd.crosstab(
    df_clean['ep01'], 
    df_clean['fe14'],
    normalize='index'  # row percentages
) * 100

crosstab_row_pct.to_latex(
    'latex/tables/ep01_fe14_crosstab_row.tex',
    caption='Kontingenztabelle: ep01 × fe14 (Zeilenprozente)',
    float_format='%.1f'
)

# 4. Calculate Spearman rank correlation
# Need to convert categorical to numeric if not already
from scipy.stats import spearmanr

# If variables are categorical, convert to ordered numeric
# Example: ep01 might be coded 1="SEHR GUT", 2="GUT", etc.
# Ensure proper ordering before correlation

spearman_corr, spearman_p = spearmanr(df_clean['ep01'], df_clean['fe14'])

corr_results = pd.DataFrame({
    'Zusammenhangsmaß': ['Spearman-Rangkorrelation'],
    'Wert': [spearman_corr],
    'p-Wert': [spearman_p],
    'n': [len(df_clean)]
})

corr_results.to_latex('latex/tables/ep01_fe14_spearman.tex', ...)

# 5. Create mosaic plot (requires statsmodels or manual implementation)
from statsmodels.graphics.mosaicplot import mosaic

fig, ax = plt.subplots(figsize=(12, 8))
mosaic(df_clean, ['ep01', 'fe14'], ax=ax, title='Mosaikdiagramm: ep01 × fe14')
plt.tight_layout()
plt.savefig('figures/block2/ep01_fe14_mosaic.pdf', bbox_inches='tight')
plt.close()

# Alternative if too many categories: Group categories first
# Example: Combine "SEHR GUT" + "GUT" → "POSITIV", etc.
```

**Important considerations:**
- If too many category combinations, group similar categories first
- Ensure ordinal variables are properly coded for Spearman correlation
- Mosaic plot dimensions: readable labels

**Expected outputs:**
- `latex/tables/ep01_fe14_crosstab_abs.tex`
- `latex/tables/ep01_fe14_crosstab_row.tex`
- `latex/tables/ep01_fe14_spearman.tex`
- `figures/block2/ep01_fe14_mosaic.pdf`

---

### 3.2 Implement Block 2b Python Analysis: Metric × Metric
**Why:** Analyze linear relationship between two metric variables.

**What to do (continue in block2_bivariat.py):**

```python
# Task 2b: xt10 × age (both metric)

# 1. Load and clean data
df_metric = df[['xt10', 'age']].dropna()

# 2. Create scatter plot
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(df_metric['age'], df_metric['xt10'], alpha=0.5, s=30)
ax.set_xlabel('Alter (Jahre)')
ax.set_ylabel('Interviewdauer (Minuten)')
ax.set_title('Streudiagramm: Alter und Interviewdauer')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figures/block2/xt10_age_scatter.pdf', bbox_inches='tight')
plt.close()

# 3. Calculate Pearson correlation
from scipy.stats import pearsonr

pearson_corr, pearson_p = pearsonr(df_metric['age'], df_metric['xt10'])

# 4. Also calculate manually to show formula understanding
mean_age = df_metric['age'].mean()
mean_xt10 = df_metric['xt10'].mean()

# Covariance
cov = ((df_metric['age'] - mean_age) * (df_metric['xt10'] - mean_xt10)).sum() / (len(df_metric) - 1)

# Standard deviations
sd_age = df_metric['age'].std()
sd_xt10 = df_metric['xt10'].std()

# Correlation
r_manual = cov / (sd_age * sd_xt10)

# 5. Export results
corr_table = pd.DataFrame({
    'Statistik': ['Pearson r', 'p-Wert', 'n', 'Mittelwert Alter', 'Mittelwert xt10', 'SD Alter', 'SD xt10'],
    'Wert': [pearson_corr, pearson_p, len(df_metric), mean_age, mean_xt10, sd_age, sd_xt10]
})

corr_table.to_latex('latex/tables/xt10_age_correlation.tex', ...)
```

**Expected outputs:**
- `latex/tables/xt10_age_correlation.tex`
- `figures/block2/xt10_age_scatter.pdf`

---

### 3.3 Write LaTeX Section: Block 2 Interpretation
**Why:** Fulfill all bivariate analysis requirements including theoretical discussions.

**What to do in 04_block2_bivariat.tex:**

#### **Task 2a: Ordinal × Ordinal (2-2.5 pages)**

1. **Introduction:**
   - "Um den Zusammenhang zwischen der aktuellen Wirtschaftseinschätzung (`ep01`) und dem Erziehungsziel 'beliebt sein' (`fe14`) zu untersuchen..."

2. **Method selection justification:**
   - Why contingency table? Shows joint distribution
   - Why Spearman? Both variables ordinal, measures monotonic relationship
   - Why not Pearson? Assumes metric data with linear relationship
   - Why not Phi/Cramér's V? Appropriate, but Spearman better captures ordered nature

3. **Present results:**
   - Include tables: `\input{tables/ep01_fe14_crosstab_abs.tex}` and row percentage version
   - Include figure: `\includegraphics{../figures/block2/ep01_fe14_mosaic.pdf}`

4. **Interpretation (2-3 paragraphs):**
   - Describe contingency table patterns: Are certain combinations more common?
   - Mosaic plot interpretation: Visual assessment of independence
   - Spearman correlation: ρ = [value]
     - Direction: Positive (both increase together) or negative (inverse)?
     - Strength: |ρ| < 0.3 weak, 0.3-0.7 moderate, > 0.7 strong
     - Significance: p < 0.05? Can we generalize to population?
   - Substantive interpretation: What does this tell us about the relationship between economic outlook and parenting values?

#### **Task 2b: Metric × Metric (1.5-2 pages)**

1. **Pearson correlation explanation:**
   - "Der Korrelationskoeffizient nach Bravais-Pearson misst die Stärke und Richtung eines *linearen* Zusammenhangs..."
   - Formula: $r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2}}$
   - Or: $r = \frac{Cov(X,Y)}{SD_X \cdot SD_Y}$
   - Properties: -1 ≤ r ≤ 1
   - r = 1: perfect positive linear
   - r = -1: perfect negative linear
   - r = 0: no linear relationship (but non-linear could exist!)

2. **Calculation demonstration:**
   - Show step-by-step calculation using your data (or reference output table)
   - "Für Alter ($\bar{x}$ = [mean_age]) und Interviewdauer ($\bar{y}$ = [mean_xt10])..."

3. **Present results:**
   - Include table: `\input{tables/xt10_age_correlation.tex}`
   - Include figure: `\includegraphics{../figures/block2/xt10_age_scatter.pdf}`

4. **Interpretation:**
   - Scatter plot assessment: Does visual pattern suggest linear relationship?
   - Correlation value: r = [value]
   - Compare scatter plot and r: Do they agree?
   - If r ≈ 0: "Das Streudiagramm zeigt keine klare lineare Tendenz, was durch r ≈ 0 bestätigt wird..."
   - Or if r ≠ 0: "Ein [positiver/negativer] Zusammenhang ist sowohl visuell als auch numerisch erkennbar..."

#### **Task 2c: Correlation vs. Causation (1-1.5 pages)**

**This is critical conceptual understanding:**

1. **Definitions:**
   - Correlation: Statistical association between variables
   - Causation: X directly causes change in Y

2. **Example using `xt10` and `age`:**
   - Suppose r = 0.15 (positive correlation)
   - Possible interpretations:
     - **A → B:** Older age causes longer interviews (more life experience to discuss?)
     - **B → A:** Longer interviews cause aging?? (Absurd! Shows limitation)
     - **C → A,B:** Third variable (e.g., health issues cause both older age and longer interviews)
     - **Random chance:** With α = 0.05, 1 in 20 tests show "significance" by chance

3. **Why correlation ≠ causation:**
   - Correlation is symmetric: corr(X,Y) = corr(Y,X)
   - Causation is directional: X causes Y ≠ Y causes X
   - Correlation doesn't account for:
     - Confounding variables
     - Reverse causation
     - Spurious relationships

4. **Conditions for causal inference:**
   - Temporal precedence (cause before effect)
   - Controlled experiments (randomization)
   - Theoretical mechanism
   - Ruling out alternatives
   - Observational data (like ALLBUS) cannot establish causation alone

5. **Example alternative explanations for `xt10` × `age`:**
   - Interviewer assignment (certain interviewers get older respondents and take longer)
   - Cohort effects (generation-specific communication styles)
   - Health/cognitive factors affecting both variables

**Expected output:** Complete Section 4 (4-5 pages total for Block 2)

---

## Phase 4: Block 3 - Inferential Statistics (Tasks 3a-3c)

### 4.1 Implement Block 3 Python Analysis
**Why:** Conduct confidence interval and hypothesis testing for single metric variable.

**What to do in block3_tests.py:**

```python
# Task 3: Inferential statistics with lm02

import scipy.stats as stats

# 1. Load data
df = pd.read_csv('data/processed/allbus_clean.csv')
lm02_data = df['lm02'].dropna()

# Task 3b: 95% Confidence Interval

# Calculate statistics
mean_lm02 = lm02_data.mean()
sd_lm02 = lm02_data.std(ddof=1)  # Sample SD
n_lm02 = len(lm02_data)
se_lm02 = sd_lm02 / np.sqrt(n_lm02)

# t-critical value (two-tailed, α=0.05, df=n-1)
t_crit = stats.t.ppf(0.975, df=n_lm02-1)

# Confidence interval
ci_lower = mean_lm02 - t_crit * se_lm02
ci_upper = mean_lm02 + t_crit * se_lm02

# Alternative: Use scipy
ci = stats.t.interval(0.95, df=n_lm02-1, loc=mean_lm02, scale=se_lm02)

# Export results
ci_table = pd.DataFrame({
    'Statistik': ['Mittelwert', 'Standardabweichung', 'Standardfehler', 'n', 
                  '95% KI untere Grenze', '95% KI obere Grenze'],
    'Wert': [mean_lm02, sd_lm02, se_lm02, n_lm02, ci_lower, ci_upper]
})
ci_table.to_latex('latex/tables/lm02_ci.tex', ...)

# Task 3c: Two-sample t-test (using 'sex' as grouping variable)

# 2. Split by sex
lm02_male = df[df['sex'] == 'MANN']['lm02'].dropna()
lm02_female = df[df['sex'] == 'FRAU']['lm02'].dropna()

# Descriptive statistics by group
desc_stats = pd.DataFrame({
    'Gruppe': ['Männer', 'Frauen'],
    'n': [len(lm02_male), len(lm02_female)],
    'Mittelwert': [lm02_male.mean(), lm02_female.mean()],
    'SD': [lm02_male.std(), lm02_female.std()],
    'SE': [lm02_male.std()/np.sqrt(len(lm02_male)), 
           lm02_female.std()/np.sqrt(len(lm02_female))]
})
desc_stats.to_latex('latex/tables/lm02_by_sex.tex', ...)

# 3. Conduct two-sample t-test
# Default: two-sided, assumes unequal variances (Welch's t-test)
t_stat, p_value = stats.ttest_ind(lm02_male, lm02_female, equal_var=False)

# Also get degrees of freedom (Welch-Satterthwaite)
# Manual calculation or use alternative method

# 4. Export test results
ttest_results = pd.DataFrame({
    'Test': ['Welch-t-Test (zweiseitig)'],
    't-Wert': [t_stat],
    'p-Wert': [p_value],
    'Signifikant (α=0.05)': ['Ja' if p_value < 0.05 else 'Nein']
})
ttest_results.to_latex('latex/tables/lm02_ttest.tex', ...)
```

**Expected outputs:**
- `latex/tables/lm02_ci.tex`
- `latex/tables/lm02_by_sex.tex`
- `latex/tables/lm02_ttest.tex`

---

### 4.2 Write LaTeX Section: Block 3 Interpretation
**Why:** Demonstrate understanding of inferential concepts and proper interpretation.

**What to do in 05_block3_tests.tex:**

#### **Task 3a: Population vs. Sample (1 page)**

1. **Define population:**
   - "Die Grundgesamtheit der ALLBUS-Umfrage besteht aus allen in Deutschland lebenden, deutschsprachigen Personen ab 18 Jahren in Privathaushalten."
   - Cite ALLBUS documentation for exact definition
   - Size: ~65-70 million people

2. **Define sample:**
   - "Die Stichprobe umfasst die tatsächlich befragten n = [X] Personen."
   - Sampling method: Probability sample (multi-stage)
   - Goal: Representative of population

3. **Inferential statistics purpose:**
   - Sample statistics (e.g., $\bar{x}$) estimate population parameters (μ)
   - Uncertainty quantified via standard errors, confidence intervals, p-values
   - "Mithilfe inferenzstatistischer Methoden können wir von der Stichprobe auf die Grundgesamtheit schließen..."

#### **Task 3b: Confidence Interval (1.5 pages)**

1. **Method description:**
   - "Für die Variable `lm02` (tägliche Fernsehdauer in Minuten) wurde ein 95%-Konfidenzintervall um den Mittelwert berechnet..."
   - Formula: $\bar{x} \pm t_{n-1, 0.975} \cdot SE$ where $SE = \frac{s}{\sqrt{n}}$

2. **Present results:**
   - Include table: `\input{tables/lm02_ci.tex}`
   - "Der Stichprobenmittelwert beträgt $\bar{x}$ = [X] Minuten (SD = [Y] Min, n = [Z])."
   - "Das 95%-KI erstreckt sich von [lower] bis [upper] Minuten."

3. **Correct interpretation (CRITICAL):**
   - ✅ **CORRECT:** "Würden wir die Stichprobenziehung 100-mal wiederholen und jedes Mal ein 95%-KI berechnen, würden etwa 95 dieser Intervalle den wahren Populationsmittelwert μ enthalten."
   - ❌ **WRONG:** "Mit 95% Wahrscheinlichkeit liegt der wahre Wert zwischen [lower] und [upper]." (The true value is fixed; the interval is random!)
   - ❌ **WRONG:** "95% der Personen schauen zwischen [lower] und [upper] Minuten fern." (This confuses CI with data spread!)

4. **Substantive interpretation:**
   - "Basierend auf diesem Intervall können wir mit 95% Konfidenz schätzen, dass die durchschnittliche tägliche Fernsehdauer in der deutschen Bevölkerung zwischen [X] und [Y] Minuten liegt."

#### **Task 3c: Two-Sample t-Test (2 pages)**

1. **Hypothesis formulation:**
   - Research question: "Unterscheidet sich die durchschnittliche Fernsehdauer zwischen Männern und Frauen?"
   - Null hypothesis: H₀: μ_male = μ_female (kein Unterschied)
   - Alternative hypothesis: H₁: μ_male ≠ μ_female (zweiseitig)
   - Significance level: α = 0.05
   - Decision: two-sided test (no directional prediction)

2. **Independence argument:**
   - "Die beiden Stichproben sind unabhängig, weil jede Person genau einer Gruppe angehört (männlich oder weiblich)."
   - "Es gibt keine Paarungen oder wiederholte Messungen an denselben Personen."
   - "Die Antwort einer Person beeinflusst nicht die Antwort einer anderen Person."

3. **Method description:**
   - Welch-t-Test (doesn't assume equal variances)
   - Why Welch instead of Student? More robust, doesn't require homoscedasticity assumption

4. **Present results:**
   - Include tables: `\input{tables/lm02_by_sex.tex}` and `\input{tables/lm02_ttest.tex}`
   - Descriptive comparison: "Männer schauten durchschnittlich [X] Minuten fern (SD=[Y]), Frauen [Z] Minuten (SD=[W])."

5. **Interpretation:**
   - t-value: Magnitude of difference in standard error units
   - p-value: "Der p-Wert beträgt p = [value]."
   - Decision: 
     - If p < 0.05: "H₀ wird verworfen. Es besteht ein signifikanter Unterschied..."
     - If p ≥ 0.05: "H₀ wird nicht verworfen. Kein signifikanter Unterschied nachweisbar..."
   - Effect size: Consider Cohen's d or simply report mean difference in minutes
   - Practical significance: Is the difference meaningful beyond statistical significance?

**Expected output:** Complete Section 5 (4-5 pages total for Block 3)

---

## Phase 5: Block 4 - Regression Analysis (Tasks 4a-4c)

### 5.1 Implement Block 4 Python Analysis
**Why:** Conduct correlation and simple linear regression analysis.

**What to do in block4_regression.py:**

```python
# Block 4: age × hhinc

# 1. Load and clean data
df = pd.read_csv('data/processed/allbus_clean.csv')
df_reg = df[['age', 'hhinc']].dropna()

# Task 4a: Correlation with significance test

from scipy.stats import pearsonr

r, p = pearsonr(df_reg['age'], df_reg['hhinc'])

corr_table = pd.DataFrame({
    'Statistik': ['Pearson r', 'r²', 'p-Wert', 'n', 
                  'Signifikant (α=0.05)'],
    'Wert': [r, r**2, p, len(df_reg), 
             'Ja' if p < 0.05 else 'Nein']
})
corr_table.to_latex('latex/tables/age_hhinc_correlation.tex', ...)

# Task 4b: Scatter plot (will add regression line in 4c)

fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(df_reg['age'], df_reg['hhinc'], alpha=0.5, s=30)
ax.set_xlabel('Alter (Jahre)')
ax.set_ylabel('Haushaltsnettoeinkommen (€)')
ax.set_title('Streudiagramm: Alter und Haushaltseinkommen')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figures/block4/age_hhinc_scatter.pdf', bbox_inches='tight')
plt.close()

# Task 4c: Simple linear regression

import statsmodels.api as sm

# Prepare data: X (age) and y (hhinc)
X = df_reg['age']
y = df_reg['hhinc']

# Add constant for intercept
X_with_const = sm.add_constant(X)

# Fit OLS model
model = sm.OLS(y, X_with_const)
results = model.fit()

# Extract coefficients
intercept = results.params['const']
slope = results.params['age']
r_squared = results.rsquared
r_squared_adj = results.rsquared_adj
f_stat = results.fvalue
f_pvalue = results.f_pvalue

# Get full summary
summary_df = pd.DataFrame({
    'Koeffizient': ['Konstante (β₀)', 'Steigung age (β₁)'],
    'Schätzung': [intercept, slope],
    'Standardfehler': [results.bse['const'], results.bse['age']],
    't-Wert': [results.tvalues['const'], results.tvalues['age']],
    'p-Wert': [results.pvalues['const'], results.pvalues['age']]
})
summary_df.to_latex('latex/tables/age_hhinc_regression_coef.tex', ...)

# Model fit statistics
fit_stats = pd.DataFrame({
    'Statistik': ['R²', 'R² (adjustiert)', 'F-Statistik', 'p-Wert (F)', 'n'],
    'Wert': [r_squared, r_squared_adj, f_stat, f_pvalue, len(df_reg)]
})
fit_stats.to_latex('latex/tables/age_hhinc_regression_fit.tex', ...)

# Example prediction
example_age = 45  # Choose meaningful value within data range
predicted_income = intercept + slope * example_age

pred_df = pd.DataFrame({
    'Beispiel-Alter': [example_age],
    'Vorhergesagtes Einkommen (€)': [predicted_income]
})
pred_df.to_latex('latex/tables/age_hhinc_prediction.tex', ...)

# Create scatter plot with regression line
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(df_reg['age'], df_reg['hhinc'], alpha=0.5, s=30, label='Beobachtungen')

# Add regression line
age_range = np.linspace(df_reg['age'].min(), df_reg['age'].max(), 100)
predicted = intercept + slope * age_range
ax.plot(age_range, predicted, 'r-', linewidth=2, label=f'Regressionsgerade: y = {intercept:.1f} + {slope:.1f}x')

ax.set_xlabel('Alter (Jahre)')
ax.set_ylabel('Haushaltsnettoeinkommen (€)')
ax.set_title(f'Lineare Regression: Einkommen ~ Alter (R² = {r_squared:.3f})')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('figures/block4/age_hhinc_regression.pdf', bbox_inches='tight')
plt.close()
```

**Expected outputs:**
- `latex/tables/age_hhinc_correlation.tex`
- `latex/tables/age_hhinc_regression_coef.tex`
- `latex/tables/age_hhinc_regression_fit.tex`
- `latex/tables/age_hhinc_prediction.tex`
- `figures/block4/age_hhinc_scatter.pdf`
- `figures/block4/age_hhinc_regression.pdf`

---

### 5.2 Write LaTeX Section: Block 4 Interpretation
**Why:** Demonstrate understanding of regression modeling and interpretation.

**What to do in 06_block4_regression.tex:**

#### **Task 4a: Correlation Analysis (1 page)**

1. **Method description:**
   - "Zur Analyse des linearen Zusammenhangs zwischen Alter und Haushaltseinkommen wurde der Pearson-Korrelationskoeffizient berechnet..."
   - Brief Python/Excel workflow

2. **Present results:**
   - Include table: `\input{tables/age_hhinc_correlation.tex}`
   - "Der Korrelationskoeffizient beträgt r = [value]."

3. **Significance test interpretation:**
   - H₀: ρ = 0 (keine Korrelation in der Population)
   - H₁: ρ ≠ 0
   - p-value interpretation
   - Decision: Significant or not?

4. **Substantive interpretation:**
   - Direction: positive/negative?
   - Strength: weak/moderate/strong?
   - Meaning: "Ein [positiver/negativer] [schwacher/moderater/starker] Zusammenhang deutet darauf hin, dass..."

#### **Task 4b: Causal Direction Discussion (1 page)**

1. **Causal assumption:**
   - "Für die Regressionsanalyse wird angenommen, dass Alter (X) einen kausalen Einfluss auf das Haushaltseinkommen (Y) hat."
   - Justification: "Dies ist plausibel, weil mit zunehmendem Alter typischerweise Berufserfahrung und Karrierefortschritt steigen..."
   - Acknowledge limitations: "Diese Annahme ist stark vereinfachend. In Wirklichkeit beeinflussen zahlreiche andere Faktoren (Bildung, Branche, Region, etc.) das Einkommen."

2. **Present scatter plot:**
   - Include figure: `\includegraphics{../figures/block4/age_hhinc_scatter.pdf}`
   - Visual assessment: Does pattern support causal direction?
   - X-axis = presumed cause (age)
   - Y-axis = presumed effect (income)

#### **Task 4c: Linear Regression (2-2.5 pages)**

1. **Method description:**
   - "Eine einfache lineare Regression wurde durchgeführt, um Haushaltseinkommen (Y) als Funktion des Alters (X) zu modellieren..."
   - Model: $\text{hhinc}_i = \beta_0 + \beta_1 \cdot \text{age}_i + \epsilon_i$
   - OLS estimation minimizes sum of squared residuals

2. **Present results:**
   - Include tables: 
     - `\input{tables/age_hhinc_regression_coef.tex}`
     - `\input{tables/age_hhinc_regression_fit.tex}`
   - Include figure: `\includegraphics{../figures/block4/age_hhinc_regression.pdf}`

3. **Regression equation:**
   - "Die geschätzte Regressionsgleichung lautet:"
   - $\widehat{\text{hhinc}} = \beta_0 + \beta_1 \cdot \text{age}$
   - $\widehat{\text{hhinc}} = [intercept] + [slope] \cdot \text{age}$

4. **Coefficient interpretation:**
   - **Intercept (β₀):** "Der y-Achsenabschnitt beträgt β₀ = [value] €. Dies würde das erwartete Einkommen bei Alter = 0 darstellen, was hier nicht sinnvoll interpretierbar ist (außerhalb des Datenbereichs)."
   - **Slope (β₁):** "Die Steigung beträgt β₁ = [value] € pro Jahr. Im Durchschnitt ist ein um ein Jahr höheres Alter mit einem um [value] € höheren Haushaltseinkommen assoziiert."
   - Significance: "Der t-Test zeigt, dass β₁ signifikant von Null verschieden ist (p = [value]), d.h. ein statistisch nachweisbarer Zusammenhang besteht."

5. **R² interpretation:**
   - "Das Bestimmtheitsmaß beträgt R² = [value]."
   - "Dies bedeutet, dass [value*100]% der Varianz im Haushaltseinkommen durch das Alter erklärt werden."
   - Remaining variance: "[100-value*100]% der Varianz sind auf andere Faktoren zurückzuführen."

6. **F-test:**
   - "Der F-Test prüft die Gesamtsignifikanz des Modells (H₀: alle Koeffizienten außer Konstante = 0)."
   - "Mit F = [value], p = [value] ist das Modell signifikant."

7. **Example prediction:**
   - Include table: `\input{tables/age_hhinc_prediction.tex}`
   - "Für eine Person im Alter von [X] Jahren wird ein Haushaltseinkommen von [predicted] € vorhergesagt."
   - Caution: "Diese Vorhersage ist mit Unsicherheit behaftet (Konfidenzintervalle könnten berechnet werden) und gilt nur innerhalb des beobachteten Altersbereichs."

8. **Comparison with scatter plot:**
   - "Die Regressionsgerade im Streudiagramm zeigt die durchschnittliche Beziehung."
   - "Die Streuung der Punkte um die Gerade verdeutlicht die begrenzte Erklärungskraft (R² = [value])."

9. **Limitations:**
   - Cross-sectional data: Cannot infer within-person age effects
   - Cohort effects: Older people may have different incomes due to generation, not age per se
   - Omitted variables: Education, occupation, region, etc.
   - Non-linearity: Relationship may not be perfectly linear (income may peak mid-career)

**Expected output:** Complete Section 6 (4-5 pages total for Block 4)

---

## Phase 6: Block 5 - ANOVA (Tasks 5a-5c)

### 6.1 Implement Block 5 Python Analysis
**Why:** Conduct one-way ANOVA with post-hoc tests at unusual significance level.

**What to do in block5_anova.py:**

```python
# Block 5: gd02 ~ hs01

# 1. Load data
df = pd.read_csv('data/processed/allbus_clean.csv')
df_anova = df[['hs01', 'gd02']].dropna()

# Task 5a: Group formation and descriptives

# Group sizes
group_sizes = df_anova['hs01'].value_counts().sort_index()

# Descriptive statistics by group
desc_by_group = df_anova.groupby('hs01')['gd02'].agg([
    ('n', 'count'),
    ('Mittelwert', 'mean'),
    ('SD', 'std'),
    ('Min', 'min'),
    ('Max', 'max')
]).reset_index()

desc_by_group.to_latex('latex/tables/gd02_by_hs01_descriptives.tex', ...)

# Task 5c: One-way ANOVA

from scipy import stats as scipy_stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Prepare data: ensure hs01 is categorical
df_anova['hs01_cat'] = df_anova['hs01'].astype('category')

# Conduct ANOVA using statsmodels (gives more detailed output)
model = ols('gd02 ~ C(hs01)', data=df_anova).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Extract key statistics
f_stat = anova_table.loc['C(hs01)', 'F']
p_value = anova_table.loc['C(hs01)', 'PR(>F)']
df_between = anova_table.loc['C(hs01)', 'df']
df_within = anova_table.loc['Residual', 'df']

# Create summary table
anova_results = pd.DataFrame({
    'Quelle': ['Zwischen Gruppen (hs01)', 'Innerhalb Gruppen (Residuen)', 'Total'],
    'df': [df_between, df_within, df_between + df_within],
    'SS': [anova_table.loc['C(hs01)', 'sum_sq'], 
           anova_table.loc['Residual', 'sum_sq'],
           anova_table.loc['C(hs01)', 'sum_sq'] + anova_table.loc['Residual', 'sum_sq']],
    'MS': [anova_table.loc['C(hs01)', 'sum_sq'] / df_between,
           anova_table.loc['Residual', 'sum_sq'] / df_within,
           ''],
    'F': [f_stat, '', ''],
    'p-Wert': [p_value, '', '']
})
anova_results.to_latex('latex/tables/gd02_anova.tex', ...)

# Significance at different alpha levels
alpha_020 = 'Ja' if p_value < 0.20 else 'Nein'
alpha_005 = 'Ja' if p_value < 0.05 else 'Nein'
alpha_040 = 'Ja' if p_value < 0.40 else 'Nein'

alpha_comparison = pd.DataFrame({
    'Signifikanzniveau (α)': [0.05, 0.20, 0.40],
    'Signifikant?': [alpha_005, alpha_020, alpha_040],
    'Interpretation': [
        'Konventionell (5% Fehlerrisiko)',
        'Vorgegeben für diese Aufgabe',
        'Sehr liberal (40% Fehlerrisiko)'
    ]
})
alpha_comparison.to_latex('latex/tables/anova_alpha_comparison.tex', ...)

# Post-hoc tests: Tukey HSD
# Even if ANOVA not significant at α=0.20, task requires running it
tukey = pairwise_tukeyhsd(endog=df_anova['gd02'], 
                          groups=df_anova['hs01'], 
                          alpha=0.20)  # Use α=0.20 as specified

# Convert Tukey results to DataFrame
tukey_df = pd.DataFrame(data=tukey.summary().data[1:], 
                        columns=tukey.summary().data[0])
tukey_df.to_latex('latex/tables/gd02_posthoc_tukey.tex', ...)

# Also compare with α=0.05 and α=0.40
tukey_005 = pairwise_tukeyhsd(endog=df_anova['gd02'], 
                              groups=df_anova['hs01'], 
                              alpha=0.05)
tukey_040 = pairwise_tukeyhsd(endog=df_anova['gd02'], 
                              groups=df_anova['hs01'], 
                              alpha=0.40)

# Create comparison table showing which pairs differ at each alpha
# (Implementation depends on output format)
```

**Expected outputs:**
- `latex/tables/gd02_by_hs01_descriptives.tex`
- `latex/tables/gd02_anova.tex`
- `latex/tables/anova_alpha_comparison.tex`
- `latex/tables/gd02_posthoc_tukey.tex`
- Optional: additional comparison tables for different α

---

### 6.2 Write LaTeX Section: Block 5 Interpretation
**Why:** Demonstrate understanding of ANOVA and critical discussion of significance levels.

**What to do in 07_block5_anova.tex:**

#### **Task 5a: Group Description (1 page)**

1. **Group formation:**
   - "Die Stichprobe wurde nach der Variable `hs01` (subjektiver Gesundheitszustand) in Gruppen aufgeteilt."
   - Include table: `\input{tables/gd02_by_hs01_descriptives.tex}`

2. **Answer specific questions:**
   - "Es wurden [X] Gruppen gebildet, entsprechend den Ausprägungen von `hs01`."
   - List groups and sizes: "Sehr gut: n=[X], Gut: n=[Y], Zufriedenstellend: n=[Z], ..."

3. **Descriptive comparison:**
   - "Die mittlere Wohndauer variiert zwischen den Gruppen:"
   - Lowest: "Gruppe [X] hat mit $\bar{x}$=[Y] Jahren die kürzeste durchschnittliche Wohndauer."
   - Highest: "Gruppe [X] hat mit $\bar{x}$=[Y] Jahren die längste durchschnittliche Wohndauer."
   - Variability: Comment on standard deviations

#### **Task 5b: Independence Argument (0.5-1 page)**

**This is conceptual argumentation:**

1. **Independence definition:**
   - Groups are independent if observations in one group don't influence observations in another
   - Each person belongs to exactly one group

2. **ALLBUS context:**
   - "Jede befragte Person gehört genau einer Gesundheitskategorie (`hs01`) an."
   - "Es gibt keine wiederholten Messungen derselben Person."
   - "Die Zuordnung zu Gesundheitskategorien erfolgt unabhängig zwischen Personen."

3. **No systematic dependencies:**
   - Persons are not paired/matched across groups
   - No clustering (family members, households) that violates independence assumption
   - Survey design: independent random sampling

4. **Conclusion:**
   - "Somit ist die Voraussetzung unabhängiger Gruppen für die Durchführung einer ANOVA erfüllt."

#### **Task 5c: ANOVA and Post-Hoc (2.5-3 pages)**

1. **Hypotheses:**
   - H₀: μ₁ = μ₂ = ... = μₖ (all group means equal in population)
   - H₁: At least one group mean differs
   - α = 0.20 (as specified in task!)

2. **Method description:**
   - "Eine einfaktorielle ANOVA wurde durchgeführt, um zu prüfen, ob sich die mittlere Wohndauer (`gd02`) zwischen den Gesundheitsgruppen (`hs01`) unterscheidet."
   - Briefly explain ANOVA logic: partitioning variance into between-groups and within-groups

3. **Present ANOVA results:**
   - Include table: `\input{tables/gd02_anova.tex}`
   - "Die ANOVA ergibt F([df_between], [df_within]) = [F], p = [p_value]."

4. **Decision at α = 0.20:**
   - If p < 0.20: "Bei α = 0.20 wird H₀ verworfen. Es besteht ein signifikanter Unterschied zwischen mindestens zwei Gruppen."
   - If p ≥ 0.20: "Bei α = 0.20 wird H₀ nicht verworfen. Kein signifikanter Unterschied nachweisbar."

5. **Comparison across significance levels:**
   - Include table: `\input{tables/anova_alpha_comparison.tex}`
   - **α = 0.05 (conventional):**
     - Decision: [Reject/Fail to reject] H₀
     - "Mit α = 0.05 (5% Irrtumswahrscheinlichkeit) würde die Entscheidung [gleich bleiben / anders ausfallen]..."
   - **α = 0.20 (task requirement):**
     - "Das vorgegebene α = 0.20 ist ungewöhnlich liberal."
     - "Dies erhöht die Power (Wahrscheinlichkeit, einen wahren Effekt zu finden)..."
     - "...aber auch die Fehler-1.-Art-Rate (fälschlicherweise H₀ verwerfen, wenn wahr)."
   - **α = 0.40 (very liberal):**
     - Decision: [almost certainly reject if 0.20 already rejects]
     - "Mit α = 0.40 würde man in 40% der Fälle einen Unterschied 'finden', selbst wenn keiner existiert – wissenschaftlich nicht vertretbar."

6. **Type I vs. Type II errors discussion:**
   - Type I error (α): Rejecting true H₀ (false positive)
   - Type II error (β): Failing to reject false H₀ (false negative)
   - Trade-off: Lower α reduces Type I but increases Type II
   - "Die Wahl von α = 0. 20 ist für explorative Studien oder Pilotstudien denkbar, aber für Standardanalysen zu riskant."

7. **Post-hoc tests:**
   - "Obwohl die Aufgabe es verlangt (auch wenn es bei manchen Ergebnissen keinen Sinn macht), wurde ein Tukey-HSD-Post-Hoc-Test durchgeführt."
   - Include table: `\input{tables/gd02_posthoc_tukey.tex}`
   - "Der Tukey-Test identifiziert, welche Gruppenpaare sich signifikant unterscheiden:"
   - List significant pairs at α = 0.20
   - Example: "Die Gruppe 'Sehr gut' unterscheidet sich signifikant von der Gruppe 'Weniger gut' (p = [value] < 0.20)."

8. **Why post-hoc might not make sense:**
   - "Falls die ANOVA bei α = 0.20 nicht signifikant war, macht der Post-Hoc-Test konzeptionell wenig Sinn, da die Gesamthypothese (mindestens ein Unterschied) bereits verworfen wurde."
   - "Dennoch zeigt die Übung die Durchführung und Interpretation."

9. **Substantive interpretation:**
   - "Inhaltlich könnte ein Zusammenhang zwischen Gesundheitszustand und Wohndauer verschiedene Ursachen haben:"
   - Gesundheit → Mobilität (kranke Menschen ziehen seltener um)
   - Wohndauer → Gesundheit (lange Wohndauer = stabile Umgebung = bessere Gesundheit)
   - Dritte Variable: Alter (ältere Menschen haben länger gewohnt UND schlechtere Gesundheit)

10. **Limitations:**
    - Ordinal variable (`hs01`) treated as categorical factor (appropriate for ANOVA)
    - Could also model ordinality explicitly (ordinal regression)
    - Cross-sectional data: no causal inference possible

**Expected output:** Complete Section 7 (4-5 pages total for Block 5)

---

## Phase 7: Final Sections & Quality Assurance

### 7.1 Update `run_all.py` Master Script
**Why:** Orchestrate all analyses in correct order for reproducibility.

**What to do in run_all.py:**

```python
"""
Master script to run all statistical analyses for the workbook.
Executes data preparation and all 5 analysis blocks in sequence.
"""

import sys
import subprocess

def run_script(script_name):
    """Execute a Python script and handle errors."""
    print(f"\n{'='*60}")
    print(f"Running {script_name}...")
    print('='*60)
    
    try:
        result = subprocess.run(
            [sys.executable, f"src/{script_name}"],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        print(f"✓ {script_name} completed successfully\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error in {script_name}:")
        print(e.stderr)
        return False

def main():
    """Run all analysis scripts in order."""
    
    scripts = [
        'data_prep.py',        # Clean and prepare data
        'block1_univariat.py', # Univariate analysis
        'block2_bivariat.py',  # Bivariate analysis
        'block3_tests.py',     # Confidence intervals & t-tests
        'block4_regression.py',# Correlation & regression
        'block5_anova.py'      # ANOVA
    ]
    
    print("\n" + "="*60)
    print("STATISTICS WORKBOOK - COMPLETE ANALYSIS PIPELINE")
    print("="*60)
    
    results = {}
    for script in scripts:
        results[script] = run_script(script)
    
    # Summary
    print("\n" + "="*60)
    print("EXECUTION SUMMARY")
    print("="*60)
    
    for script, success in results.items():
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"{script:25s} {status}")
    
    all_success = all(results.values())
    
    if all_success:
        print("\n" + "="*60)
        print("ALL ANALYSES COMPLETED SUCCESSFULLY!")
        print("Next steps:")
        print("1. Review generated tables in latex/tables/")
        print("2. Review generated figures in figures/")
        print("3. Compile LaTeX document: cd latex && lualatex main.tex")
        print("="*60 + "\n")
    else:
        print("\n" + "="*60)
        print("SOME ANALYSES FAILED - Please review errors above")
        print("="*60 + "\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

**Expected output:** Working master script that runs entire pipeline

**Validation:** Execute `python src/run_all.py` and verify all scripts complete successfully

---

### 7.2 Write Discussion Section
**Why:** Reflect on methodology, findings, and limitations (demonstrates critical thinking).

**What to do in 08_diskussion.tex:**

**Structure (2-3 pages):**

1. **Summary of key findings:**
   - Brief recap of main results from each block
   - "Die univariaten Analysen zeigten..."
   - "Im bivariaten Kontext wurde festgestellt..."
   - "Inferenzstatistische Tests ergaben..."
   - "Die Regressionsanalyse offenbarte..."
   - "Die ANOVA zeigte..."

2. **Methodological reflections:**
   - **Measurement levels:** "Die Beachtung der Skalenniveaus war entscheidend für die Wahl geeigneter Analysemethoden..."
   - **Missing data:** "Der listenweise Fallausschluss könnte zu Verzerrungen führen, wenn Daten nicht zufällig fehlen (MCAR)..."
   - **Assumption violations:** Discuss any violated assumptions (normality, homoscedasticity, etc.)

3. **Correlation vs. causation:**
   - "Durchgängig wurde deutlich, dass die gefundenen Zusammenhänge keine kausalen Schlüsse erlauben..."
   - ALLBUS = cross-sectional observational data
   - Need for longitudinal/experimental designs

4. **Significance testing critique:**
   - "Die mechanische Anwendung von p < 0.05 als Entscheidungskriterium ist problematisch..."
   - Discuss: effect sizes vs. statistical significance
   - Publication bias, p-hacking
   - α = 0.20 exercise showed arbitrariness of thresholds

5. **Practical significance:**
   - Some statistically significant findings may lack practical importance
   - Example: "Ein Einkommensunterschied von 50€ bei n=3000 kann statistisch signifikant sein, ist aber praktisch vernachlässigbar."

6. **Limitations:**
   - Sample: represents 2021 Germany only (dated by now in 2025)
   - Survey data: self-reports, social desirability bias
   - Simplified analyses: ignored confounders, interactions, non-linearities
   - Workbook scope: real analysis would require more sophisticated methods

7. **Strengths:**
   - Representative probability sample
   - Established survey (ALLBUS)
   - Transparent documentation of methods
   - Reproducible analysis pipeline

**Expected output:** Complete Section 8 (2-3 pages)

**Citations:** Reference methodological literature if used

---

### 7.3 Write Conclusion Section
**Why:** Provide closure and summarize learning outcomes.

**What to do in 09_fazit.tex:**

**Structure (1-1.5 pages):**

1. **Achievement summary:**
   - "Dieses Workbook demonstrierte die Anwendung fundamentaler statistischer Methoden auf sozialwissenschaftliche Daten..."
   - Covered: descriptive statistics, visualization, inference, correlation, regression, ANOVA

2. **Learning outcomes:**
   - "Die Bearbeitung verdeutlichte die Bedeutung von:"
     - Measurement level awareness
     - Appropriate method selection
     - Assumption checking
     - Critical interpretation beyond p-values
     - Distinction between statistical and practical significance

3. **Key takeaways:**
   - Statistics as tool for understanding, not just number crunching
   - Importance of transparency and reproducibility
   - Limitations of observational data for causal inference

4. **Outlook:**
   - "Weiterführende Analysen könnten umfassen:"
     - Multivariate regression (controlling for confounders)
     - Structural equation modeling
     - Longitudinal analysis
     - Machine learning approaches

5. **Personal reflection (optional, brief):**
   - Challenges encountered
   - Skills developed

**Expected output:** Complete Section 9 (1-1.5 pages)

---

### 7.4 Complete Front Matter
**Why:** Fulfill formal requirements for academic submission.

**What to do in 00_frontmatter.tex:**

1. **Ehrenwörtliche Erklärung (Declaration of Authenticity):**
   - Standard text about independent work
   - No plagiarism
   - Proper citations
   - Sign with name, date, location

2. **Abstract (optional but recommended):**
   - 150-250 words summarizing:
     - Purpose: statistical analysis of ALLBUS 2021 data
     - Methods: descriptive, inferential, regression, ANOVA
     - Key findings: brief highlights
     - Conclusion: demonstrated methodological competence

3. **Danksagung (Acknowledgments - optional):**
   - Thank course instructor
   - Any persons who provided feedback
   - ALLBUS team for data access

**Expected output:** Complete Section 0

---

### 7.5 Create and Verify Bibliography
**Why:** Fulfill citation requirements and academic standards.

**What to do in main.bib:**

**Required entries:**

```bibtex
% ALLBUS data citation
@misc{allbus2021,
    author = {{GESIS - Leibniz-Institut für Sozialwissenschaften}},
    title = {Allgemeine Bevölkerungsumfrage der Sozialwissenschaften ALLBUS 2021},
    year = {2021},
    doi = {10.4232/1.13742},
    publisher = {GESIS Datenarchiv},
    address = {Köln}
}

% Course materials (adjust as needed)
@misc{vorlesung2025,
    author = {Labs, Oliver},
    title = {Statistik - Vorlesungsunterlagen},
    year = {2025},
    howpublished = {IU Internationale Hochschule, myCampus},
    note = {Wintersemester 2024/25}
}

% Add textbook if used
@book{example_textbook,
    author = {Nachname, Vorname},
    title = {Statistik-Lehrbuch Titel},
    year = {2023},
    publisher = {Verlag},
    address = {Stadt}
}
```

**In-text citations:**
- Throughout LaTeX sections, add citations: `\cite{allbus2021}` when discussing data
- `\cite{vorlesung2025}` when referencing methods from course materials
- Add page/slide numbers in citations: `\cite[S. 42]{vorlesung2025}`

**Expected output:** Complete bibliography with at least ALLBUS and course materials cited

---

### 7.6 Quality Assurance Checklist
**Why:** Ensure all formal and content requirements are met before submission.

**Complete this checklist systematically:**

#### **Formal Requirements:**
- [ ] Student metadata filled in main.tex (name, matriculation number, address, date)
- [ ] 10-20 pages main content (excluding front matter, TOC, references)
- [ ] Arial font throughout (already in template)
- [ ] Consistent formatting (APA7 style already configured)
- [ ] No spelling/grammar errors (run spell check)
- [ ] All figures have captions and source notes
- [ ] All tables have captions and labels
- [ ] All figures/tables referenced in text
- [ ] Page numbers present
- [ ] Table of contents up to date (compile LaTeX twice)

#### **Content Requirements:**

**Block 1 (20%):**
- [ ] Task 1a: Full dataset description with sample size, missing values strategy, measurement levels, variable assignment screenshot
- [ ] Task 1b: Comprehensive measurement level explanation with examples
- [ ] Task 1c: `ep04` frequency table, bar chart, mode, median, interpretation
- [ ] Task 1d: `hhinc` classes, frequency table, histogram, mean, SD, density discussion

**Block 2 (20%):**
- [ ] Task 2a: `ep01` × `fe14` contingency table, mosaic plot, Spearman correlation, interpretation
- [ ] Task 2b: `xt10` × `age` scatter plot, Pearson correlation explained and calculated
- [ ] Task 2c: Correlation vs. causation discussion with examples

**Block 3 (20%):**
- [ ] Task 3a: Population vs. sample explanation in ALLBUS context
- [ ] Task 3b: 95% CI for `lm02` with CORRECT interpretation
- [ ] Task 3c: Two-sample t-test with hypotheses, independence argument, interpretation

**Block 4 (20%):**
- [ ] Task 4a: `age` × `hhinc` Pearson correlation with significance test
- [ ] Task 4b: Scatter plot with causal direction discussion
- [ ] Task 4c: Linear regression equation, R², significance, example prediction, interpretation

**Block 5 (20%):**
- [ ] Task 5a: Groups by `hs01`, sizes, descriptive statistics for `gd02`
- [ ] Task 5b: Independence argument for ANOVA
- [ ] Task 5c: ANOVA at α=0.20, post-hoc tests, comparison with α=0.05 and α=0.40

#### **Technical Requirements:**
- [ ] All Python scripts run without errors
- [ ] `python src/run_all.py` executes successfully
- [ ] All tables exist in `latex/tables/`
- [ ] All figures exist in `figures/blockX/`
- [ ] LaTeX compiles without errors: `cd latex && lualatex main.tex`
- [ ] All `\input{}` and `\includegraphics{}` commands find their files
- [ ] No TODO markers remain in LaTeX files

#### **Academic Standards:**
- [ ] All sources cited (ALLBUS, course materials, any textbooks)
- [ ] Bibliography complete and formatted correctly
- [ ] Methods justified (why this test/visualization?)
- [ ] Results interpreted substantively (not just "p < 0.05")
- [ ] Limitations discussed
- [ ] Ehrenwörtliche Erklärung signed

#### **Python Code Quality:**
- [ ] Code is readable with comments
- [ ] No hardcoded paths (use config.py)
- [ ] Consistent style (optional: run `black` formatter)
- [ ] Results reproducible (set random seed in config)

**Validation:** Go through each checkbox systematically. Fix any missing elements.

---

### 7.7 Final Document Compilation
**Why:** Generate the submission-ready PDF.

**What to do:**

1. **Compile LaTeX (in PowerShell):**
   ```powershell
   cd latex
   lualatex main.tex
   biber main          # If using bibliography
   lualatex main.tex   # Second run for references
   lualatex main.tex   # Third run for TOC
   ```

2. **Verify PDF output:**
   - Open `latex/main.pdf`
   - Check all sections present
   - Verify figures display correctly
   - Check tables format properly
   - Confirm page count (10-20 pages main content)
   - Review table of contents
   - Check figure/table numbering

3. **Final proofreading:**
   - Read entire document start to finish
   - Check for:
     - Typos and grammatical errors
     - Inconsistent terminology
     - Missing or incorrect citations
     - Awkward phrasing
     - Logical flow between sections
     - Consistency in notation (e.g., always `β₁` not sometimes `b₁`)

4. **Generate screenshot for Task 1a:**
   - Open `data/raw/Zuteilung_OL_2025Q4.csv` in Excel
   - Your matriculation number visible in cell
   - All assigned variables visible
   - Take screenshot
   - Save as `figures/variable_assignment.png`
   - Include in Section 2 (02_daten.tex)

---

### 7.8 Prepare Submission Files
**Why:** Meet submission requirements (PDF + Python files).

**What to do:**

1. **Rename PDF for submission:**
   ```powershell
   cd latex
   cp main.pdf ../Workbook_Statistik_[YourMatrNo]_[YourLastName].pdf
   ```

2. **Prepare Python files email:**
   - Create folder: `Workbook_Python_[YourMatrNo]`
   - Copy all .py files from `src/`:
     - config.py
     - data_prep.py
     - block1_univariat.py
     - block2_bivariat.py
     - block3_tests.py
     - block4_regression.py
     - block5_anova.py
     - run_all.py
   - Optional: Include requirements.txt
   - Optional: Include README with execution instructions
   - Zip folder: `Workbook_Python_[YourMatrNo].zip`

3. **Upload to myCampus/Turnitin:**
   - Submit PDF only (as per instructions)
   - Verify upload successful

4. **Send Python files via email:**
   - To: Oliver.Labs@iu.org
   - Subject: "Workbook Statistik WiSe 2025 - Python-Dateien - [Your Matrikelnummer]"
   - Attachment: ZIP file with all Python scripts
   - Brief email body:
     ```
     Sehr geehrter Herr Labs,
     
     im Anhang finden Sie die Python-Dateien zu meinem Workbook Statistik.
     Matrikelnummer: [Your Number]
     
     Das Workbook-PDF wurde über myCampus/Turnitin eingereicht.
     
     Mit freundlichen Grüßen,
     [Your Name]
     ```

---

## Phase 8: Optional Enhancements (Time Permitting)

### 8.1 Advanced Visualizations
**Why:** Improve presentation quality beyond minimum requirements.

**Optional enhancements:**

1. **Boxplots for group comparisons:**
   - Block 3: `lm02` by `sex` boxplot
   - Block 5: `gd02` by `hs01` boxplot
   - Shows distribution beyond just means

2. **Diagnostic plots for regression:**
   - Residual plots (residuals vs. fitted)
   - Q-Q plot (normality of residuals)
   - Scale-location plot (homoscedasticity)
   - Shows assumption checking

3. **Enhanced scatter plots:**
   - Add confidence bands around regression line
   - Color-code by third variable
   - Add marginal histograms

4. **Heatmap for correlation matrix:**
   - If analyzing multiple variables
   - Shows patterns at a glance

**Implementation:** Add to respective block scripts, export to figures/, include in LaTeX if space allows

---

### 8.2 Sensitivity Analyses
**Why:** Demonstrate robustness of findings.

**Optional analyses:**

1. **Different class widths for `hhinc`:**
   - Compare results with alternative binning
   - Discuss sensitivity to choices

2. **Outlier handling:**
   - Identify outliers (e.g., income > 99th percentile)
   - Re-run analyses with/without outliers
   - Discuss impact

3. **Different correlation methods:**
   - Compare Pearson vs. Spearman for `xt10` × `age`
   - Discuss when differences emerge

**Reporting:** Add to discussion section if implemented

---

### 8.3 Code Documentation
**Why:** Professional practice and potential reuse.

**Enhancements:**

1. **Docstrings for all functions:**
   ```python
   def calculate_frequency_table(series, relative=True):
       """
       Calculate frequency table for categorical variable.
       
       Parameters:
       -----------
       series : pd.Series
           Categorical variable
       relative : bool
           If True, include relative frequencies
           
       Returns:
       --------
       pd.DataFrame
           Frequency table with absolute and relative frequencies
       """
       ...
   ```

2. **Inline comments:**
   - Explain complex steps
   - Document data transformations
   - Justify methodological choices

3. **README for Python code:**
   - Execution instructions
   - Package versions used
   - Expected outputs

---

### 8.4 Reproducibility Documentation
**Why:** Scientific best practice.

**Create reproducibility report:**

1. **System information:**
   ```python
   import platform
   import pandas as pd
   import numpy as np
   import scipy
   import statsmodels
   
   print(f"Python version: {platform.python_version()}")
   print(f"Pandas version: {pd.__version__}")
   print(f"NumPy version: {np.__version__}")
   print(f"SciPy version: {scipy.__version__}")
   print(f"Statsmodels version: {statsmodels.__version__}")
   ```

2. **Execution log:**
   - Save console output when running `run_all.py`
   - Include timestamps

3. **Checksums:**
   - MD5 hash of input data file
   - Ensures data integrity

**Optional:** Include in appendix or separate documentation file

---

## Timeline and Effort Estimation

### Recommended Schedule (assumes ~40-60 hours total):

**Week 1: Foundation (8-10 hours)**
- Day 1-2: Data preparation (7.2.1) - 3-4 hours
- Day 3-4: Task 1a LaTeX + Block 1 Python (1.2-2.2) - 5-6 hours

**Week 2: Descriptive Statistics (10-12 hours)**
- Day 1-2: Block 1 LaTeX interpretation (2.2) - 4-5 hours
- Day 3-4: Block 2 Python + LaTeX (3.1-3.3) - 6-7 hours

**Week 3: Inferential Statistics (10-12 hours)**
- Day 1-2: Block 3 Python + LaTeX (4.1-4.2) - 5-6 hours
- Day 3-4: Block 4 Python + LaTeX (5.1-5.2) - 5-6 hours

**Week 4: Advanced Analysis (8-10 hours)**
- Day 1-2: Block 5 Python + LaTeX (6.1-6.2) - 5-6 hours
- Day 3-4: Discussion + Conclusion (7.2-7.3) - 3-4 hours

**Week 5: Finalization (10-12 hours)**
- Day 1: Quality assurance checklist (7.6) - 3-4 hours
- Day 2: Final compilation and proofreading (7.7) - 3-4 hours
- Day 3: Buffer for revisions - 2-3 hours
- Day 4: Submission preparation (7.8) - 1-2 hours

**Total: ~40-60 hours** (adjust based on prior statistical knowledge and Python proficiency)

---

## Critical Success Factors

### Must-Do (Non-Negotiable):

1. **Use assigned variables** from Zuteilung file - using wrong variables = major deduction
2. **Cite sources properly** - at minimum ALLBUS data and course materials
3. **Interpret results substantively** - not just "p < 0.05" but what it means
4. **Meet formal requirements** - 10-20 pages, proper formatting, signed declaration
5. **Ensure reproducibility** - `run_all.py` must execute without errors
6. **LaTeX must compile** - cannot submit broken PDF

### Should-Do (Strongly Recommended):

1. **Check assumptions** - mention normality, homoscedasticity, etc.
2. **Discuss limitations** - shows critical thinking
3. **Use proper terminology** - "statistically significant" not just "significant"
4. **Proofread carefully** - spelling/grammar errors hurt credibility
5. **Make figures professional** - clear labels, readable fonts, proper scaling

### Nice-to-Have (If Time):

1. **Advanced visualizations** - diagnostic plots, enhanced graphics
2. **Sensitivity analyses** - robustness checks
3. **Detailed code comments** - helps reviewer understand approach
4. **Appendix** - additional tables, extended discussion

---

## Common Pitfalls to Avoid

### Statistical:
- ❌ Confusing correlation with causation
- ❌ Misinterpreting confidence intervals (see Task 3b)
- ❌ Using mean for ordinal variables
- ❌ Ignoring violated assumptions without discussion
- ❌ Over-interpreting small effect sizes
- ❌ Reporting only p-values without effect sizes

### Technical:
- ❌ Hardcoding file paths (use config.py)
- ❌ Not handling missing values consistently
- ❌ Forgetting to set figure size (tiny plots in LaTeX)
- ❌ LaTeX special characters not escaped (%, $, &, etc.)
- ❌ Using wrong encoding (use UTF-8)

### Formal:
- ❌ Missing citations
- ❌ Inconsistent notation
- ❌ Too short or too long (not 10-20 pages)
- ❌ Missing signature on declaration
- ❌ Wrong submission format

### Content:
- ❌ Pure description without interpretation
- ❌ Screenshots without explanation
- ❌ Copy-pasted software output without commentary
- ❌ Missing discussion of limitations
- ❌ No coherent narrative (just disconnected analyses)

---

## Resources and References

### Official Materials:
- Task PDF: `docs/DS-Statistik2025WiSe-VC_Workbook_Aufgaben_OL_2025-11-03.pdf`
- Data: `data/raw/VERSION_2025-11-19_..._ALLBUS_..._Teildatensatz-aus-2021-nur-29-Variablen.xlsx`
- Data description: `VERSION-2025-11-19_..._Workbook_Datensatz-Beschreibung_OL_2025-11-01.docx`
- Variable assignment: `data/raw/Zuteilung_OL_2025Q4.csv`
- IU guidelines: Available on myCampus

### Python Documentation:
- Pandas: https://pandas.pydata.org/docs/
- SciPy stats: https://docs.scipy.org/doc/scipy/reference/stats.html
- Statsmodels: https://www.statsmodels.org/stable/index.html
- Matplotlib: https://matplotlib.org/stable/index.html

### Statistical Resources:
- Course materials on myCampus (primary reference!)
- Statistics textbooks as needed
- ALLBUS documentation: https://www.gesis.org/allbus

---

## Final Checklist Before Submission

**48 hours before deadline:**
- [ ] All analyses complete
- [ ] LaTeX compiles successfully
- [ ] PDF has 10-20 pages main content
- [ ] All requirements from checklist 7.6 met

**24 hours before deadline:**
- [ ] Final proofreading complete
- [ ] Fresh eyes review (if possible, ask someone to read it)
- [ ] Bibliography verified
- [ ] Signature on declaration

**12 hours before deadline:**
- [ ] PDF renamed for submission
- [ ] Python files zipped
- [ ] Test LaTeX compilation one final time
- [ ] Email to Oliver.Labs@iu.org drafted

**2 hours before deadline:**
- [ ] Upload PDF to myCampus/Turnitin
- [ ] Send email with Python files
- [ ] Verify uploads successful
- [ ] Keep confirmation emails

**After submission:**
- [ ] Backup all files (ZIP entire project directory)
- [ ] Store in cloud (OneDrive, Google Drive, etc.)
- [ ] Celebrate completing a comprehensive statistical analysis! 🎉

---

## Conclusion

This plan provides a complete, step-by-step roadmap from data preparation through final submission. The key to success is:

1. **Systematic execution** - work through phases in order
2. **Regular validation** - test each component as you build it
3. **Clear documentation** - both in code and LaTeX
4. **Critical interpretation** - go beyond mere calculation
5. **Attention to detail** - formal requirements matter

Follow this plan methodically, allocate sufficient time, and you will produce a high-quality workbook that demonstrates comprehensive statistical competence.

**Remember:** The goal is not just to complete the assignment, but to genuinely understand and apply statistical methods to real-world data. Use this opportunity to develop skills that will serve you throughout your academic and professional career.

---

**Document Version:** 1.0  
**Created:** December 5, 2025  
**Status:** Complete execution plan ready for implementation  
**Next Action:** Begin Phase 1.1 - Update LaTeX metadata
