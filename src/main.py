import asyncio
import flet as ft
from train_calc import braking_percent

VERSION = "ALPHA 0.1"


async def main(page: ft.Page) -> None:
    """Flet application entry point."""
    page.title = "TSW Zugdatenberechner"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    progress = ft.ProgressRing(width=20, height=20, visible=False)
    result_text = ft.Text("")

    async def calculate(e):
        progress.visible = True
        progress.update()
        await asyncio.sleep(1)
        train_weight = 400  # t
        braking_weight = 256  # t
        brh = braking_percent(train_weight, braking_weight)
        result_text.value = (
            f"Brems Hundertstel des fiktiven Zuges: {brh:.0f} BrH"
        )
        result_text.update()
        print(result_text.value)
        progress.visible = False
        progress.update()

    async def clear(e):
        result_text.value = ""
        result_text.update()

    page.appbar = ft.AppBar(
        leading=ft.Image(src="assets/tsw-calculator-logo.png", width=40, height=40),
        title=ft.Text("TSW Zugdatenberechner"),
        center_title=False,
        actions=[ft.Text(VERSION, size=10, color=ft.colors.ON_SURFACE_VARIANT)],
    )

    buttons_row = ft.Row(
        controls=[
            ft.ElevatedButton("Calculate", on_click=calculate),
            ft.ElevatedButton("Clear", on_click=clear),
            progress,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    content = ft.Container(
        content=ft.Column([buttons_row, result_text]),
        animate_opacity=ft.Animation(500, "ease"),
        opacity=0,
    )

    page.add(content)
    page.update()

    # Fade in content on start
    content.opacity = 1
    content.update()

    # Perform an initial calculation for a fictitious train
    await calculate(None)


if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.WEB_BROWSER,
        port=8080,
        host="0.0.0.0",
        assets_dir="assets",
    )
