# State Pattern
#
# Allows an object to change its behavior when its internal state changes.

from abc import ABC, abstractmethod


class DrawingTool(ABC):
    def __init__(self, tool_name: str):
        self.tool_name = tool_name

    @abstractmethod
    def handle(self) -> None:
        raise NotImplementedError


class RectSelectionTool(DrawingTool):
    def __init__(self) -> None:
        super().__init__("RectSelectionTool")

    def handle(self) -> None:
        print("Select with a rectangle")


class CircleSelectionTool(DrawingTool):
    def __init__(self) -> None:
        super().__init__("CircleSelectionTool")

    def handle(self) -> None:
        print("Select with a circle")


class LassoSelectionTool(DrawingTool):
    def __init__(self) -> None:
        super().__init__("LassoSelectionTool")

    def handle(self) -> None:
        print("Select with a lasso")


class DrawingApp:
    def active_tool(self) -> str:
        return self._tool.tool_name

    def change_tool(self, tool: DrawingTool) -> None:
        self._tool = tool

    def use_tool(self) -> None:
        self._tool.handle()


# Client code
app = DrawingApp()

app.change_tool(RectSelectionTool())
app.use_tool()


app.change_tool(CircleSelectionTool())
app.use_tool()

app.change_tool(LassoSelectionTool())
app.use_tool()
