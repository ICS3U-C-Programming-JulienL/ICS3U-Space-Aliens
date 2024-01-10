#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: January 9, 2024
# This is the code for the pybadge game "Space Aliens"

import stage
import ugame


def game_scene():
    # this function is the main game scene

    # declare background variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)

    # declare game
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    # use a whileTrue loop to keep the game running
    while True:
        pass


if __name__ == "__main__":
    game_scene()
