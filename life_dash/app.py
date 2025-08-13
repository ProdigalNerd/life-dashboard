from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static

from life_dash.widgets.clock import ClockWidget

class LifeDashApp(App):
    CSS_PATH = "app.css"

    def compose(self) -> ComposeResult:
        grid = Grid(id="main-grid")
        yield grid

    def on_mount(self):
        grid = self.query_one("#main-grid", Grid)

        grid.mount(ClockWidget(id="clock"), Static("Pomodoro placeholder", id="pomodoro"))
        grid.mount(Static("Agenda placeholder", id="agenda"), Static("Feed placeholder"))
        grid.mount(Static("[Q] Quit | [P] Pomodoro | [C] Commands", id="footer"))

if __name__ == "__main__":
    LifeDashApp().run()
