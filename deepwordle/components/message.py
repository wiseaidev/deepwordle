"""
| The following script contains all the necessary logic required for the message panel widget.

| This program and the accompanying materials are made available under the terms of the `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""
from rich.align import (
    Align,
)
from rich.console import (
    Console,
    RenderableType,
)
from rich.panel import (
    Panel,
)
from rich.style import (
    Style,
)
from rich.text import (
    Text,
)
from textual.app import (
    App,
)
from textual.reactive import (
    Reactive,
)
from textual.views import (
    DockView,
)
from textual.widget import (
    Widget,
)
from textual.widgets import (
    Footer,
    Header,
)
from typing import (
    Optional,
    Union,
)

from deepwordle.components.rich_text import (
    FigletText,
)


class MessagePanel(Widget):

    _content: Reactive[str] = Reactive("")
    _figlet: Reactive[bool] = Reactive(False)
    _font_name: Reactive[str] = Reactive("")
    _color: Union[str, Style] = Reactive("")

    def __init__(
        self,
        content: str,
        figlet: Optional[bool] = False,
        font_name: Optional[str] = "small",
        style: Optional[str] = "bold",
    ) -> None:
        super().__init__(self.__class__.__name__)
        self.content: str = content
        self.figlet: Optional[bool] = figlet
        self.font_name: Optional[str] = font_name
        self.color: Union[str, Style] = style

    @property
    def content(self) -> str:
        """
        A getter method that returns the value of the `content` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `content` attribute.
        """
        if not hasattr(self, "_content"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named content."
            )
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        """
        A setter method that changes the value of the `content` attribute.
        :param value: A string that represents the value of the `content` attribute.
        :return: None.
        """
        setattr(self, "_content", value)

    @property
    def figlet(self) -> Optional[bool]:
        """
        A getter method that returns the value of the `figlet` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `figlet` attribute.
        """
        if not hasattr(self, "_figlet"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named figlet."
            )
        return self._figlet

    @figlet.setter
    def figlet(self, value: str) -> None:
        """
        A setter method that changes the value of the `figlet` attribute.
        :param value: A string that represents the value of the `figlet` attribute.
        :return: None.
        """
        setattr(self, "_figlet", value)

    @property
    def font_name(self) -> Optional[str]:
        """
        A getter method that returns the value of the `font_name` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `font_name` attribute.
        """
        if not hasattr(self, "_font_name"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named font_name."
            )
        return self._font_name

    @font_name.setter
    def font_name(self, value: str) -> None:
        """
        A setter method that changes the value of the `font_name` attribute.
        :param value: A string that represents the value of the `font_name` attribute.
        :return: None.
        """
        setattr(self, "_font_name", value)

    @property
    def color(self) -> Union[str, Style]:
        """
        A getter method that returns the value of the `color` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `color` attribute.
        """
        if not hasattr(self, "_color"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named color."
            )
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        """
        A setter method that changes the value of the `color` attribute.
        :param value: A string that represents the value of the `color` attribute.
        :return: None.
        """
        setattr(self, "_color", value)

    def __repr__(self):
        ret = f"{self.__class__.__name__}(name='{self.name}', content='{self.content}',"
        ret += f" figlet='{self.figlet}', font_name='{self.font_name}', style='{self.style}')"
        return ret

    def render(self) -> RenderableType:
        renderable: Align
        if self.figlet:
            renderable = Align.center(
                FigletText(text=self.content, font_name=self.font_name),
                vertical="middle",
            )
        else:
            renderable = Align.center(
                Text(text=self.content, style=self.color), vertical="middle"
            )
        return Panel(renderable, style=self.color)


if __name__ == "__main__":
    message_panel = MessagePanel("Awesome Widget")
    assert message_panel.content == "Awesome Widget"
    print(message_panel)
    console = Console()
    console.print(message_panel)
    message_panel = MessagePanel("Awesome Widget", figlet=True, font_name="mini")
    console.print(message_panel)
    message_panel = MessagePanel(
        "Awesome Widget", figlet=True, font_name="small", style="green"
    )
    console.print(message_panel)
    # class MyApp(App):
    #     async def on_load(self) -> None:
    #         """Bind keys here."""
    #         await self.bind("q", "quit", "Quit")
    #     async def on_mount(self) -> None:
    #         view = await self.push_view(DockView())
    #         footer = Footer()
    #         #header = Header()
    #         #await view.dock(header, edge="top")
    #         await view.dock(footer, edge="bottom")
    #         await view.dock(MessagePanel("Awesome Widget"), edge="top", size=10)
    #         await view.dock(MessagePanel("Awesome Widget"), edge="left", size=30)
    #         await view.dock(MessagePanel("Awesome Widget"), edge="right", size=30)
    # MyApp.run(log="textual.log", title= "app")
