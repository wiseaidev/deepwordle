"""
| The following script contains all constants required for our application.

| This program and the accompanying materials are made available under the
| terms of the `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""

WORD_LENGTH = 5
MAX_ATTEMPTS = 6
LETTERS = "abcdefghijklmnopqrstuvwxyz"

DARK = "bold white on rgb(50,57,50)"
ORANGE = "bold white on rgb(208,178,60)"
GREEN = "bold white on rgb(66,164,55)"

NOT_IN_WORD = 0
IS_IN_WORD = 1
IS_IN_POSITION = 2

LETTER_COLORS = {
    NOT_IN_WORD: DARK,
    IS_IN_WORD: ORANGE,
    IS_IN_POSITION: GREEN,
}

CUBES = {NOT_IN_WORD: "⬛", IS_IN_WORD: "🟨", IS_IN_POSITION: "🟩"}
