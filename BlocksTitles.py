#!/bin/env python3
"""
@author: Aeldit <https://github.com/Aeldit/>
@summary: Prints in the console (Windows) or adds to the clipboard the given text but as a 'blocks' title
"""
import sys

import pyperclip

LETTERS = {
    'A': [
        " █████╗ ",
        "██╔══██╗",
        "███████║",
        "██╔══██║",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ],
    'B': [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔══██╗",
        "██████╔╝",
        "╚═════╝ "
    ],
    'C': [
        " ██████╗",
        "██╔════╝",
        "██║     ",
        "██║     ",
        "╚██████╗",
        " ╚═════╝"
    ],
    'D': [
        "██████╗ ",
        "██╔══██╗",
        "██║  ██║",
        "██║  ██║",
        "██████╔╝",
        "╚═════╝"
    ],
    'E': [
        "███████╗",
        "██╔════╝",
        "███████╗",
        "██╔════╝",
        "███████╗",
        "╚══════╝"
    ],
    'F': [
        "███████╗",
        "██╔════╝",
        "███████╗",
        "██╔════╝",
        "██║     ",
        "╚═╝     "
    ],
    'G': [
        " ████████╗",
        "██╔══════╝",
        "██║ ████╗ ",
        "██║ ╚══██╗",
        "╚███████╔╝",
        " ╚══════╝ "
    ],
    'H': [
        "██╗  ██╗",
        "██║  ██║",
        "███████║",
        "██╔══██║",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ],
    'I': [
        "██╗ ",
        "╚═╝ ",
        "██╗ ",
        "██║ ",
        "██║ ",
        "╚═╝ "
    ],
    'J': [
        "   ██╗",
        "   ██║",
        "   ██║",
        "   ██║",
        "████╔╝",
        "╚═══╝"
    ],
    'K': [
        "██╗  ██╗",
        "██║ ██╔╝",
        "█████╔╝ ",
        "██╔═██╗ ",
        "██║ ╚██╗",
        "╚═╝  ╚═╝"
    ],
    'L': [
        "██╗     ",
        "██║     ",
        "██║     ",
        "██║     ",
        "███████╗",
        "╚══════╝"
    ],
    'M': [
        "██╗   ██╗",
        "████████║",
        "██╔██═██║",
        "██║   ██║",
        "██║   ██║",
        "╚═╝   ╚═╝"
    ],
    'N': [
        "██╗   ██╗",
        "████╗ ██║",
        "██╔██╗██║",
        "██║╚████║",
        "██║  ╚██║",
        "╚═╝   ╚═╝"
    ],
    'O': [
        " ██████╗ ",
        "██╔═══██╗",
        "██║   ██║",
        "██║   ██║",
        "╚██████╔╝",
        " ╚═════╝ "
    ],
    'P': [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔═══╝ ",
        "██║     ",
        "╚═╝     "
    ],
    'Q': [
        " ██████╗  ",
        "██╔═══██╗ ",
        "██║   ██║ ",
        "██║  ███║ ",
        "╚████████╗",
        " ╚═══════╝"
    ],
    'R': [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔══██╗",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ],
    'S': [
        " ██████╗",
        "██╔════╝",
        "╚█████╗ ",
        " ╚═══██╗",
        "██████╔╝",
        "╚═════╝ "
    ],
    'T': [
        "████████╗",
        "╚══██╔══╝",
        "   ██║   ",
        "   ██║   ",
        "   ██║   ",
        "   ╚═╝   "
    ],
    'U': [
        "██╗   ██╗",
        "██║   ██║",
        "██║   ██║",
        "██║   ██║",
        "╚██████╔╝",
        " ╚═════╝ "
    ],
    'V': [
        "██╗     ██╗",
        "╚██╗   ██╔╝",
        " ╚██╗ ██╔╝ ",
        "  ╚████╔╝  ",
        "   ╚██╔╝   ",
        "    ╚═╝    "
    ],
    'W': [
        "██╗         ██╗",
        "╚██╗       ██╔╝",
        " ╚██╗ ██╗ ██╔╝ ",
        "  ╚████████╔╝  ",
        "   ╚██╔═██╔╝   ",
        "    ╚═╝ ╚═╝    "
    ],
    'X': [
        "██╗   ██╗",
        "╚██╗ ██╔╝",
        " ╚████╔╝ ",
        " ██╔═██╗ ",
        "██╔╝ ╚██╗",
        "╚═╝   ╚═╝"
    ],
    'Y': [
        "██╗   ██╗",
        "╚██╗ ██╔╝",
        " ╚████╔╝ ",
        "   ██╔╝  ",
        "   ██║   ",
        "   ╚═╝   "
    ],
    'Z': [
        "████████╗",
        "     ██╔╝",
        "   ██╔═╝ ",
        " ██╔═╝   ",
        "████████╗",
        "╚═══════╝"
    ],
    ' ': [
        "      ",
        "      ",
        "      ",
        "      ",
        "      ",
        "      "
    ]
}


def main(text: str) -> None:
    """
    Takes the given string and puts it in the user clipboard
    @param text: The text to transform into a blocks title
    @return: None
    """
    # Appends all the letters found in the given string
    # (if the given letters are defined in the LETTERS array)
    letters: list[list] = [LETTERS[s] for s in text.upper() if s in LETTERS.keys()]

    lines: list[str] = []
    text_len = len(text)
    for line_nb in range(6):
        # Makes all the values in the current list a single string
        lines.append("".join(
            # For each letter, add its part of index 'line_nb' to the list
            [letters[s][line_nb] for s in range(text_len)]
        ))

    final_str = "%s\n%s\n%s\n%s\n%s\n%s" % (lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])
    pyperclip.copy(final_str)
    print("The title has been successfully added to your clipboard, you can now copy it where you want")
    return None


if __name__ == '__main__':
    if "linux" in sys.platform:
        if len(sys.argv) == 2:
            if sys.argv[1] == "-h":
                print(
                    "Usage: %s [TEXT] ...\n\n"
                    "Adds to your clipboard the given text under the form of a block title\n\n"
                    "Example:\n%s \"My title\"" % (sys.argv[0], sys.argv[0])
                )
            else:
                main(sys.argv[1])
        else:
            print("Wrong number of arguments.\nTry '%s -h' for more information." % sys.argv[0])
            exit(1)
    else:
        # Replace the text here manually if you are on any other system than Linux
        main("Your text")
