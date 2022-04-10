"""
| The following script contains all the necessary logic required for the grid of letters.

| This program and the accompanying materials are made available under the terms of the `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""

from textual import (
    events,
)
from textual.app import (
    App,
)
from textual.reactive import (
    Reactive,
)
from textual.views import (
    DockView,
    GridView,
)
from textual.widgets import (
    Footer,
    Header,
)
from typing import (
    List,
    Optional,
    TypeVar,
)

from deepwordle.components.constants import (
    LETTERS,
    MAX_ATTEMPTS,
    WORD_LENGTH,
)
from deepwordle.components.letter import (
    Letter,
)
from deepwordle.components.utils import (
    add_new_letter,
    remove_letter,
    update_letters_state,
)

L = TypeVar("L", bound=Letter)


class LettersGrid(GridView):
    """
    A widget that encapsulates the current_letters, the letters and the the max_letters of the grid.
    """

    _current_letters: Reactive[List[L]] = Reactive(
        default=None, layout=False, repaint=True
    )
    _letters: Reactive[List[L]] = Reactive(default=None, layout=False, repaint=True)
    _max_letters: Reactive[int] = Reactive(
        default=WORD_LENGTH * MAX_ATTEMPTS, layout=False, repaint=True
    )
    _letters_count: Reactive[int] = Reactive(default=0, layout=False, repaint=True)

    @property
    def current_letters(self) -> List[L]:
        """
        A getter method that returns the value of the `current_letters` attribute.
        :param self: Instance of the class.
        :return: A list of letters that represents the value of the `current_letters` attribute.
        """
        if not hasattr(self, "_current_letters"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named current_letters."
            )
        index: int = 0
        if self.letters_count is None:
            self.letters_count = 0
        index: int = int(self.letters_count / WORD_LENGTH) * WORD_LENGTH
        self._current_letters = self.letters[index : index + WORD_LENGTH]
        return self._current_letters

    @current_letters.setter
    def current_letters(self, value: List[L]) -> None:
        """
        A setter method that changes the value of the `current_letters` attribute.
        :param value: A list of letters that represents the value of the `current_letters` attribute.
        :return: None.
        """
        setattr(self, "_current_letters", value)

    @property
    def letters(self) -> List[L]:
        """
        A getter method that returns the value of the `letters` attribute.
        :param self: Instance of the class.
        :return: A list of letters that represents the value of the `letters` attribute.
        """
        if not hasattr(self, "_letters"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named letters."
            )
        return self._letters

    @letters.setter
    def letters(self, value: List[L]) -> None:
        """
        A setter method that changes the value of the `letters` attribute.
        :param value: A list of letters that represents the value of the `letters` attribute.
        :return: None.
        """
        setattr(self, "_letters", value)

    @property
    def max_letters(self) -> int:
        """
        A getter method that returns the value of the `letters` attribute.
        :param self: Instance of the class.
        :return: An integer that represents the value of the `letters` attribute.
        """
        if not hasattr(self, "_max_letters"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named max_letters."
            )
        return self._max_letters

    @max_letters.setter
    def max_letters(self, value: int) -> None:
        """
        A setter method that changes the value of the `max_letters` attribute.
        :param value: An integer that represents the value of the `max_letters` attribute.
        :return: None.
        """
        setattr(self, "_max_letters", value)

    @property
    def letters_count(self) -> int:
        """
        A getter method that returns the value of the `letters_count` attribute.
        :param self: Instance of the class.
        :return: An integer that represents the value of the `letters_count` attribute.
        """
        if not hasattr(self, "_letters_count"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named letters_count."
            )
        return self._letters_count

    @letters_count.setter
    def letters_count(self, value: int) -> None:
        """
        A setter method that changes the value of the `letters_count` attribute.
        :param value: An integer that represents the value of the `letters_count` attribute.
        :return: None.
        """
        if value:
            setattr(self, "_letters_count", value)

    def non_empty_letters(self) -> list[L]:
        """
        A helper method to return all the letters of a row that has character.
        """
        return [letter for letter in self.letters if letter.character]

    async def on_mount(self) -> None:
        # Make all the letters
        self.letters = [Letter("") for _ in range(WORD_LENGTH * MAX_ATTEMPTS)]
        self.letters_count = 0
        # Set basic grid settings
        # center of the DockView
        self.grid.set_align("center", "center")
        self.grid.set_gutter(1)
        self.grid.set_gap(1, 1)
        # Create rows / columns / areas
        self.grid.add_column("column", repeat=WORD_LENGTH, size=7)
        self.grid.add_row("row", repeat=MAX_ATTEMPTS, size=3)
        # Place out widgets in to the layout
        self.grid.place(*self.letters)

    def check_guess(self, answer: str) -> Optional[bool]:
        self.log("Checking for solution...")
        for letter in self.current_letters:
            if letter.character == "":
                return False
        current_guess = "".join(
            map(lambda letter: letter.character, self.current_letters)
        ).lower()
        # update the state of the letters on the grid.
        # in python, a list is passed by reference
        _ = update_letters_state(self.current_letters, answer.upper())
        # check if we reach the last row of the grid.
        if self.letters_count and self.letters_count < self.max_letters - 1:
            self.letters_count += 1
        return current_guess == answer


if __name__ == "__main__":

    class MyApp(App):
        result: Reactive[bool] = Reactive(default=False, layout=False, repaint=True)

        async def on_load(self) -> None:
            """Bind keys here."""
            await self.bind("q", "quit", "Quit")

        def on_key(self, event: events.Key) -> None:
            if not self.result:
                if event.key == "enter":
                    self.result = self.letters_grid.check_guess("react")
                    return
                elif event.key in LETTERS:
                    self.letters_grid.letters_count = add_new_letter(
                        self.letters_grid.letters,
                        self.letters_grid.letters_count,
                        event.key,
                    )
                    return
                elif event.key == "ctrl+h":
                    self.letters_grid.letters_count = remove_letter(
                        self.letters_grid.letters, self.letters_grid.letters_count
                    )
                    return
            else:
                return

        async def on_mount(self) -> None:
            view = await self.push_view(DockView(name="letters"))
            footer = Footer()
            header = Header(tall=False, clock=False)
            self.letters_grid = LettersGrid()
            await view.dock(self.letters_grid, edge="left", name="grid letters")
            await view.dock(header, edge="top")
            await view.dock(footer, edge="bottom")

    MyApp.run(log="textual.log", log_verbosity=2, screen=True, title="Letter App")
