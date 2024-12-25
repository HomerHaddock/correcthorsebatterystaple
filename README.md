# correcthorsebatterystaple

Customizable password generator using Python and the built-in `secrets` module.

- [correcthorsebatterystaple](#correcthorsebatterystaple)
  - [Requirements](#requirements)
  - [Setup](#setup)
  - [Configuration](#configuration)
    - [General Settings](#general-settings)
      - [dictionary:](#dictionary)
      - [ignore:](#ignore)
    - [Password Specific (password:)](#password-specific-password)
      - [separators:](#separators)
      - [min\_words:](#min_words)
      - [min\_length:](#min_length)
      - [numbered:](#numbered)
      - [amount:](#amount)
    - [Word Specific Settings (password: words:)](#word-specific-settings-password-words)
      - [capitalize:](#capitalize)
  - [Dictionaries](#dictionaries)
  - [Usage](#usage)
  - [Credits](#credits)
    - [Dictionary Sources](#dictionary-sources)

## Requirements

To run the script you will need `python>=3.10`, for better YAML support it is recommended you have `PyYAML>=6.0.2` installed.

## Setup

To download and setup `correcthorsebatterystaple` on Debian 12 or similar operating systems run the following.

```bash
git clone https://github.com/HomerHaddock/correcthorsebatterystaple.git
cd correcthorsebatterystaple
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

(If you are using Windows or operating systems that don't work with all of these commands, set this up how you setup everything else how you would normally.)

## Configuration

While the `config.yaml` provided works for what most people need, if you want to change any settings you can either read the comments in the file or read this section.

### General Settings

#### dictionary:

Path(s) to dictionary file or folder. Paths may be relative to `config.yaml` or absolute. You can have `"one/path/to/dictionary"` or `["a", "list", "of/paths"]` as the value. `Default: "dictionary"`

#### ignore:

Name(s) of dictionary files to ignore. Names are case-sensitive and needs to be the name in full.

If a dictionary file is found with a name that is in the list all words in the dictionary will not be added.

This is useful if you have dictionaries that should be enabled sometimes but not all the time. `Default: ["jargon.txt", "science_terms.txt"]`

### Password Specific (password:)

#### separators:

String of characters to place between entries. If there is more than one character then what is placed is randomly selected. `Default: "-"`

#### min_words:

Minimum amount of words to have in the password. There may be more words that what was given to the setting. `Default: 4`

#### min_length:

The smallest the password can be. More words will be added until it's at least as long as the value given. `Default: 20`

#### numbered:

If and how to place numbers in the password, numbers are `0-9` and only single digit. Allowed values are `"none"`, `"end"`, and `"all"`. `Default: "none"`

| Value    | Behaviour                                                                                   |
| -------- | ------------------------------------------------------------------------------------------- |
| `"none"` | Numbers are not to be used                                                                  |
| `"end"`  | Add a number at the end of the password as it's own word                                    |
| `"all"`  | Add a number to the end of every word, does not add an extra one at the end of the password |

#### amount:

How many passwords to generate before exiting. This allows for there to be more than one password to select without needing to restart the script. `Default: 4`

### Word Specific Settings (password: words:)

#### capitalize:

Makes the first character in a word uppercase, makes entire word lowercase otherwise. `Default: True`

## Dictionaries

Dictionaries in a nutshell are just `.txt` files that are read by the script to be added to the dictionary of words to use in the password.
All dictionaries must be encoded with `UTF-8` and end with `.txt` to be properly read by the script (Most editors will use `UTF-8` by default).

Inside the file every word is separated by a newline character (`\n`) or a space character (`" "`).

Comments can be added in a way similar to Python. When there is a `#` in a line the script will ignore the character and all following characters until a newline.

```
# This is an example dictionary.
# Anything past a '#' is being ignored, this allows comments to exist.
but
these
words
are
being
added
and
is
separated
by
newline
characters
others can work fine with spaces # And will be fully parsed by the script!
# But being separated by spaces isn't the best for people with narrow screens,
# and code editing tools that parse lines up to a certain number of characters.
```

## Usage

While this script is fully functional out-of-the box, it is recommended you edit [config.yaml](#configuration)
and add entries to your [dictionary](#dictionaries) to make your passwords that extra bit secure.

To generate passwords is just starting `main.py`.

```bash
python3 main.py
```

When generating passwords the script will use `print()` to output the passwords to the terminal.
You can run the script as many times you want without worry about anything breaking,
unless a setting was changed to something the script cannot hadle.

## Credits

Written and maintained by [HomerHaddock](https://github.com/HomerHaddock)

Inspired by [xkcd.com](https://www.xkcd.com/936/) and [correcthorsebatterystaple.net](https://www.correcthorsebatterystaple.net/index.html)

### Dictionary Sources

Adjectives: https://github.com/aaronbassett/Pass-phrase/blob/master/adjectives.txt

Nouns: https://www.desiquintans.com/nounlist

Verbs: https://github.com/aaronbassett/Pass-phrase/blob/master/verbs.txt

Extras: https://bitbucket.org/jvdl/correcthorsebatterystaple/src/master/data/wordlist.txt

Jargon: https://bitbucket.org/jvdl/correcthorsebatterystaple/src/master/data/jargon.txt

Science Terms: https://bitbucket.org/jvdl/correcthorsebatterystaple/src/master/data/science-terms.txt
