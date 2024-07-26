#!/bin/env python
import cProfile

import pygame
import sys
from pygame.locals import *
import subprocess


def main() -> None:
    """pygame.init()

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    DISPLAY.fill("#1e1e2e")

    pygame.draw.rect(DISPLAY, "#313244", (200, 150, 100, 50))"""

    nmcli = subprocess.run(("nmcli", "dev", "wifi"), capture_output = True)
    lines = nmcli.stdout.decode().split("\n")
    if len(lines) < 2:
        return None

    networks = tuple(
        net for net in tuple(
            network[27:network.index("Infra")]
            .strip() for network in lines[1:] if len(network) >= 28
        ) if net != "--"
    )

    print(networks)
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()"""


if __name__ == '__main__':
    # main()
    cProfile.run("main()")
