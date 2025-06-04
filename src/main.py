import asyncio
import flet as ft

version_number = "ALPHA 0.1"


async def main(page: ft.Page):

    # Input fields for the train data
    train_type = ft.Dropdown(
        label="Zugart",
        options=[
            ft.dropdown.Option("Güterzug"),
            ft.dropdown.Option("Nahverkehr"),
            ft.dropdown.Option("Fernverkehr"),
        ],
        width=200,
    )

    mass_field = ft.TextField(label="Gesamtmasse (t)", width=200)
    length_field = ft.TextField(label="Länge (m)", width=200)

    brake_setting = ft.Dropdown(
        label="Bremsstellung",
        options=[ft.dropdown.Option("R"), ft.dropdown.Option("P"), ft.dropdown.Option("G")],
        width=200,
    )

    brake_weight_field = ft.TextField(label="Bremsgewicht (t)", width=200)

    result_text = ft.Text(value="")

    async def calculate(e):
        """Calculate brake ratio and PZB category."""
        try:
            mass = float(mass_field.value)
            brake_weight = float(brake_weight_field.value)
        except (TypeError, ValueError):
            result_text.value = "Ungültige Eingabe"
            await page.update_async()
            return

        ratio = (brake_weight / mass) * 100

        if ratio < 66.6:
            pzb_type = "U"
        elif ratio <= 111.1:
            pzb_type = "M"
        else:
            pzb_type = "O"

        result_text.value = (
            f"Bremsverhältnis: {ratio:.1f}%\nPZB-Zugart: {pzb_type}"
        )
        await page.update_async()

    async def clear(e):
        mass_field.value = ""
        length_field.value = ""
        brake_weight_field.value = ""
        train_type.value = None
        brake_setting.value = None
        result_text.value = ""
        await page.update_async()


#---------------------------------------------

    version = ft.Text(version_number, size=10, color="darkgray", text_align="right")


# Add the title and logo to the page
#TODO Fix logo implementation

    title = ft.Text("TSW Zugdatenberechner", size=50)
    logo = ft.Image("assets/tsw-calculator-logo.png", width=50, height=50)
    page.add(
        ft.Row([title, logo], alignment=ft.MainAxisAlignment.CENTER)
    )

    page.add(ft.Row([version], alignment=ft.MainAxisAlignment.END))

    page.add(
        ft.Column(
            [
                train_type,
                mass_field,
                length_field,
                brake_setting,
                brake_weight_field,
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


