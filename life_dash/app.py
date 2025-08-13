from textual.app import App, ComposeResult
from textual.containers import Grid

class LifeDashApp(App):
    CSS_PATH = "app.css"

    def compose(self) -> ComposeResult:
        yield Grid(id="main-grid")

if __name__ == "__main__":
    LifeDashApp().run()
