"""
| The following script contains all the utility functions required for running our app.

| This program and the accompanying materials are made available under the terms of the `MIT License`_.
| SPDX short identifier: MIT
| Contributors:
    Mahmoud Harmouch, mail_.
.. _MIT License: https://opensource.org/licenses/MIT
.. _mail: eng.mahmoudharmouch@gmail.com

"""
from collections import (
    Counter,
)
import datetime
import os
from typing import (
    List,
    TypeVar,
)

from deepwordle.components.constants import (
    IS_IN_POSITION,
    IS_IN_WORD,
    NOT_IN_WORD,
    WORD_LENGTH,
)
from deepwordle.components.letter import (
    Letter,
)

L = TypeVar("L", bound=Letter)
INIT_DATE = datetime.date(2021, 6, 19)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)


def update_letters_state(current_guess_letters: List[L], answer: str) -> List[L]:
    """
    A helper function that update the state for each letter.
    """
    # if the current guess is correct, then mark all letters as in position
    current_guess = "".join(map(lambda letter: letter.character, current_guess_letters))
    if current_guess == answer:
        for i, letter in enumerate(current_guess_letters):
            # set all correct
            letter.state = IS_IN_POSITION
            # update the letter in the list
            current_guess_letters[i] = letter
    else:
        # counting letters frequency and making a dictionary from it
        counter_dict = Counter(answer)
        for i, letter in enumerate(current_guess_letters):
            # check if the letter is at correct position
            if answer[i] == letter.character:
                # decrease counter
                counter_dict[letter.character] -= 1
                # set state to IS_IN_POSITION
                letter.state = IS_IN_POSITION
            else:
                # if the counter is 0, mark the letter as NOT_IN_WORD
                if counter_dict.get(letter.character, 0) == 0:
                    letter.state = NOT_IN_WORD
                # else, the letter is in the word
                else:
                    counter_dict[letter.character] -= 1
                    letter.state = IS_IN_WORD
            # update the letter in the list
            current_guess_letters[i] = letter
    return current_guess_letters


def add_new_letter(letters: List[L], letters_count: int, character: str) -> int:
    """
    A helper method to check if the user has entered a 5 letter long word.
    If so, return. the current keep track of all letters.
    if it is divisable by 5 then return.
    else increase the current count of letters being entered.
    """
    for i, letter in enumerate(letters):
        if letter.character and i == letters_count:
            _, remainder = divmod(letters_count, WORD_LENGTH)
            if remainder == WORD_LENGTH - 1:
                # the user didn't enter a 5 letter long word
                return
            letters_count += 1
    # add the new character to grid
    if letters_count is not None:
        letters[letters_count].character = character.upper()
    return letters_count


def remove_letter(letters: List[L], letters_count: int) -> int:
    """
    A helper method to check if the user has entered a backspace letter.
    the letters_count keep track of all letters.
    if the letters_count is divisable by 5 then return.
    """
    for i, letter in enumerate(letters):
        if not letter.character and i == letters_count:
            _, remainder = divmod(letters_count, WORD_LENGTH)
            if remainder == 0:
                # the user can't remove if no letter entered, return.
                return
            letters_count -= 1
    # remove the letter by changing its character
    if letters_count is not None and letters[letters_count].character != "":
        letters[letters_count].character = ""
    return letters_count


def get_day_index() -> int:
    today = datetime.date.today()
    return abs((today - INIT_DATE).days)


def read_from_file(filename):
    with open(os.path.join(BASE_DIR, "data", filename), "r") as file:
        words_list = [
            line[:-1] for line in file if line != "\n"
        ]  # each line contains a newline character.
    return words_list


def append_to_file(filename, word):
    with open(os.path.join(BASE_DIR, "data", filename), "a+") as file:
        file.write(f"{word}\n")


if __name__ == "__main__":
    letters = []
    for letter in "there":
        letters.append(Letter(letter))
    new_letters = update_letters_state(letters, "react")
    list(map(print, new_letters))
    add_new_letter
