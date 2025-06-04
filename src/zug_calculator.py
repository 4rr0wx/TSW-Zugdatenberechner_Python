from typing import List, Dict


def berechne_zugdaten(waggons: List[Dict]) -> Dict[str, float | int | str]:
    """Calculate train mass, brake weight, brake ratio and PZB category."""
    gesamtmasse = 0.0
    gesamtbremsgewicht = 0.0
    gesamtlange = 0.0

    for w in waggons:
        gesamtmasse += w["masse"] * w["anzahl"]
        gesamtbremsgewicht += w["bremsgewicht"] * w["anzahl"]
        gesamtlange += w["laenge"] * w["anzahl"]

    brh = round((gesamtbremsgewicht / gesamtmasse) * 100)

    if brh > 111:
        zugart = "O"
    elif brh >= 67:
        zugart = "M"
    else:
        zugart = "U"

    return {
        "Zugmasse [t]": gesamtmasse,
        "Bremsgewicht [t]": gesamtbremsgewicht,
        "BRH [%]": brh,
        "PZB-Zugart": zugart,
        "Lange [m]": round(gesamtlange, 1),
    }
