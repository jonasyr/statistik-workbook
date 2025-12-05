# Block 1: Univariate analysis (Tasks 1b-1d)
import pandas as pd
from config import DATA_PROCESSED


FILENAME_PROCESSED = "allbus_raw_copy.csv"

VARIABLES_BLOCK1 = ["mc04", "ep04", "hhinc"]


def load_processed() -> pd.DataFrame:
    path = DATA_PROCESSED / FILENAME_PROCESSED
    print(f"Lade processed data aus: {path}")
    df = pd.read_csv(path)
    print("Daten geladen. Form:", df.shape)
    return df


def check_variables_exist(df: pd.DataFrame) -> None:
    print("\n--- Check: Variablen für Block 1 ---")
    for var in VARIABLES_BLOCK1:
        if var in df.columns:
            print(f"OK   - {var} vorhanden.")
        else:
            print(f"FEHLT - {var} NICHT im Datensatz!")


def quick_value_glimpse(df: pd.DataFrame) -> None:
    print("\n--- Erste Werte deiner Variablen ---")
    for var in VARIABLES_BLOCK1:
        if var in df.columns:
            print(f"\nVariable: {var}")
            print(df[var].head(10))


def main():
    df = load_processed()
    check_variables_exist(df)
    quick_value_glimpse(df)


if __name__ == "__main__":
    main()

