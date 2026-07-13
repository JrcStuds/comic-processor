import flet as ft



class IssueRenamerView(ft.View):
    def __init__(self, page: ft.Page):

        file_picker = ft.FilePicker()


        async def handle_pick_files(e):
            files = await file_picker.pick_files(allow_multiple=True)


        super().__init__(
            route="/issue-renamer",
            controls=[
                ft.Button(
                    content="Select Files",
                    on_click=handle_pick_files
                )
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )