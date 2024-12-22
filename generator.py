"""Tools for generating the password"""

import secrets
from typing import List, Literal
import enum


class Numbered(enum.Enum):
    """Settings for password numbering mapped for config."""

    NONE = 0
    END = 1
    ALL = 2


def select_word(dictionary: List[str]) -> str:
    """Secretly select a word from the dictionary and remove it from the dictionary

    Arguments:
        dictionary -- List of words to select from

    Raises:
        ValueError: Dictionary has no words and cannot be used
        ValueError: Dictionary has duplicate words and can affect the selection process negatively

    Returns:
        The selected word to be used in the password
    """
    if len(dictionary) == 0:
        raise ValueError("No words in dictionary")
    if len(dictionary) != len(set(dictionary)):
        raise ValueError("Dictionary has duplicate words")

    word = secrets.choice(dictionary)
    dictionary.remove(word)
    return word


def random_int(minimum: int, maximum: int) -> int:
    """Generate a random number between min and max+1 using secrets module

    Arguments:
        minimum -- Lowest number allowed
        maximum -- Highest number allowed

    Raises:
        ValueError: Maximum is lower than minimum

    Returns:
        The number that was generated
    """
    if maximum <= minimum:
        raise ValueError("Max is smaller than min")
    maximum += 1
    difference = abs(maximum - minimum)

    random = secrets.randbelow(difference)

    return minimum + random


def overall_length(words: List[str], separators: str) -> int:
    """Return the total length of the password including separators

    Arguments:
        words -- Words that are in the password
        separators -- The list of separators to count

    Returns:
        Total length of the password
    """
    length = len(words) - 1 if len(separators) > 0 else 0
    for word in words:
        length += len(word)

    return length


def generate_password(
    dictionary: List[str],
    *,
    separators: str = "-",
    minimum_words: int = 4,
    minimum_length: int = 20,
    capitalize: bool = True,
    numbered: Literal[Numbered.NONE, Numbered.END, Numbered.ALL] = Numbered.ALL,
) -> str:
    """Return a randomly generated password using secrets

    Arguments:
        dictionary -- What words to use in the password
        separators -- Characters to put between words, selected at random
        minimum_words -- How many words are needed in the password
        minimum_length -- Smallest amount of characters in the password
        capitalize -- Capitalize the first character or have the entire word lowercase
        numbered -- How to and if the password should be numbered

    Returns:
        Generated password using the arguments given
    """
    words = []
    while (
        overall_length(words, separators) < minimum_length or len(words) < minimum_words
    ):
        new_word = select_word(dictionary)
        if capitalize:
            new_word = new_word[0].upper() + new_word[1:]
        else:
            new_word = new_word.lower()

        if numbered == Numbered.ALL:
            new_word += str(random_int(0, 9))

        words.append(new_word)

    if numbered == Numbered.END:
        words.append(str(random_int(0, 9)))

    password = ""
    for word in words[:-1]:
        password += word
        if separators:
            password += secrets.choice(separators)
    password += words[-1]

    return password
