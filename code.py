#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: January 9, 2024
# This is the code for the pybadge game "Space Aliens"

import constants
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
    background = stage.Grid(
        image_bank_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # declare game, game layers, and render_block
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [ship] + [background]
    game.render_block()

    # use a whileTrue loop to keep the game running
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # if B is pressed, then pass
        if keys & ugame.K_X:
            pass

        # if A is pressed, then pass
        if keys & ugame.K_O:
            pass

        # if Start is pressed, then pass
        if keys & ugame.K_START:
            pass

        # if Select is pressed, then pass
        if keys & ugame.K_SELECT:
            pass

        # if right on the d-pad is pressed, move the ship right
        if keys & ugame.K_RIGHT:
            # if the ship's x position <= constants.SCREEN_X, move the ship 1 unit right
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                # otherwise set the ship's x-position to 0
                ship.move(0, ship.y)

        # if left on the d-pad is pressed
        if keys & ugame.K_LEFT:
            # if the ship's x position >= 0, move the ship 1 unit left
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                # otherwise set the ship's x-position to constants.SCREEN_X-constants.SPRITE_SIZE
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        # if up on the d-pad is pressed,then pass
        if keys & ugame.K_UP:
            pass

        # if down on the d-pad is pressed, then pass
        if keys & ugame.K_DOWN:
            pass
        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
