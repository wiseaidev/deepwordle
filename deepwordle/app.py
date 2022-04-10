"""
| The following script is an entry point for our application.

| This program and the accompanying materials are made available under the
| terms of the `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""
import asyncio
import nest_asyncio
import random
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
)
from textual.widgets import (
    Footer,
    Header,
)
from typing import (
    Optional,
)

from deepwordle.audio_record import (
    AudioRecorder,
)
from deepwordle.components import (
    CUBES,
    LETTERS,
    LettersGrid,
    MessagePanel,
    add_new_letter,
    get_day_index,
    read_from_file,
    remove_letter,
    update_letters_state,
)
from deepwordle.transcribe import (
    Recognizer,
)
from deepwordle.twitter import (
    Twitter,
)

nest_asyncio.apply()


class MainApp(App):
    _result: Reactive[bool] = Reactive(False)
    _end: Reactive[bool] = Reactive(False)

    @property
    def result(self) -> Reactive[bool]:
        """
        A getter method that returns the value of the `result` attribute.
        :param self: Instance of the class.
        :return: A boolean that represents the value of the `result` attribute.
        """
        if not hasattr(self, "_result"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named result."
            )
        return self._result

    @result.setter
    def result(self, value: Reactive[bool]) -> None:
        """
        A setter method that changes the value of the `result` attribute.
        :param value: A boolean that represents the value of the `result` attribute.
        :return: None.
        """
        setattr(self, "_result", value)

    @property
    def end(self) -> Reactive[bool]:
        """
        A getter method that returns the value of the `end` attribute.
        :param self: Instance of the class.
        :return: A boolean that represents the value of the `end` attribute.
        """
        if not hasattr(self, "_end"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named end."
            )
        return self._end

    @end.setter
    def end(self, value: Reactive[bool]) -> None:
        """
        A setter method that changes the value of the `end` attribute.
        :param value: A boolean that represents the value of the `end` attribute.
        :return: None.
        """
        setattr(self, "_end", value)

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("q", "quit", "Quit")
        await self.bind("t", "tweet", "Tweet")
        await self.bind("r", "None", "Record")

    def on_key(self, event: events.Key) -> None:
        if self.letters_grid.letters_count == 5 * 6 - 1:
            self.end = True
        if not self.result and not self.end:
            self.message.content = "Press `r` to start recording audio..."
            if event.key == "r":
                self.process_recording(duration=2)

            if event.key == "enter":
                self.result = self.check_guess()
                return

            elif event.key == "ctrl+h":
                self.letters_grid.letters_count = remove_letter(
                    self.letters_grid.letters, self.letters_grid.letters_count
                )
                return
        else:
            return

    def watch__result(self, value) -> None:
        if value is True:
            self.message.content = "You Win!\nPress `t` to tweet your result."

    def watch__end(self, value) -> None:
        if value is True:
            self.message.content = f"The answer is: {self.secret}"

    def check_guess(self) -> bool:
        current_letters = self.letters_grid.current_letters
        current_word = "".join(
            map(lambda letter: letter.character, current_letters)
        ).lower()
        if len(current_word) < 5:
            self.message.content = "Not enough letters"
            return False
        if (
            current_word not in self.guesses_list
            and current_word not in self.answers_list
        ):
            self.message.content = "Not in word list"
            return False
        result = self.letters_grid.check_guess(self.secret)
        return result

    def process_recording(self, duration=2):
        self.message.content = f"Recording audio for {duration} seconds..."
        self.audio_recorder.record(duration)
        self.message.content = "Transcribing audio data..."
        result = self.loop.run_until_complete(self.recognizer.recognize())
        words = result["results"]["channels"][0]["alternatives"][0]["words"]
        word = ""
        if len(words) > 0:
            word = words[0]["word"]
            if len(word) == 5:
                self.message.content = (
                    f"You said {word}.\nPress:\n  ↵ to submit your word."
                )
                self.message.content += "\n  ← to remove your letters."
                self.construct_letters_from_word(word)
            else:
                self.message.content = (
                    f"You said `{word}` which is not a five letters word."
                )
                self.message.content += "\nPress `r` and try again."
        else:
            self.message.content = (
                f"You said `{word}` which is not a five letters word."
            )
            self.message.content += "\nPress `r` and try again."

    def construct_letters_from_word(self, word=""):
        for letter in word:
            self.letters_grid.letters_count = add_new_letter(
                self.letters_grid.letters, self.letters_grid.letters_count, letter
            )

    def action_tweet(self) -> None:
        if self.result:
            letters = self.letters_grid.non_empty_letters()
            numerator = len(letters) // 5 if self.result else "x"
            result = "Wordle {index} {numerator}/6 \n\n{status} \n\n\n{footer}"
            status = "".join(map(lambda letter: CUBES[letter.state], letters))
            status = "\n".join(
                [status[index : index + 5] for index in range(0, len(status), 5)]
            )
            footer = "This tweet was generated by #deepwordle: A wordle clone game "
            footer += "powered by #deepgram, #textual, #tweepy, and friends."
            tweet = result.format(
                index=self.index, numerator=numerator, status=status, footer=footer
            )
            # self.message.content = tweet
            self.message.content = "Tweeting your result...\n"
            self.twitter.text = tweet
            self.twitter.post_tweet()
            # self.message.content = self.twitter.text

    async def on_mount(self) -> None:
        view = await self.push_view(DockView())
        header = Header(tall=False)
        footer = Footer()
        # initialize twitter api
        self.twitter = Twitter()
        # initialize deepgram api
        self.recognizer = Recognizer()
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        # initialize
        self.audio_recorder = AudioRecorder()
        # day index
        self.index = get_day_index()
        # self.result = True
        # read files
        self.guesses_list = read_from_file("wordle-guesses.txt")
        self.answers_list = read_from_file("wordle-answers.txt")
        # secret word to guess
        self.secret = random.choice(self.answers_list)
        self.message = MessagePanel("Press `r` to start recording audio...")
        self.stats = MessagePanel("Stats: Coming Soon...")
        letters_grid = DockView()
        self.letters_grid = LettersGrid()
        await view.dock(header, edge="top")
        await letters_grid.dock(self.letters_grid, size=36, z=0, edge="top")
        await view.dock(footer, edge="bottom")
        await view.dock(self.stats, edge="left", size=40)
        await view.dock(self.message, edge="right", size=40)
        await view.dock(letters_grid, edge="left", z=-10)


def main(argv=None) -> int:
    try:
        MainApp.run(title="DeepWordle", log="textual.log", log_verbosity=2)
    except KeyboardInterrupt:
        return -1
    return 0


if __name__ == "__main__":
    main()
