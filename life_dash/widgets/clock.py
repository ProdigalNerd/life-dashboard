from textual.widget import Widget
from textual.reactive import reactive
from datetime import datetime

class ClockWidget(Widget):
    time_str = reactive("")

    def on_mount(self):
        self.set_interval(1, self.update_time)

    def update_time(self):
        self.time_str = datetime.now().strftime("%H:%M:%S")

    def render(self):
        return f"[bold cyan]{self.time_str}[/bold cyan]"
