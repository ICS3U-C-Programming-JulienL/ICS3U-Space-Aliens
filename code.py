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
        keys = ugame.buttons.get_pressed()

        # if B is pressed, display B
        if keys & ugame.K_X:
            print("B")

        # if A is pressed, display A
        if keys & ugame.K_O:
            print("A")
        
        # if Start is pressed, display Start
        if keys & ugame.K_START:
            print("Start")

        # if Select is pressed, display Select
        if keys & ugame.K_SELECT:
            print("Select")
        
        # if right on the d-pad is pressed, move the ship right
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)

        # if left on the d-pad is pressed, move the ship left
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)

        # if up on the d-pad is pressed, move the ship up
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        
        # if down on the d-pad is pressed, move the ship down
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()
