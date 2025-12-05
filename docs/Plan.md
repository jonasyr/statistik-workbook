# Step by Step Plan

## 1. Aufgabenverständnis im Kontext deiner Variablen

### Aufgabe 1b – Skalenniveaus erklären

* **Ziel:**
  Die drei Skalenniveaus (nominal, ordinal, metrisch) an echten Beispielen aus deinem Datensatz erklären und daraus ableiten, welche Auswertungen jeweils sinnvoll sind.
* **Relevante Variablen:**

  * `mc04` – „Ausländer im Freundeskreis?“ (nominal; Kategorien ohne natürliche Ordnung)
  * `ep04` – „Wirtschaftslage in Deutschland in 1 Jahr“ (ordinal; geordnete Antwortkategorien)
  * `hhinc` – Haushaltsnettoeinkommen (metrisch; Einkommen in Euro)
* **Statistische Methoden / Inhalte:**

  * Reine Beschreibung: Definition der drei Skalenniveaus.
  * Kurze Diskussion, welche Kennwerte und Diagramme pro Niveau erlaubt/sinnvoll sind (z. B. Modus vs. Median vs. Mittelwert).
* **Rolle der Messniveaus:**

  * **Nominal (`mc04`)** → Kategorien vergleichen, Häufigkeiten/Prozente, Modus.
  * **Ordinal (`ep04`)** → geordnete Kategorien, Median und Rang-basiertes Denken.
  * **Metrisch (`hhinc`)** → Mittelwert, Varianz, Standardabweichung, Histogramm, Regression etc.

---

### Aufgabe 1c – Univariate Beschreibung von `ep04` (ordinal)

* **Ziel:**
  Die Verteilung der Einschätzung der zukünftigen Wirtschaftslage (`ep04`) übersichtlich darstellen und interpretieren.
* **Relevante Variable:**

  * `ep04` (ordinal; z. B. 1 = „wesentlich besser“ … 5 = „wesentlich schlechter“)
* **Statistische Methoden:**

  * Häufigkeitstabelle (absolute und relative Häufigkeiten der Kategorien).
  * Balken-/Säulendiagramm mit geordneter x-Achse.
  * Lagemaße: Modus (häufigste Kategorie), Median (mittlere Kategorie).
* **Rolle der Messniveaus:**

  * Ordinalskala erlaubt sinnvolle Reihenfolge und Median/Modus, aber Mittelwert ist heikel zu interpretieren.
  * Diagrammwahl (Balkendiagramm) passt zur kategorialen, geordneten Natur.

---

### Aufgabe 1d – Univariate Beschreibung von `hhinc` (metrisch)

* **Ziel:**
  Die Einkommensverteilung (`hhinc`) über Klassen, Histogramm und Kennwerte beschreiben.
* **Relevante Variable:**

  * `hhinc` – Haushaltsnettoeinkommen (metrisch)
* **Statistische Methoden:**

  * Bereinigung: Sondercodes/negative Werte als fehlend behandeln.
  * Klassenbildung (z. B. 0–1000, 1000–2000, …) und Häufigkeitstabelle pro Klasse.
  * Histogramm (Diskussion: Häufigkeiten vs. Häufigkeitsdichten).
  * Kennwerte: Mittelwert, Standardabweichung, ggf. Median.
* **Rolle der Messniveaus:**

  * Metrisch → Mittelwert, SD, Histogramm und weitere metrische Verfahren (z. B. Regression, ANOVA) sind zulässig.

---

### Aufgabe 2a – Bivariate Deskription `ep01` und `fe14` (ordinal × ordinal)

* **Ziel:**
  Den Zusammenhang zwischen aktueller Wirtschaftseinschätzung und Erziehungsziel „Kind soll beliebt sein“ untersuchen.
* **Relevante Variablen:**

  * `ep01` – Einschätzung der **aktuellen** Wirtschaftslage (ordinal).
  * `fe14` – Wichtigkeit „beliebt sein“ als Erziehungsziel (ordinal, Ränge).
* **Statistische Methoden:**

  * Kreuztabelle (Kontingenztabelle) `ep01` × `fe14` mit absoluten und relativen Häufigkeiten.
  * Mosaikdiagramm (Verteilungen visuell).
  * Rangbezogenes Zusammenhangsmaß (Spearman-Rangkorrelation).
