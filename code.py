#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: January 9, 2024
# This is the code for the pybadge game "Space Aliens"

import stage
import ugame


def game_scene():
    # this function is the main game scene

    # declare image_bank_background variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # declare image_bank_sprites
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # declare ship
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # declare background
    background = stage.Grid(image_bank_background, 10, 8)

    # declare game, game layers, and render_block
    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()

    # use a whileTrue loop to keep the game running
    while True:
        # get user input

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
