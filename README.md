# Statistik-Workbook WiSe 2025 – ALLBUS 2021

Dieses Repository enthält die Bearbeitung des Statistik-Workbooks im Wintersemester 2025 auf Basis des ALLBUS-Teildatensatzes 2021.

Die **verbindliche Aufgabenstellung** befindet sich in:

> `docs/DS-Statistik2025WiSe-VC_Workbook_Aufgaben_OL_2025-11-03.pdf`

Diese PDF ist die **Source of Truth** für alle Aufgaben.  
Alle Beschreibungen in diesem README sind nur erläuternde Zusammenfassungen.

---

## 1. Überblick: Aufgabenblöcke und meine Variablen

### Aufgabe 1b–1d – Univariate Deskription & Skalenniveaus

- **Ziel (kurz):**
  - 1b: Skalenniveaus (nominal, ordinal, metrisch) erklären.
  - 1c: Ordinale Variable univariat beschreiben.
  - 1d: Metrische Variable univariat beschreiben (Klassen, Histogramm, Kennwerte).

- **Meine Variablen:**
  - `mc04` – nominal
  - `ep04` – ordinal
  - `hhinc` – metrisch

- **Statistische Aufgaben (paraphrasiert):**
  - Skalenniveaus definieren und an `mc04`, `ep04`, `hhinc` illustrieren.
  - Für `ep04`: Häufigkeitstabelle, Lagemaße (Modus, Median), geeignetes Diagramm.
  - Für `hhinc`: Klassenbildung, Häufigkeitstabelle, Histogramm, Mittelwert, Standardabweichung.

---

### Aufgabe 2a – Bivariate Deskription (ordinal × ordinal)

- **Ziel (kurz):**
  - Gemeinsame Verteilung und Zusammenhang zweier ordinaler Variablen untersuchen.

- **Meine Variablen:**
  - `ep01`
  - `fe14`

- **Statistische Aufgaben (paraphrasiert):**
  - Kreuztabelle `ep01 × fe14` (absolute und relative Häufigkeiten).
  - Grafische Darstellung (z. B. Mosaikdiagramm).
  - Zusammenhang messen (z. B. Spearman-Rangkorrelation) und interpretieren.

---

### Aufgabe 2b–2c – Korrelation und Kausalität (metrisch × metrisch)

- **Ziel (kurz):**
  - 2b: Linearen Zusammenhang zwischen zwei metrischen Variablen beschreiben.
  - 2c: Klarstellen, warum Korrelation keine Kausalität ist.

- **Meine Variablen:**
  - `xt10` – metrisch
  - `age` – metrisch

- **Statistische Aufgaben (paraphrasiert):**
  - Streudiagramm `xt10` vs. `age`.
  - Pearson-Korrelation berechnen und interpretieren.
  - Diskutieren, warum ein gefundener Zusammenhang keine kausale Aussage beweist.

---

### Aufgabe 3 – Inferenz mit einer metrischen Variable (`lm02`)

- **Ziel (kurz):**
  - Grundgesamtheit vs. Stichprobe erklären.
  - Konfidenzintervall für einen Mittelwert.
  - t-Test für zwei unabhängige Gruppen.

- **Meine Hauptvariable:**
  - `lm02` – metrisch

- **Statistische Aufgaben (paraphrasiert):**
  - Population / Stichprobe im ALLBUS-Kontext beschreiben.
  - 95 %-Konfidenzintervall für den Mittelwert von `lm02` berechnen und interpretieren.
  - Zwei-Gruppen-t-Test für `lm02` mit einer geeigneten Gruppierungsvariable (z. B. `sex`).

---

### Aufgabe 4 – Korrelation & Regression (`age` und `hhinc`)

- **Ziel (kurz):**
  - Linearen Zusammenhang zwischen Alter und Einkommen untersuchen.
  - Einfaches Regressionsmodell aufstellen und interpretieren.

- **Meine Variablen:**
  - `age` – metrisch
  - `hhinc` – metrisch

- **Statistische Aufgaben (paraphrasiert):**
  - Pearson-Korrelation zwischen `age` und `hhinc` (inkl. Signifikanztest).
  - Streudiagramm (x = `age`, y = `hhinc`), ggf. Regressionsgerade einzeichnen.
  - Einfache lineare Regression `hhinc ~ age`:
    - Schätzung und Interpretation von Koeffizienten.
    - R² und Signifikanztest.
    - Beispielhafte Prognose innerhalb des beobachteten Altersbereichs.

---

### Aufgabe 5 – Einfaktorielle ANOVA (`gd02` nach `hs01`)

- **Ziel (kurz):**
  - Mittelwerte einer metrischen Variable in mehreren Gruppen vergleichen.
  - ANOVA und Post-Hoc-Vergleiche interpretieren.

- **Meine Variablen:**
  - `hs01` – ordinal (als Gruppierungsfaktor)
  - `gd02` – metrisch

- **Statistische Aufgaben (paraphrasiert):**
  - Gruppen nach `hs01` bilden; n, Mittelwert, SD von `gd02` je Gruppe bestimmen.
  - Einfaktorielle ANOVA mit `gd02` als Zielvariable und `hs01` als Faktor (vorgegebenes α, z. B. 0,20, beachten).
  - Post-Hoc-Tests (z. B. Tukey) zur Identifikation signifikanter Gruppenpaare.
  - Einfluss des gewählten Signifikanzniveaus auf die Testergebnisse diskutieren.

---

## 2. Technisches Setup & Projektstruktur

- **Programmiersprache:** Python
- **Typische Pakete:** `pandas`, `numpy`, `matplotlib`, `scipy`, `statsmodels`

Empfohlene Struktur (vereinfacht):

```text
statistik-workbook/
├─ data/
│  ├─ raw/         # Originaldaten, inkl. Aufgaben-PDF
│  └─ processed/   # Bereinigte Daten (z. B. allbus_clean.csv)
├─ src/
│  ├─ config.py
│  ├─ data_prep.py
│  ├─ block1_univariat.py
│  ├─ block2_bivariat.py
│  ├─ block3_tests.py
│  ├─ block4_regression.py
│  ├─ block5_anova.py
│  └─ run_all.py
├─ figures/        # Alle Grafiken für das LaTeX-Workbook
├─ latex/
│  ├─ main.tex
│  └─ tables/      # Tabellen, die aus Python als .tex exportiert werden
└─ README.md
````

---

## 3. Datenquellen

* **Datensatz:**

  * `VERSION_2025-11-19_DS-Statistik2025WiSe_Workbook_ALLBUS_ZA5284_version-1-1-0_Teildatensatz-aus-2021-nur-29-Variablen.xlsx`
* **Datensatzbeschreibung:**

  * `VERSION-2025-11-19_DS-Statistik2025WiSe_Workbook_Datensatz-Beschreibung_OL_2025-11-01.docx`
* **Aufgabenstellung (Source of Truth):**

  * `DS-Statistik2025WiSe-VC_Workbook_Aufgaben_OL_2025-11-03.pdf`

---

## 4. Reproduzierbarkeit

1. Virtuelle Umgebung erstellen und aktivieren.
2. Pakete installieren (z. B. `pip install -r requirements.txt`).
3. Rohdaten und Aufgaben-PDF in `data/raw/` bzw. `docs/` ablegen.
4. Datenaufbereitung ausführen:

   ```bash
   python src/data_prep.py
   ```
5. Analysen laufen lassen:

   ```bash
   python src/run_all.py
   ```
6. LaTeX-Dokument kompilieren (`latex/main.tex`), um das fertige Workbook-PDF zu erzeugen.
