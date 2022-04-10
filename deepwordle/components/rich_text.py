"""
| The following script contains all the necessary logic required for the
| figlet styled text.

| This program and the accompanying materials are made available under the
| terms of the `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""

import attr
from attrs import (
    field,
    frozen,
    validators,
)
from pyfiglet import (
    Figlet,  # type: ignore
)
from rich.console import (
    Console,
    ConsoleOptions,
    RenderResult,
)
from rich.text import (
    Text,
)
from typing import (
    Optional,
)


@frozen
@attr.s(auto_attribs=True, slots=True, init=False, repr=False)
class FigletText:

    _text: str = field(init=True, validator=validators.instance_of(str), converter=str)
    _font_name: Optional[str] = field(
        default="small", validator=validators.instance_of(str), converter=str
    )

    @property
    def text(self) -> str:
        """
        A getter method that returns the value of the `text` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `text` attribute.
        """
        if not hasattr(self, "_text"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named text."
            )
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        """
        A setter method that changes the value of the `text` attribute.
        :param value: A string that represents the value of the `text` attribute.
        :return: None.
        """
        setattr(self, "_text", value)

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

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        """Build a Rich renderable to render the Figlet text."""
        if min(options.max_width / 2, options.max_height) < 4:
            yield Text(self.text, style="bold")
        else:
            font = Figlet(font=self.font_name, width=options.max_width)
            yield Text(font.renderText(self.text).rstrip("\n"), style="bold")

    def __repr__(self) -> str:
        """
        A method that Return a formated string for a given FigletText instance.
        :param self: a reference for a given instance.
        :return: a formated string of attributes for a given instance.
        """
        return f"{self.__class__.__name__}(text='{self.text}')"


def main() -> int:
    figlet = FigletText(text="foo", font_name="mini")
    assert figlet.text == "foo"
    print(figlet)
    console = Console()
    console.print(figlet)
    console.print(FigletText(text="foo", font_name="small"))
    console.print(FigletText(text="foo", font_name="standard"))
    console.print(FigletText(text="foo", font_name="big"))
    return 0


if __name__ == "__main__":
    main()
