"""Command line tool to calculate train data from custom wagon configurations."""

from typing import List, Dict

from .zug_calculator import berechne_zugdaten


def eingabe_waggon() -> Dict:
    """Prompt the user for wagon data and return a dictionary."""
    print("\nNeues Fahrzeug hinzufugen")
    bez = input("Bezeichnung: ").strip() or "Unbekannt"
    anzahl = int(input("Anzahl: "))
    masse = float(input("Masse pro Stuck (t): "))
    bremsgewicht = float(input("Bremsgewicht pro Stuck (t): "))
    laenge = float(input("Lange pro Stuck (m): "))
    return {
        "bezeichnung": bez,
        "anzahl": anzahl,
        "masse": masse,
        "bremsgewicht": bremsgewicht,
        "laenge": laenge,
    }


def main():
    print("Benutzerdefinierter Zugdatenrechner")
    waggons: List[Dict] = []

    while True:
        waggons.append(eingabe_waggon())
        mehr = input("Weiteres Fahrzeug hinzufugen? (j/n): ").strip().lower()
        if mehr != "j":
            break

    daten = berechne_zugdaten(waggons)

    print("\nErgebnis:")
    for k, v in daten.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
