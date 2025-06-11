import asyncio
import flet as ft

version_number = "ALPHA 0.1"


async def main(page: ft.Page):

    page.title = "TSW Zugdatenberechner"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    progress = ft.ProgressRing(width=20, height=20, visible=False)

    # Define the calculate function that will be called when the calculate button is clicked
    async def calculate(e):
        progress.visible = True
        progress.update()
        await asyncio.sleep(1)
        progress.visible = False
        progress.update()

    # Define the clear function that will be called when the clear button is clicked
    async def clear(e):
        print("Clearing...")


    # ---------------------------------------------

    page.appbar = ft.AppBar(
        leading=ft.Image(src="assets/tsw-calculator-logo.png", width=40, height=40),
        title=ft.Text("TSW Zugdatenberechner"),
        center_title=False,
        actions=[ft.Text(version_number, size=10, color=ft.colors.ON_SURFACE_VARIANT)],
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
        content=buttons_row,
        animate_opacity=ft.Animation(500, "ease"),
        opacity=0,
    )

    page.add(content)
    page.update()

    # Fade in content on start
    content.opacity = 1
    content.update()

if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.WEB_BROWSER,
        port=8080,
        host="0.0.0.0",
        assets_dir="assets",
    )


