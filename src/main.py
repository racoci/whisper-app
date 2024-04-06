from flet import *


def main(current_page: Page):
    def on_record_click(e):
        current_page.snack_bar = SnackBar(
            Text("start Record 5 second Now..", size=20, weight=FontWeight.BOLD),
            bgcolor="blue"
        )

    current_page.add(
        Column([
            Text("Grave um audio", size=30, weight=FontWeight.BOLD),
            Divider(),
            Text("Grave um audio de 5 segundos", size=20, weight=FontWeight.BOLD),
            ElevatedButton("Grave Aqui", bgcolor="red", color="white", on_click=on_record_click)
        ])
    )


app(target=main)
