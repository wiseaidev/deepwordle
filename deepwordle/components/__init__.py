"""
| Top-level package for components.

| This program and the accompanying materials are made available under the terms of the `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""

from .utils import update_letters_state, add_new_letter, remove_letter, get_day_index, read_from_file
from .message import MessagePanel
from .letters_grid import LettersGrid
from .constants import CUBES, LETTERS