* **Rolle der Messniveaus:**

  * Beide Variablen ordinal → Ranginformation nutzen (Spearman), nicht nur nominale Struktur.
  * Interpretation: Richtung und Stärke eines monotonen Zusammenhangs.

---

### Aufgabe 2b – Korrelation `xt10` und `age` (metrisch × metrisch)

* **Ziel:**
  Den (linearen) Zusammenhang zwischen Interviewdauer und Alter quantifizieren.
* **Relevante Variablen:**

  * `xt10` – Interviewdauer (metrisch, z. B. Minuten).
  * `age` – Alter in Jahren (metrisch).
* **Statistische Methoden:**

  * Streudiagramm (z. B. x = Alter, y = Interviewdauer).
  * Pearson-Korrelationskoeffizient (Bravais-Pearson).
  * Evtl. Test auf Signifikanz der Korrelation.
* **Rolle der Messniveaus:**

  * Beide metrisch → Pearson-Korrelation ist Standardwahl.
  * Erlaubt Aussagen über Richtung (positiv/negativ), Stärke und Linearität.

---

### Aufgabe 2c – „Korrelation ist nicht Kausalität“ (Diskussion an `xt10` & `age`)

* **Ziel:**
  Anhand eines konkreten Beispiels klarmachen, warum ein beobachteter Zusammenhang keine Kausalität beweist.
* **Relevante Variablen:**

  * `xt10`, `age` (wie in 2b).
* **Statistische Methoden / Inhalte:**

  * Konzeptuelle Diskussion (keine neue Berechnung nötig):

    * A → B, B → A oder drittes Merkmal C beeinflusst beide.
    * Beispiel: Interviewdauer könnte vom Befrager, vom Fragebogen, von der Situation etc. abhängen.
* **Rolle der Messniveaus:**

  * Metrisch ist hier nur der Rahmen der vorherigen Korrelationsanalyse; der Kern ist interpretativ.

---

### Aufgabe 3 – Inferenz mit `lm02` (Konfidenzintervall & t-Test)

#### 3a – Population vs. Stichprobe

* **Ziel:**
  Unterschied zwischen Grundgesamtheit und Stichprobe im ALLBUS-Kontext erklären.
* **Relevante Variablen:**

  * Allgemein ALLBUS; beispielhaft `lm02` (metrisch).
* **Statistische Inhalte:**

  * Grundgesamtheit: z. B. deutsche Wohnbevölkerung ab X Jahren.
  * Stichprobe: tatsächlich befragte Personen im ALLBUS 2021.
  * Übergang zur Inferenzstatistik: von Stichprobe → Population.

---

#### 3b – 95 %-Konfidenzintervall für den Mittelwert von `lm02`

* **Ziel:**
  Den durchschnittlichen Fernsehkonsum in der Population anhand eines Konfidenzintervalls schätzen.
* **Relevante Variable:**

  * `lm02` – tägliche Fernsehdauer in Minuten (metrisch).
* **Statistische Methoden:**

  * Mittelwert, Standardabweichung, Stichprobengröße bestimmen.
  * 95 %-Konfidenzintervall für den Populationsmittelwert (t-Verteilung, da σ unbekannt).
  * Textliche Interpretation (kein „95 % der Personen liegen im Intervall“, sondern „95 % aller solcher Intervalle enthalten den wahren Mittelwert“).
* **Rolle der Messniveaus:**

  * Metrisch → Mittelwert und CI sinnvoll.
  * Annahme: Zentraler Grenzwertsatz bzw. (annähernd) normalverteilter Stichprobenmittelwert.

---

#### 3c – t-Test für zwei unabhängige Gruppen (z. B. `lm02` nach Geschlecht)

* **Ziel:**
  Prüfen, ob sich der durchschnittliche Fernsehkonsum in zwei Gruppen unterscheidet.
* **Relevante Variablen:**

  * Testvariable: `lm02` (metrisch).
  * Gruppierungsvariable: z. B. `sex` (nominal, 2 Kategorien).
* **Statistische Methoden:**

  * Deskriptiv: Mittelwert, SD, n pro Gruppe.
  * t-Test für unabhängige Stichproben (zweiseitig oder einseitig, je nach Fragestellung).
  * Interpretation von t-Wert, df, p-Wert (Signifikanzniveau 5 %).
