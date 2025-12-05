# Data preparation: Reading and cleaning data
import pandas as pd
from config import DATA_RAW, DATA_PROCESSED


# Dateiname der Rohdaten (ggf. anpassen)
FILENAME_RAW = "ALLBUS_2021_teildatensatz.xlsx"
FILENAME_PROCESSED = "allbus_raw_copy.csv"


def load_raw_data() -> pd.DataFrame:
    """
    Liest den ALLBUS-Teildatensatz aus data/raw ein.
    """
    raw_path = DATA_RAW / FILENAME_RAW
    print(f"Lade Rohdaten aus: {raw_path}")
    df = pd.read_excel(raw_path)
    print("Rohdaten geladen. Form:", df.shape)
    return df


def quick_overview(df: pd.DataFrame) -> None:
    """
    Gibt einen sehr groben Überblick über den Datensatz.
    """
    print("\n--- Erste fünf Zeilen ---")
    print(df.head())

    print("\n--- Spalten (erste 20) ---")
    print(list(df.columns)[:20])

    print("\n--- Info ---")
    print(df.info())


def save_basic_copy(df: pd.DataFrame) -> None:
    """
    Speichert eine 1:1-Kopie als CSV in data/processed.
    """
    out_path = DATA_PROCESSED / FILENAME_PROCESSED
    df.to_csv(out_path, index=False)
    print(f"\nKopie der Rohdaten gespeichert unter: {out_path}")


def main():
    df = load_raw_data()
    quick_overview(df)
    save_basic_copy(df)


if __name__ == "__main__":
    main()
