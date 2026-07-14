import os, zipfile, tempfile, shutil, asyncio
import flet as ft
import xml.etree.ElementTree as ET
from services.issue_renamer import parse_name



class IssueRenamerView(ft.View):
    def __init__(self, page: ft.Page):

        self.files = []
        self.save_path = None
        self.temp_folder = tempfile.mkdtemp()
        print(f"Temp dir at {self.temp_folder}")

        self.content = ft.Column(
            controls=[
                ft.Button(
                    content="Select Files",
                    on_click=self.handle_pick_files
                ),
                ft.Button(
                    content="Select Directory",
                    on_click=self.handle_select_directory
                ),
                ft.Button(
                    content="Process Files",
                    on_click=self.process_files
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        super().__init__(
            route="/issue-renamer",
            controls=[
                ft.SafeArea(self.content)
            ]
        )
    

    async def handle_pick_files(self, e: ft.Event[ft.Button]):
        files = await ft.FilePicker().pick_files(allow_multiple=True)
        for file in files:
            if file.name not in self.files:
                new_cache_path = os.path.join(self.temp_folder, file.name)
                shutil.copy2(file.path, new_cache_path)
                self.files.append(file.name)


    async def handle_select_directory(self, e: ft.Event[ft.Button]):
        self.save_path = await ft.FilePicker().get_directory_path()


    async def process_files(self, e):
        
        self.master_zip_path = os.path.join(self.temp_folder, "export.zip")
        with zipfile.ZipFile(self.master_zip_path, "w", zipfile.ZIP_DEFLATED) as master:

            for file in os.listdir(self.temp_folder):
                if file != "export.zip":
                    file_path = os.path.join(self.temp_folder, file)
                    new_name = parse_name(file_path)
                    master.write(file_path, new_name)
        
        shutil.copy2(self.master_zip_path, self.save_path)

        shutil.rmtree(self.temp_folder)
        self.files = {}
        self.save_path = None