* **Rolle der Messniveaus:**

  * Metrische Zielvariable, nominale Gruppierung → klassisches t-Test-Setting.
  * Unabhängigkeit der Gruppen wichtig (jede Person gehört genau einer Gruppe an).

---

### Aufgabe 4 – Korrelation, Regression `age` und `hhinc`

#### 4a – Pearson-Korrelation + Test

* **Ziel:**
  Linearen Zusammenhang zwischen Alter und Haushaltsnettoeinkommen beschreiben und testen.
* **Relevante Variablen:**

  * `age` (metrisch).
  * `hhinc` (metrisch).
* **Statistische Methoden:**

  * Pearson-Korrelation (r) und Signifikanztest H₀: ρ = 0.
  * Interpretation von r und p-Wert.
* **Rolle der Messniveaus:**

  * Beide metrisch → Pearson-Korrelation zulässig.
  * Mögliche Schiefe/Outlier der Einkommensverteilung in der Interpretation reflektieren.

---

#### 4b – Streudiagramm mit kausaler Deutungsidee

* **Ziel:**
  Streudiagramm als Grundlage für eine kausale Interpretation (oder bewusste Nicht-Kausalität) nutzen.
* **Relevante Variablen:**

  * `age` → X-Achse (potentielle „Ursache“).
  * `hhinc` → Y-Achse (potentielle „Wirkung“).
* **Statistische Methoden:**

  * Streudiagramm mit Alter auf x-, Einkommen auf y-Achse.
  * Evtl. schon Regressionsgerade einzeichnen (visuell).
* **Rolle der Messniveaus:**

  * Wieder metrisch; wichtig ist hier, die **Annahme** einer kausalen Richtung zu diskutieren (Daten allein beweisen sie nicht).

---

#### 4c – Einfache lineare Regression `hhinc ~ age`

* **Ziel:**
  Lineares Regressionsmodell schätzen, interpretieren und für Prognosen nutzen.
* **Relevante Variablen:**

  * `age` – Prädiktor X (metrisch).
  * `hhinc` – Zielvariable Y (metrisch).
* **Statistische Methoden:**

  * Schätzung von β₀ und β₁, Bestimmtheitsmaß R², Test auf β₁ ≠ 0.
  * Prognose des Einkommens für exemplarische Alterswerte (nur im beobachteten Bereich).
  * Einzeichnen der Regressionsgerade in das Streudiagramm.
* **Rolle der Messniveaus:**

  * Metrische Skala zwingend nötig für dieses lineare Modell.
  * Interpretation der Steigung als durchschnittlicher Einkommenszuwachs pro Jahr Alter (unter starken Vereinfachungen).

---

### Aufgabe 5 – ANOVA `gd02` nach `hs01`

#### 5a – Gruppenbildung und Überblick

* **Ziel:**
  Die Gruppen nach Gesundheitszustand bilden und Basisstatistiken der Wohndauer pro Gruppe betrachten.
* **Relevante Variablen:**

  * `hs01` – Gesundheitszustand (ordinal; Faktor in der ANOVA).
  * `gd02` – Wohndauer im Ort (metrisch, z. B. Jahre; „Unter 1 Jahr“ → 0).
* **Statistische Methoden:**

  * Gruppengrößen je `hs01`.
  * Mittelwert und SD von `gd02` je Gruppe.
* **Rolle der Messniveaus:**

  * `hs01` ordinal, aber als kategorialer Faktor genutzt.
  * `gd02` metrisch → geeignet für Mittelwerte und ANOVA.

---

#### 5b – Unabhängigkeit der Gruppen argumentieren

* **Ziel:**
  Zeigen, dass ANOVA-Voraussetzung „unabhängige Gruppen“ plausibel erfüllt ist.
* **Relevante Variablen:**

  * `hs01`, evtl. Personen-ID (falls vorhanden).
* **Statistische Inhalte:**

  * Jede Person genau in einer `hs01`-Kategorie.
  * Keine Mehrfachmessungen pro Person.
  * Keine inhaltlichen Kopplungen zwischen Personen/Haushalten (nur grob diskutiert).

---

