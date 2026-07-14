import flet as ft
from views.home import HomeView
from views.issue_renamer import IssueRenamerView


async def main(page: ft.Page):
    page.title = "Comic Processor"

    def route_change(route):
        page.views.clear()
        page.views.append(HomeView(page))

        if page.route == "/issue-renamer":
            page.views.append(IssueRenamerView(page))

        page.update()

    async def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    await page.push_route("/")
    route_change("/")


ft.run(main)