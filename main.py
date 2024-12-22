"""Main file for organizing other modules and making password generation work"""

import sys

from generator import Numbered, generate_password
from loading.dictionary import load_files
from loading.settings import config


def main():
    """Generate password and print to terminal using 'config.yaml' as settings

    Raises:
        ValueError: Config file setting 'numbered' has a value not supported
    """
    dictionary = load_files(config["dictionary"], config["ignore"])
    password_settings = config["password"]

    numbered_setting: str = password_settings["numbered"].lower()
    match numbered_setting:
        case "none":
            numbering = Numbered.NONE
        case "end":
            numbering = Numbered.END
        case "all":
            numbering = Numbered.ALL
        case _:
            raise ValueError("Setting 'numbered' has a value that is not supported")

    for _ in range(password_settings["amount"]):
        password = generate_password(
            dictionary.copy(),
            separators=password_settings["separators"],
            minimum_words=password_settings["min_words"],
            minimum_length=password_settings["min_length"],
            capitalize=password_settings["words"]["capitalize"],
            numbered=numbering,
        )

        print(password)


if __name__ == "__main__":
    main()
    sys.exit(0)
