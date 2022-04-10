"""
| The following script implements all the necessary logic required for deepgram.

| This program and the accompanying materials are made available under the terms of the `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""

import asyncio
from attrs import (
    define,
    field,
)
from deepgram import (
    Deepgram,
)
import json
import os
from typing import (
    Optional,
    TypeVar,
)

T = TypeVar("T", bound=Deepgram)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@define
class Recognizer:
    """Class that encapsulates Deepgram's api config."""

    _api_key: Optional[str] = field(default=os.environ.get("DEEPGRAM_API_KEY"))
    _file_name: Optional[str] = field(default="word.wav")
    _deepgram: Optional[T] = field(default=None)

    @property
    def api_key(self) -> str:
        """
        A getter method that returns the value of the `api_key` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `api_key` attribute.
        """
        if not hasattr(self, "_api_key"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named api_key."
            )
        return self._api_key

    @api_key.setter
    def api_key(self, value: str) -> None:
        """
        A setter method that changes the value of the `api_key` attribute.
        :param value: A string that represents the value of the `api_key` attribute.
        :return: NoReturn.
        """
        setattr(self, "_api_key", value)

    @property
    def file_name(self) -> str:
        """
        A getter method that returns the value of the `file_name` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `file_name` attribute.
        """
        if not hasattr(self, "_file_name"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named file_name."
            )
        return self._file_name

    @file_name.setter
    def file_name(self, value: str) -> None:
        """
        A setter method that changes the value of the `file_name` attribute.
        :param value: A string that represents the value of the `file_name` attribute.
        :return: NoReturn.
        """
        setattr(self, "_file_name", value)

    @property
    def deepgram(self) -> T:
        """
        A getter method that returns the value of the `deepgram` attribute.
        :param self: Instance of the class.
        :return: A Deepgram object that represents the value of the `deepgram` attribute.
        """
        if not hasattr(self, "_deepgram"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named deepgram."
            )
        return self._deepgram

    @deepgram.setter
    def deepgram(self, value: T) -> None:
        """
        A setter method that changes the value of the `deepgram` attribute.
        :param value: A Deepgram object that represents the value of the `deepgram` attribute.
        :return: NoReturn.
        """
        setattr(self, "_deepgram", value)

    def __attrs_post_init__(self):
        self.deepgram = Deepgram(self.api_key)

    async def recognize(self):
        # Open the audio file
        with open(os.path.join(BASE_DIR, self.file_name), "rb") as audio:
            # ...or replace mimetype as appropriate
            source = {"buffer": audio, "mimetype": "audio/wav"}
            response = await self.deepgram.transcription.prerecorded(
                source, {"punctuate": False}
            )
            return response


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(Recognizer().recognize())
    words = result["results"]["channels"][0]["alternatives"][0]["words"]
    print(words)


if __name__ == "__main__":
    main()
