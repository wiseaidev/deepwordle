"""
| The following script implements all the necessary logic required for recording audio data in
| our application.

| This program and the accompanying materials are made available under the terms of the
| `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""

from attrs import (
    define,
    field,
)
import os
import pyaudio  # type: ignore

# import numpy as np
# from uniplot import (
#     plot_to_string
# )
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
from rich.panel import (
    Panel,
)
from rich.style import (
    Style,
)
from rich.text import (
    Text,
)
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
from textual.widget import (
    Widget,
)
from textual.widgets import (
    Footer,
    Header,
)
import time
from typing import (
    IO,
    List,
    Literal,
    Optional,
    Union,
)
import wave

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@define
class AudioRecorder:
    """
    A brief encapsulation of an audio recorder object attributes and methods.
    All fields are private by default, and only accessible through
    getters/setters, but someone still could hack his/her way around it!

    Attrs:
        frames_per_buffer: An integer indicating the number of frames per buffer;
            1024 frames/buffer by default.
        audio_format: An integer that represents the number of bits per sample
            stored as 16-bit signed int.
        channels: An integer indicating how many channels a microphone has.
        rate: An integer indicating how many samples per second: frequency.
        py_audio: pyaudio instance.
        data_stream: stream object to get data from microphone.
        wave_file: wave class instance.
        mode: file object mode.
        file_name: file name to store audio data in it.
    """

    _frames_per_buffer: int = field(init=True, default=1024)
    _audio_format: int = field(init=True, default=pyaudio.paInt16)
    _channels: int = field(init=True, default=1)
    _rate: int = field(init=True, default=44100)
    _py_audio: pyaudio.PyAudio = field(init=False, default=pyaudio.PyAudio())
    _data_stream: IO[bytes] = field(init=False, default=None)
    _wave_file: wave.Wave_write = field(init=False, default=None)
    _mode: str = field(init=True, default="wb")
    _file_name: Union[str, IO[bytes]] = field(init=True, default="word.wav")

    @property
    def frames_per_buffer(self) -> int:
        """
        A getter method that returns the value of the `frames_per_buffer` attribute.
        :param self: Instance of the class.
        :return: An integer that represents the value of the `frames_per_buffer` attribute.
        """
        if not hasattr(self, "_frames_per_buffer"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named frames_per_buffer."
            )
        return self._frames_per_buffer

    @frames_per_buffer.setter
    def frames_per_buffer(self, value: int) -> None:
        """
        A setter method that changes the value of the `frames_per_buffer` attribute.
        :param value: An integer that represents the value of the `frames_per_buffer` attribute.
        :return: NoReturn.
        """
        setattr(self, "_frames_per_buffer", value)

    @property
    def audio_format(self) -> int:
        """
        A getter method that returns the value of the `audio_format` attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `audio_format` attribute.
        """
        if not hasattr(self, "_audio_format"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named audio_format."
            )
        return self._audio_format

    @audio_format.setter
    def audio_format(self, value: int) -> None:
        """
        A setter method that changes the value of the `audio_format` attribute.
        :param value: An integer that represents the value of the `audio_format` attribute.
        :return: NoReturn.
        """
        setattr(self, "_frames_per_buffer", value)

    @property
    def channels(self) -> int:
        """
        A getter method that returns the value of the `channels` attribute.
        :param self: Instance of the class.
        :return: An integer that represents the value of the `channels` attribute.
        """
        if not hasattr(self, "_channels"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named channels."
            )
        return self._channels

    @channels.setter
    def channels(self, value: int) -> None:
        """
        A setter method that changes the value of the `channels` attribute.
        :param value: An integer that represents the value of the `channels` attribute.
        :return: NoReturn.
        """
        setattr(self, "_channels", value)

    @property
    def rate(self) -> int:
        """
        A getter method that returns the value of the `rate`attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `rate` attribute.
        """
        if not hasattr(self, "_rate"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named rate."
            )
        return self._rate

    @rate.setter
    def rate(self, value: int) -> None:
        """
        A setter method that changes the value of the `rate` attribute.
        :param value: An integer that represents the value of the `rate` attribute.
        :return: NoReturn.
        """
        setattr(self, "_rate", value)

    @property
    def py_audio(self) -> pyaudio.PyAudio:
        """
        A getter method that returns the value of the `py_audio`attribute.
        :param self: Instance of the class.
        :return: A PyAudio object that represents the value of the `py_audio` attribute.
        """
        if not hasattr(self, "_py_audio"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named py_audio."
            )
        return self._py_audio

    @py_audio.setter
    def py_audio(self, value: int) -> None:
        """
        A setter method that changes the value of the `py_audio` attribute.
        :param value: A PyAudio object that represents the value of the `py_audio` attribute.
        :return: NoReturn.
        """
        setattr(self, "_py_audio", value)

    @property
    def data_stream(self) -> IO[bytes]:
        """
        A getter method that returns the value of the `data_stream`attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `data_stream` attribute.
        """
        if not hasattr(self, "_data_stream"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named data_stream."
            )
        return self._data_stream

    @data_stream.setter
    def data_stream(self, value: IO[bytes]) -> None:
        """
        A setter method that changes the value of the `data_stream` attribute.
        :param value: A string that represents the value of the `data_stream` attribute.
        :return: NoReturn.
        """
        setattr(self, "_data_stream", value)

    @property
    def wave_file(self) -> wave.Wave_write:
        """
        A getter method that returns the value of the `wave_file`attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `wave_file` attribute.
        """
        if not hasattr(self, "_wave_file"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named wave_file."
            )
        return self._wave_file

    @wave_file.setter
    def wave_file(self, value: wave.Wave_write) -> None:
        """
        A setter method that changes the value of the `wave_file` attribute.
        :param value: A string that represents the value of the `wave_file` attribute.
        :return: NoReturn.
        """
        setattr(self, "_wave_file", value)

    @property
    def file_name(self) -> Union[str, IO[bytes]]:
        """
        A getter method that returns the value of the `file_name`attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `file_name` attribute.
        """
        if not hasattr(self, "_mode"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named file_name."
            )
        return self._file_name

    @file_name.setter
    def file_name(self, value: Union[str, IO[bytes]]) -> None:
        """
        A setter method that changes the value of the `file_name` attribute.
        :param value: A string that represents the value of the `file_name` attribute.
        :return: NoReturn.
        """
        setattr(self, "_file_name", value)

    @property
    def mode(self) -> str:
        """
        A getter method that returns the value of the `mode`attribute.
        :param self: Instance of the class.
        :return: A string that represents the value of the `mode` attribute.
        """
        if not hasattr(self, "_mode"):
            raise AttributeError(
                f"Your {self.__class__.__name__!r} instance has no attribute named mode."
            )
        return self._mode

    @mode.setter
    def mode(self, value: str) -> None:
        """
        A setter method that changes the value of the `mode` attribute.
        :param value: A string that represents the value of the `mode` attribute.
        :return: NoReturn.
        """
        setattr(self, "_mode", value)

    def __repr__(self) -> str:
        attrs: dict = {
            "frames_per_buffer": self.frames_per_buffer,
            "audio_format": self.audio_format,
            "channels": self.channels,
            "rate": self.rate,
            "py_audio": repr(self.py_audio),
            "data_stream": self.data_stream,
            "wave_file": repr(self.wave_file),
            "mode": self.mode,
            "file_name": self.file_name,
        }
        return f"{self.__class__.__name__}({attrs})"

    # def __attrs_post_init__(self) -> None:
    #     wave_file = wave.open(os.path.join(BASE_DIR, self.file_name), self.mode)
    #     wave_file.setnchannels(self.channels)
    #     wave_file.setsampwidth(self.py_audio.get_sample_size(self.audio_format))
    #     wave_file.setframerate(self.rate)
    #     self.wave_file = wave_file
    #     del wave_file
    #     return

    def record(self, duration: int = 3) -> Optional[List[List[str]]]:
        self.wave_file = wave.open(os.path.join(BASE_DIR, self.file_name), self.mode)
        self.wave_file.setnchannels(self.channels)
        self.wave_file.setsampwidth(self.py_audio.get_sample_size(self.audio_format))
        self.wave_file.setframerate(self.rate)
        # if not self.wave_file:
        #     return [[''], ]
        # stream object to get data from microphone
        self.data_stream = self.py_audio.open(
            format=self.audio_format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            output=True,
            frames_per_buffer=self.frames_per_buffer,
        )
        frame_count = 0
        # frames: List[List[str]] = []
        max_frames: int = int(self.rate / self.frames_per_buffer * duration) - 1
        # start_time = time.time()
        while True:
            frame_count += 1
            # read audio data
            string_audio_data = self.data_stream.read(self.frames_per_buffer)
            # write to file
            self.wave_file.writeframes(string_audio_data)
            # if frame_count % 5 == 0:
            #     # convert data to integers
            #     audio_data = np.frombuffer(string_audio_data, dtype=np.int16)
            #     # make np array\
            #     # convert plot to list of strings
            #     #yield plot_to_string(audio_data)
            #     frames.append(plot_to_string(audio_data))
            #     #print("\n".join(plot))
            if frame_count == max_frames:
                break
        # calculate average frame rate
        # stop_time = time.time()
        # frame_rate = frame_count / (stop_time - start_time)
        # print(f'Average frame rate = {frame_rate:.2f} FPS')
        # return frames

    def stop_recording(self) -> None:
        if self.data_stream:
            self.data_stream.close()
            self.py_audio.terminate()
            self.wave_file.close()


class Figure(Widget):

    plot: str = Reactive("")
    vertical: Optional[Literal["top", "middle", "bottom"]]
    title: Optional[str] = "plot"
    _style: str

    def __init__(
        self,
        name: str,
        plot: str,
        style: str,
        vertical: Optional[Literal["top", "middle", "bottom"]] = "middle",
    ) -> None:
        super().__init__(name)
        self.plot: str = plot
        self.vertical: str = vertical
        self._style: str = style
        self.title = name

    def render(self) -> RenderableType:
        """Build a Rich renderable to render the plot."""
        return Panel(
            renderable=Align.center(Text(self.plot), vertical=self.vertical),
            style=self._style,
            expand=False,
            title=self.title,
        )


if __name__ == "__main__":
    rec = AudioRecorder()
    # rec.init_recording()
    print(rec)
    rec.record()
    # for frame in frames:
    #     print('\n'.join(frame))
    # rec.stop_recording()
    # class MyApp(App):
    #     async def on_load(self) -> None:
    #         """Bind keys here."""
    #         await self.bind("q", "quit", "Quit")

    #     def on_key(self, event: events.Key) -> None:
    #         if event.key == "r":
    #             for frame in self.rec.record():
    #             #print('\n'.join(frame))
    #                 self.figure.plot = "\n".join(frame)
    #             self.rec.stop_recording()

    #     async def on_mount(self) -> None:
    #         view: DockView = await self.push_view(DockView())
    #         self.rec = AudioRecorder()
    #         #self.rec.init_recording()
    #         await view.dock(Header(), edge="top")
    #         await view.dock(Footer(), edge="bottom")
    #         #self.rec = AudioRecorder()
    #         #self.rec.init_recording()
    #         #print(self.rec)
    #         style: str = "bold white on rgb(58,58,58)"
    #         self.figure = Figure(name="Sine Wave Plot", plot="a", style=style)
    #         await view.dock(self.figure, edge="bottom", size=60)  # type: ignore
    #         #rec.stop_recording()
    # MyApp.run(title="Plot", log="textual.log", log_verbosity=2)
