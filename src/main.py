import asyncio
import flet as ft

version_number = "ALPHA 0.1"


async def main(page: ft.Page):

# Define the calculate function that will be called when the calculate button is clicked
    async def calculate(e):
        print("Calculating...")
        await asyncio.sleep(1)
        print("Done!")

# Define the clear function that will be called when the clear button is clicked
    async def clear(e):
        print("Clearing...")


#---------------------------------------------

    version = ft.Text(version_number, size=10, color="darkgray", text_align="right")


# Add the title and logo to the page
#TODO Fix logo implementation

    title = ft.Text("TSW Zugdatenberechner", size=50)
    logo = ft.Image("assets/tsw-calculator-logo.png", width=50, height=50)
    page.add(
        ft.Row([title,
                logo
                ], alignment=ft.MainAxisAlignment.CENTER)
    )

    page.add(ft.Row([version], alignment=ft.MainAxisAlignment.END))



# Add controls to the page
    page.add(
        ft.Row(controls=[
            ft.ElevatedButton("Calculate", color="blue", on_click=calculate),
            ft.ElevatedButton("Clear", color="red", on_click=clear)
        ])
    )


    page.update()

ft.app(target=main)