#### 5c – Einfaktorielle ANOVA + Post-Hoc bei α = 0,20

* **Ziel:**
  Prüfen, ob sich die mittlere Wohndauer im Ort (`gd02`) zwischen Gesundheitsgruppen unterscheidet und welche Gruppen sich unterscheiden.
* **Relevante Variablen:**

  * `hs01` (Faktor).
  * `gd02` (metrische Zielvariable).
* **Statistische Methoden:**

  * Einfaktorielle ANOVA H₀: alle Mittelwerte gleich.
  * Signifikanzniveau α = 0,20 (explizit so interpretieren).
  * Post-Hoc-Vergleiche (z. B. Tukey) zur Identifikation signifikanter Gruppenpaare.
  * Diskussion: wie sich α = 0,05 oder α = 0,40 auf Testergebnisse auswirken würde.
* **Rolle der Messniveaus:**

  * Metrische Zielvariable, kategorialer Faktor → klassisches ANOVA-Setting.
  * Ordinalität von `hs01` kann in der Interpretation genutzt werden („tendenziell schlechterer Gesundheitszustand → ...?“).

---

## 2. Schritt-für-Schritt-Plan für die Bearbeitung mit Python

*(ausgehend von deinem aktuellen Stand: Struktur + Basis-Pipeline funktionieren)*

### 2.1 Vorbereitung (ist bei dir weitgehend erledigt)

1. **Projektstruktur & Environment**

   * Repo-Struktur wie vereinbart (data/, src/, figures/, latex/, …) – ✔️
   * Virtuelle Umgebung und `requirements.txt` vorhanden – ✔️
   * Typische Pakete:

     * `pandas`, `numpy` (Daten, Kennwerte)
     * `matplotlib` (Plots)
     * `scipy` (Tests, Korrelationen)
     * `statsmodels` (Regression, ANOVA, Post-Hoc)

2. **Basislauf testen**

   * `python src/run_all.py` ausführen.
   * Prüfen, dass:

     * Rohdaten eingelesen werden.
     * eine erste Kopie unter `data/processed/` entsteht.
     * die Block-1-Variablen (`mc04`, `ep04`, `hhinc`) gefunden werden.

---

### 2.2 Datenimport & -bereinigung in Python

**Ziel:** saubere, einheitliche Datengrundlage `allbus_clean.csv`, auf der alle Aufgaben 1–5 arbeiten.

1. **`data_prep.py` erweitern – Eingangs-Daten bereinigen**

   * Sonderwerte/negative Werte bei `hhinc` in `NaN` verwandeln.
   * `gd02`: „Unter 1 Jahr“ → 0, Rest zu numerischem Typ.
   * Auswahl deiner relevanten Variablen (mc04, ep01, ep04, fe14, xt10, age, lm02, hhinc, hs01, gd02, plus evtl. Gruppierungsvariablen wie `sex`) und eventuell unnötige Spalten droppen.

2. **Datentypen setzen**

   * `mc04`, `ep01`, `ep04`, `fe14`, `hs01`, Gruppierungsvariable (z. B. `sex`) → kategorische Variablen (`category` oder int mit beschrifteter Bedeutung).
   * `hhinc`, `lm02`, `gd02`, `xt10`, `age` → numerisch (`float`/`int`).

3. **Fehlende Werte-Strategie**

   * Grundsatz: Für jede Analyse nur vollständige Fälle der jeweils benötigten Variablen verwenden (listwise deletion).
   * Optional in `data_prep.py`: einfache Checks wie Anzahl fehlender Werte pro Variable als Zusammenfassung ausgeben.

4. **Bereinigten Datensatz speichern**

   * `allbus_clean.csv` (oder ähnlicher Name) in `data/processed/`.
   * Abschließend: `python src/data_prep.py` ausführen, sicherstellen, dass `allbus_clean.csv` existiert und plausibel aussieht.

---

### 2.3 Analyseschritte je Aufgabe

Für alle Blöcke:

* Verwende `pandas` zum Rechnen/Tabellen.
* Verwende `matplotlib` für Plots.
* Verwende `scipy` und `statsmodels` für Korrelationen, Tests, Regression, ANOVA.

---

#### Block 1 – Univariante Deskription (`block1_univariat.py`)

