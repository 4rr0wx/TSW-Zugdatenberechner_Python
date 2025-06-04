import asyncio
import flet as ft

from .zug_calculator import berechne_zugdaten

version_number = "ALPHA 0.1"


async def main(page: ft.Page):
    """Flet UI allowing custom train configurations."""

    wagons: list[dict] = []
    wagon_list = ft.Column()

    # input fields for a single vehicle
    bez_field = ft.TextField(label="Bezeichnung", width=150)
    anzahl_field = ft.TextField(label="Anzahl", width=80)
    masse_field = ft.TextField(label="Masse (t)", width=100)
    bg_field = ft.TextField(label="Bremsgewicht (t)", width=140)
    laenge_field = ft.TextField(label="Länge (m)", width=100)

    result_text = ft.Text(value="")

    async def add_wagon(e):
        try:
            w = {
                "bezeichnung": bez_field.value or "Unbekannt",
                "anzahl": int(anzahl_field.value),
                "masse": float(masse_field.value),
                "bremsgewicht": float(bg_field.value),
                "laenge": float(laenge_field.value),
            }
        except (TypeError, ValueError):
            result_text.value = "Ungültige Eingabe"
            await page.update_async()
            return

        wagons.append(w)
        wagon_list.controls.append(
            ft.Text(
                f"{w['bezeichnung']} x{w['anzahl']} - {w['masse']} t, {w['bremsgewicht']} t, {w['laenge']} m"
            )
        )
        bez_field.value = ""
        anzahl_field.value = ""
        masse_field.value = ""
        bg_field.value = ""
        laenge_field.value = ""
        result_text.value = ""
        await page.update_async()

    async def calculate(e):
        if not wagons:
            result_text.value = "Keine Fahrzeuge eingegeben"
            await page.update_async()
            return
        data = berechne_zugdaten(wagons)
        result_text.value = "\n".join(f"{k}: {v}" for k, v in data.items())
        await page.update_async()

    async def clear(e):
        wagons.clear()
        wagon_list.controls.clear()
        bez_field.value = ""
        anzahl_field.value = ""
        masse_field.value = ""
        bg_field.value = ""
        laenge_field.value = ""
        result_text.value = ""
        await page.update_async()

    version = ft.Text(version_number, size=10, color="darkgray", text_align="right")

    title = ft.Text("TSW Zugdatenberechner", size=50)
    logo = ft.Image("assets/tsw-calculator-logo.png", width=50, height=50)
    page.add(ft.Row([title, logo], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row([version], alignment=ft.MainAxisAlignment.END))

    page.add(
        ft.Column(
            [
                ft.Row([
                    bez_field,
                    anzahl_field,
                    masse_field,
                    bg_field,
                    laenge_field,
                    ft.ElevatedButton("Hinzufügen", on_click=add_wagon),
                ]),
                wagon_list,
                ft.Row(
                    [
                        ft.ElevatedButton("Berechnen", color="blue", on_click=calculate),
                        ft.ElevatedButton("Clear", color="red", on_click=clear),
                    ]
                ),
                result_text,
            ]
        )
    )

    page.update()


if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.WEB_BROWSER,
        port=8080,
        host="0.0.0.0",
        assets_dir="assets",
    )
