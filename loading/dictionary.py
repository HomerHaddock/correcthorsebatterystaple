"""Load and parse all files found in dictionary folder(s)"""

from typing import List, Set
from pathlib import Path
import os


def read_file(path: str) -> List[str]:
    """Read text from file and create parsed list of words,
    ignore everything at "#" and later until newline

    Arguments:
        path -- File to be read and parsed

    Returns:
        List of all words that were found with their original format
    """
    words: List[str] = []
    with open(path, encoding="utf-8") as file:
        for line in file.readlines():
            comment_index = line.find("#")
            if comment_index != -1:
                line = line[:comment_index]
            line.strip()
            if not line:
                continue
            words.extend([word.strip("\n") for word in line.split(" ")])
    return words


def load_files(paths: List[str], ignore: List[str]) -> List[str]:
    """Create dictionary from text files in given paths sorted based on "_TYPE.txt"

    Arguments:
        paths -- List of paths of files or folders to check and parse .txt files
        ignore -- Names of files to skip when reading

    Returns:
        Complete dictionary of adjectives, nouns, and verbs with undefined types put in nouns
        dictionary is sorted with "adjectives", "nouns", "verbs", and "adverbs" as the keys
    """
    files: List[str] = []
    for path in paths:
        path = os.path.realpath(path)
        if os.path.isfile(path):
            files.append(path)
            continue
        files.extend(
            [
                str(file)
                for file in list(Path(path).rglob("*.[tT][xX][tT]"))
                if os.path.isfile(file)
            ]
        )

    dictionary: Set[str] = set()
    for file in files:
        if os.path.basename(file) in ignore:
            continue
        dictionary = dictionary.union(read_file(file))

    return list(dictionary)