**Ziel:** Aufgaben 1b–1d vollständig abdecken.

1. **1b – Skalenniveaus erklären (Textarbeit, wenig Code)**

   * Aus `allbus_clean` die Spalteninfos holen (unique Werte der Variablen).
   * In deinem LaTeX-Text: Definition nominal/ordinal/metrisch + Zuordnung:

     * `mc04` → nominal
     * `ep04` → ordinal
     * `hhinc` → metrisch

2. **1c – Analyse von `ep04`**

   * Häufigkeitstabelle (`value_counts`, mit relativen Häufigkeiten).
   * Tabelle nach `latex/tables/ep04_freq.tex` exportieren.
   * Balkendiagramm in `figures/block1/ep04_bar.pdf` speichern.
   * Modus & Median berechnen (für Text).

3. **1d – Analyse von `hhinc`**

   * `hhinc`-Verteilung prüfen (Min/Max, ggf. Boxplot).
   * Klassenbildung (z. B. mit `pd.cut`).
   * Häufigkeitstabelle je Klasse -> `latex/tables/hhinc_classes.tex`.
   * Histogramm (`matplotlib`) -> `figures/block1/hhinc_hist.pdf`.
   * Mittelwert & Standardabweichung berechnen und in Tabelle/LaTeX übernehmen.

---

#### Block 2 – Bivariate Deskription (`block2_bivariat.py`)

**Ziel:** Aufgaben 2a–2c.

1. **2a – `ep01` × `fe14`**

   * Kreuztabelle (`pd.crosstab(ep01, fe14, normalize='index' oder 'all'`).
   * Tabelle nach `latex/tables/ep01_fe14_crosstab.tex`.
   * Mosaikdiagramm (z. B. über `statsmodels.graphics.mosaicplot`).
   * Spearman-Rangkorrelation (`scipy.stats.spearmanr`) und Kennwerte notieren.

2. **2b – `xt10` & `age`**

   * Streudiagramm (`plt.scatter`) -> `figures/block2/xt10_age_scatter.pdf`.
   * Pearson-Korrelation (`scipy.stats.pearsonr`).
   * Kleine Tabelle mit r, p, n → `latex/tables/xt10_age_corr.tex`.

3. **2c – Korrelation vs. Kausalität**

   * Im Code nur ggf. Kennwerte speichern;
   * Hauptarbeit in LaTeX: strukturiert erläutern, warum r ≠ 0 noch keine Kausalität beweist.
   * Auf alternative Erklärungen für den Zusammenhang hinweisen.

---

#### Block 3 – Konfidenzintervall & t-Test (`block3_tests.py`)

**Ziel:** Aufgaben 3a–3c.

1. **3a – Population vs. Stichprobe**

   * Eher Textteil, aber du kannst im Skript:

     * Stichprobengröße `n = len(allbus_clean)` berechnen.
     * Evtl. ein paar Grundstatistiken zur Stichprobe ausgeben (z. B. Altersmittelwert).

2. **3b – 95 %-CI für `lm02`**

   * n, Mittelwert, SD von `lm02` aus `allbus_clean` berechnen.
   * 95 %-CI (z. B. mit t-Quantil aus `scipy.stats.t.ppf`).
   * Tabelle mit Mittelwert, SD, CI-Grenzen nach `latex/tables/lm02_ci.tex`.

3. **3c – t-Test für zwei Gruppen**

   * Gruppierungsvariable (z. B. `sex`) auswählen.
   * Für jede Gruppe: n, Mittelwert, SD von `lm02` berechnen.
   * t-Test (`scipy.stats.ttest_ind`) durchführen.
   * Tabelle mit Gruppenstatistik + Testresultat nach `latex/tables/lm02_ttest_by_group.tex`.
   * Interpretation (H₀ verwerfen oder nicht) in LaTeX-Text schreiben.

---

#### Block 4 – Korrelation & Regression (`block4_regression.py`)

**Ziel:** Aufgaben 4a–4c.

1. **4a – Korrelation `age`–`hhinc`**

   * Pearson-Korrelation + p-Wert (`scipy.stats.pearsonr`).
   * Ausgabe in Tabelle → `latex/tables/age_hhinc_corr.tex`.

