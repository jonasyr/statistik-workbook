# Master script: Runs all analysis blocks in sequence
from config import ensure_directories
import data_prep
import block1_univariat


def main():
    print("=== Schritt 1: Verzeichnisse prüfen ===")
    ensure_directories()

    print("\n=== Schritt 2: Rohdaten -> processed Kopie ===")
    data_prep.main()

    print("\n=== Schritt 3: Test Block 1 (Variablencheck) ===")
    block1_univariat.main()

    print("\n=== Basis-Pipeline abgeschlossen. ===")


if __name__ == "__main__":
    main()

