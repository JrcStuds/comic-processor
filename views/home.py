import flet as ft



class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/",
            controls=[
                ft.Text("This is the app"),
                ft.Button(
                    content="button",
                    on_click=self.go_to_issue_renamer
                )
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )


    async def go_to_issue_renamer(self):
        await self.page.push_route("/issue-renamer")