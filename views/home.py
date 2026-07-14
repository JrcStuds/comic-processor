import flet as ft



class HomeView(ft.View):
    def __init__(self, page: ft.Page):

        self.content = ft.Column(
            controls=[
                ft.Text("This is the Home View"),
                ft.Button(
                    content="Go to Issue Renamer",
                    on_click=self.goto_issue_renamer
                )
            ]
        )

        super().__init__(
            route="/",
            controls=[ft.SafeArea(self.content)]
        )
    

    async def goto_issue_renamer(self, e):
        await self.page.push_route("/issue-renamer")