# Configuration settings for the statistics workbook
from pathlib import Path

# Projektwurzel (z. B. .../statistik-workbook)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Wichtige Pfade
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
FIGURES_DIR = PROJECT_ROOT / "figures"
TABLES_DIR = PROJECT_ROOT / "latex" / "tables"

# Optional: Seed für Reproduzierbarkeit
RANDOM_SEED = 42


def ensure_directories():
    """
    Stellt sicher, dass alle wichtigen Verzeichnisse existieren.
    """
    for path in [DATA_RAW, DATA_PROCESSED, FIGURES_DIR, TABLES_DIR]:
        path.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    print("PROJECT_ROOT:", PROJECT_ROOT)
    ensure_directories()
    print("Verzeichnisse geprüft/angelegt.")

