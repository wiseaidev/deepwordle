"""
| The following script contains all the necessary logic required for the letter button.

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
    ConsoleRenderable,
    RenderableType,
    RichCast,
)
from rich.padding import (
    Padding,
)
from rich.style import (
    Style,
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
from textual.widgets import (
    Button,
    Footer,
    Header,
)
from typing import (
    Literal,
    Optional,
    Union,
)

from deepwordle.components.constants import (
    IS_IN_POSITION,
    IS_IN_WORD,
    LETTER_COLORS,
    NOT_IN_WORD,
)
from deepwordle.components.rich_text import (
    FigletText,
)


class Letter(Button):
    """
    A widget that encapsulates the character, the state and the the style for each letter.
    """

    _character: Reactive[RenderableType] = Reactive(
        default="", layout=False, repaint=True
    )
    _state: Reactive[Literal[NOT_IN_WORD, IS_IN_WORD, IS_IN_POSITION]] = Reactive(
        default=NOT_IN_WORD, layout=False, repaint=True
    )
    _color: Reactive[Union[str, Style]] = Reactive(
        default=LETTER_COLORS[NOT_IN_WORD], layout=False, repaint=True
    )
    _font_name: Reactive[Literal["mini", "small", "standard", "big"]] = Reactive(
        default="mini", layout=False, repaint=True
    )

    def __init__(
        self, character: str, state: int = NOT_IN_WORD, font_name: str = "small"
    ):
        super().__init__(character)
        self.character = character
        self.state = state
        self.color = LETTER_COLORS[state]
        self.font_name = font_name

    @property
    def character(self) -> Union[ConsoleRenderable, RichCast, str]:
        """
        A getter method that returns the value of the `character` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `character` attribute.
        """
        if not hasattr(self, "_character"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named character."
            )
        return self._character

    @character.setter
    def character(self, value: str) -> None:
        """
        A setter method that changes the value of the `character` attribute.
        :param value: A string that represents the value of the `character` attribute.
        :return: None.
        """
        setattr(self, "_character", value)

    @property
    def state(self) -> int:
        """
        A getter method that returns the value of the `state` attribute.
        :param self: Instance of the class.
        :return: An integer that represents the value of the `state` attribute.
        """
        if not hasattr(self, "_state"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named state."
            )
        return self._state

    @state.setter
    def state(self, value: int) -> None:
        """
        A setter method that changes the value of the `state` attribute.
        :param value: An integer that represents the value of the `state` attribute.
        :return: None.
        """
        setattr(self, "_state", value)

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

    @property
    def font_name(self) -> str:
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

    def __repr__(self) -> str:
        """
        A method that Return a formated string for a given FigletText instance.
        :param self: a reference for a given instance.
        :return: a formated string of attributes for a given instance.
        """
        state: str
        if self.state == NOT_IN_WORD:
            state = "Not in word"
        elif self.state == IS_IN_WORD:
            state = "In word"
        elif self.state == IS_IN_POSITION:
            state = "In position"
        ret = f"{self.__class__.__name__}(character='{self.character}', state='{state}'"
        ret += f", color='{self.color}', font='{self.font_name}')"
        return ret

    def render(self) -> RenderableType:
        """Build a Rich renderable to render the calculator display."""
        # change the style according to the state
        if self.color != LETTER_COLORS[self.state]:
            self.color = LETTER_COLORS[self.state]
        renderable = Align.center(
            FigletText(text=self.character, font_name=self.font_name), vertical="middle"
        )
        return Padding(
            renderable,
            pad=(1, 1, 1, 1),
            style=self.color,
            expand=True,
        )


if __name__ == "__main__":
    letter_a = Letter("A", 0, "mini")
    letter_b = Letter("B", 1, "big")
    letter_c = Letter("C", 2, "standard")
    letter_d = Letter("D")
    tuple(map(print, [letter_a, letter_b, letter_c, letter_d]))
    assert letter_a.state == 0
    assert letter_b.state == 1
    assert letter_c.state == 2
    assert letter_d.state == 0
    assert letter_a.character == "A"
    assert letter_b.character == "B"
    assert letter_c.character == "C"
    assert letter_d.character == "D"
    console = Console()
    tuple(map(console.print, [letter_a, letter_b, letter_c, letter_d]))
    # class MyApp(App):
    #     async def on_load(self) -> None:
    #         """Bind keys here."""
    #         await self.bind("q", "quit", "Quit")
    #     async def on_mount(self) -> None:
    #         view = await self.push_view(DockView(name="letters"))
    #         footer = Footer()
    #         header = Header(tall=False, clock=False)
    #         await view.dock(header, edge="top")
    #         await view.dock(footer, edge="bottom")
    #         #await view.dock(Placeholder(name="header", height=2), edge="top", size=5, name="header")
    #         #await view.dock(Placeholder(name="a"), edge="left", size=30)
    #         #await view.dock(Placeholder(), edge="right", size=30, name="a")
    #         #await view.dock(Placeholder(), edge="bottom", size=30, name="footer")
    #         await view.dock(letter_a, edge="left", size=33, z=-1, name="letter a")
    #         await view.dock(letter_b, edge="left", size=33, z=-1, name="letter b")
    #         await view.dock(letter_c, edge="left", size=33, z=-1, name="letter c")
    #         await view.dock(letter_d, edge="left", size=33, z=-1, name="letter d")
    # MyApp.run(log="textual.log", log_verbosity=2, screen=True, title= "Letter App")
