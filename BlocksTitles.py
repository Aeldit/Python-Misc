#!/bin/env python3
"""
:author: Aeldit <https://github.com/Aeldit/>
:summary: Prints in the console the given text but as a 'blocks' title
"""

################################################################################
#                                   IMPORTS                                    #
################################################################################
import sys

################################################################################
#                               GLOBAL VARIABLES                               #
################################################################################
# fmt: off
LETTERS = {
    "A": (
        " █████╗ ",
        "██╔══██╗",
        "███████║",
        "██╔══██║",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ),
    "B": (
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔══██╗",
        "██████╔╝",
        "╚═════╝ "
    ),
    "C": (
        " ██████╗",
        "██╔════╝",
        "██║     ",
        "██║     ",
        "╚██████╗",
        " ╚═════╝"
    ),
    "D": (
        "██████╗ ",
        "██╔══██╗",
        "██║  ██║",
        "██║  ██║",
        "██████╔╝",
        "╚═════╝ "
    ),
    "E": (
        "███████╗",
        "██╔════╝",
        "███████╗",
        "██╔════╝",
        "███████╗",
        "╚══════╝"
    ),
    "F": (
        "███████╗",
        "██╔════╝",
        "███████╗",
        "██╔════╝",
        "██║     ",
        "╚═╝     "
    ),
    "G": (
        " ████████╗",
        "██╔══════╝",
        "██║ ████╗ ",
        "██║ ╚══██╗",
        "╚███████╔╝",
        " ╚══════╝ "
    ),
    "H": (
        "██╗  ██╗",
        "██║  ██║",
        "███████║",
        "██╔══██║",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ),
    "I": (
        "██╗ ",
        "╚═╝ ",
        "██╗ ",
        "██║ ",
        "██║ ",
        "╚═╝ "
    ),
    "J": (
        "   ██╗",
        "   ██║",
        "   ██║",
        "   ██║",
        "████╔╝",
        "╚═══╝ "
    ),
    "K": (
        "██╗  ██╗",
        "██║ ██╔╝",
        "█████╔╝ ",
        "██╔═██╗ ",
        "██║ ╚██╗",
        "╚═╝  ╚═╝"
    ),
    "L": (
        "██╗     ",
        "██║     ",
        "██║     ",
        "██║     ",
        "███████╗",
        "╚══════╝"
    ),
    "M": (
        "██╗   ██╗",
        "████████║",
        "██╔██═██║",
        "██║   ██║",
        "██║   ██║",
        "╚═╝   ╚═╝"
    ),
    "N": (
        "██╗   ██╗",
        "████╗ ██║",
        "██╔██╗██║",
        "██║╚████║",
        "██║  ╚██║",
        "╚═╝   ╚═╝"
    ),
    "O": (
        " ██████╗ ",
        "██╔═══██╗",
        "██║   ██║",
        "██║   ██║",
        "╚██████╔╝",
        " ╚═════╝ "
    ),
    "P": (
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔═══╝ ",
        "██║     ",
        "╚═╝     "
    ),
    "Q": (
        " ██████╗  ",
        "██╔═══██╗ ",
        "██║   ██║ ",
        "██║  ███║ ",
        "╚████████╗",
        " ╚═══════╝"
    ),
    "R": (
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔══██╗",
        "██║  ██║",
        "╚═╝  ╚═╝"
    ),
    "S": (
        " ██████╗",
        "██╔════╝",
        "╚█████╗ ",
        " ╚═══██╗",
        "██████╔╝",
        "╚═════╝ "
    ),
    "T": (
        "████████╗",
        "╚══██╔══╝",
        "   ██║   ",
        "   ██║   ",
        "   ██║   ",
        "   ╚═╝   "
    ),
    "U": (
        "██╗   ██╗",
        "██║   ██║",
        "██║   ██║",
        "██║   ██║",
        "╚██████╔╝",
        " ╚═════╝ "
    ),
    "V": (
        "██╗     ██╗",
        "╚██╗   ██╔╝",
        " ╚██╗ ██╔╝ ",
        "  ╚████╔╝  ",
        "   ╚██╔╝   ",
        "    ╚═╝    "
    ),
    "W": (
        "██╗         ██╗",
        "╚██╗       ██╔╝",
        " ╚██╗ ██╗ ██╔╝ ",
        "  ╚████████╔╝  ",
        "   ╚██╔═██╔╝   ",
        "    ╚═╝ ╚═╝    "
    ),
    "X": (
        "██╗   ██╗",
        "╚██╗ ██╔╝",
        " ╚████╔╝ ",
        " ██╔═██╗ ",
        "██╔╝ ╚██╗",
        "╚═╝   ╚═╝"
    ),
    "Y": (
        "██╗   ██╗",
        "╚██╗ ██╔╝",
        " ╚████╔╝ ",
        "   ██╔╝  ",
        "   ██║   ",
        "   ╚═╝   "
    ),
    "Z": (
        "████████╗",
        "     ██╔╝",
        "   ██╔═╝ ",
        " ██╔═╝   ",
        "████████╗",
        "╚═══════╝"
    ),
    " ": (
        "      ",
        "      ",
        "      ",
        "      ",
        "      ",
        "      "
    )
}
# fmt: on


################################################################################
#                                  FUNCTIONS                                   #
################################################################################
def main(text: str) -> str:
    """
    Transforms the given text to a 'blocky' one

    :param text: The text to transform into a blocks title
    :returns: The blocky text
    """
    # Appends all the letters found in the given string
    # (if the given letters are defined in the LETTERS array)
    letters = tuple(LETTERS[s] for s in text.upper() if s in LETTERS.keys())
    text_len = len(text)
    return "\n".join(
        # Makes all the values in the current list a single string
        "".join(
            # For each letter, add its part of index 'line_nb' to the list
            letters[s][line_nb]
            for s in range(text_len)
        )
        for line_nb in range(6)
    )


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            print(
                "Usage: %s [TEXT] ...\n\n"
                "Prints in the console the given text under the form of "
                "a block title\n\n"
                'Example:\n%s "My title"' % (sys.argv[0], sys.argv[0])
            )
        else:
            print(main(sys.argv[1]))
    else:
        print(
            "Wrong number of arguments.\nTry '%s -h' for more "
            "information." % sys.argv[0]
        )