2. **4b – Streudiagramm + erste Interpretation**

   * Streudiagramm (x = age, y = hhinc) erstellen.
   * Datei: `figures/block4/age_hhinc_scatter.pdf`.
   * Optional: Punkte farbig nach einem kategorialen Merkmal einfärben (nur wenn du Lust auf Nice-to-have hast).

3. **4c – Regression `hhinc ~ age`**

   * Lineares Modell via `statsmodels` (`OLS`).
   * Regressionskoeffizienten, R², p-Werte aus dem Modell extrahieren.
   * Zusammenfassung als LaTeX-Tabelle (`latex/tables/age_hhinc_regression.tex`).
   * Regressionsgerade im Streudiagramm einzeichnen -> `figures/block4/age_hhinc_regline.pdf`.
   * Beispielprognose im LaTeX-Text interpretieren (z. B. für 30 oder 50 Jahre).

---

#### Block 5 – ANOVA (`block5_anova.py`)

**Ziel:** Aufgaben 5a–5c.

1. **5a – Gruppenüberblick**

   * `hs01`-Gruppengrößen (`value_counts`).
   * Mittelwert & SD von `gd02` je `hs01`.
   * Tabelle nach `latex/tables/gd02_by_hs01_descriptives.tex`.

2. **5b – Unabhängigkeit der Gruppen**

   * Sicherstellen, dass jede Person genau eine `hs01`-Kategorie hat (ggf. `nunique` einer Personen-ID).
   * Auswertung vor allem im Text (Warum unabhängige Gruppen plausibel sind).

3. **5c – Einfaktorielle ANOVA + Post-Hoc**

   * ANOVA: `gd02 ~ C(hs01)` via `statsmodels` (`ols` + `anova_lm`).
   * Fokus: Signifikanztest bei α = 0,20 interpretieren.
   * Post-Hoc: Tukey-Test (`pairwise_tukeyhsd`) → Tabelle nach `latex/tables/gd02_hs01_tukey.tex`.
   * Im Text diskutieren:

     * Welche Gruppenpaare signifikant sind.
     * Wie sich die Ergebnisse verändern würden, wenn du α = 0,05 bzw. 0,40 wählen würdest (Konzept: Fehler 1. Art vs. 2. Art).

---

### 2.4 Erstellung von Tabellen & Grafiken für LaTeX

1. **Tabellen**

   * Alle wichtigen Resultate (Häufigkeiten, Kreuztabellen, Kennwerte, Testergebnisse, Regression, ANOVA, Post-Hoc) als `DataFrame.to_latex(...)` in `latex/tables/` speichern.
   * Einheitliches Tabellenformat (z. B. `index=False`, saubere Spaltennamen).

2. **Grafiken**

   * Alle Plots als PDF (oder PNG) unter `figures/blockX/` speichern.
   * Einheitliches Layout: Achsentitel, sinnvolle Skalen, lesbare Tick-Labels.

3. **LaTeX-Integration**

   * Im LaTeX-Dokument nur noch referenzieren:

     * `\input{latex/tables/...}`
     * `\includegraphics[]{figures/...}`
   * Logik: Du änderst Code → Skript neu laufen lassen → LaTeX neu übersetzen → alles konsistent.

---

### 2.5 Qualitätssicherung / Plausibilitätschecks

1. **Vor jeder Auswertung**

   * Datenumfang (`n`) prüfen.
   * Verteilungen ansehen (Histogramme, Boxplots).
   * Auf offensichtliche Ausreißer achten (z. B. extrem hohe `xt10`, `lm02`, `hhinc`).

2. **Nach jeder Analyse**

   * Prüfen, ob Summen von relativen Häufigkeiten ≈ 1 sind.
   * Ob Gruppengrößen für Tests angemessen sind (z. B. nicht n=3 in einer ANOVA-Gruppe ohne Kommentar).
   * Ob Zeichen von Kodierungsfehlern auftauchen (z. B. `age` < 15 oder > 100).

3. **Dokumentation im Workbook**

   * Jede größere Bereinigungsentscheidung (z. B. „negative Einkommen als fehlend behandelt“) im Methoden- oder Datenkapitel kurz festhalten.
   * Auch ungewöhnliche Testeinstellungen (α = 0,20) explizit begründen und reflektieren.
