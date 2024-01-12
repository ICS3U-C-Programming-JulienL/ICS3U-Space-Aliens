#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: January 9, 2024
# This is the code for the pybadge game "Space Aliens"

import constants
import stage
import ugame
import time
import random


def splash_scene():
    # this function is the splash game scene

    # get sound ready
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # declare image_bank_background variable
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # declare background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # used this program to split the image into tile:
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # declare game and set FPS
    game = stage.Stage(ugame.display, constants.FPS)

    # set the game layers
    game.layers = [background]

    # render background and sprite list location
    game.render_block()

    # use a whileTrue loop to keep the game running
    while True:
        # wait for 2 seconds then call menu_scene()
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    # this function is the menu game scene

    # declare image_bank_background variable
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PAlETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("JulLam Studios")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PAlETTE, buffer=None
    )
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # declare background
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # declare game and set FPS
    game = stage.Stage(ugame.display, constants.FPS)

    # set the game layers
    game.layers = text + [background]

    # render background and sprite list location
    game.render_block()

    # use a whileTrue loop to keep the game running
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # if Start is pressed, then pass
        if keys & ugame.K_START != 0:
            game_scene()

        # redraw Sprites
        game.tick()


def game_scene():
    # this function is the main game scene

    # declare image_bank_background variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # declare image_bank_sprites
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that need state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # prepare sound
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # declare ship
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # declare alien
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # declare background
    background = stage.Grid(
        image_bank_background, constants.SCREEN_X, constants.SCREEN_Y
    )

    # use a nested for loop to randomize the background
    for x_location in range(constants.SCREEN_X):
        for y_location in range(constants.SCREEN_Y):
            tile_picked = random.randint(1, 3)
            background.tile(x_location, y_location, tile_picked)

    # declare game and set FPS
    game = stage.Stage(ugame.display, constants.FPS)

    # set the game layers
    game.layers = [ship] + [alien] + [background]

    # render background and sprite list location
    game.render_block()

    # use a whileTrue loop to keep the game running
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button status check
        if keys & ugame.K_O != 0:
            # if the a button is up, make it so it was just pressed
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                # otherwise, if the a button was just pressed, make it so it is still pressed
                a_button = constants.button_state["button_still_pressed"]
        else:
            # otherwise, if the a button is still pressed, make it so it was just released
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                # otherwise, make it so the a button is up
                a_button = constants.button_state["button_up"]

        # if B is pressed, then pass
        if keys & ugame.K_X != 0:
            pass

        # if Start is pressed, then pass
        if keys & ugame.K_START != 0:
            pass

        # if Select is pressed, then pass
        if keys & ugame.K_SELECT != 0:
            pass

        # if right on the d-pad is pressed, move the ship right
        if keys & ugame.K_RIGHT != 0:
            # if the ship's x position <= constants.SCREEN_X, move the ship 1 unit right
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                # otherwise set the ship's x-position to 0
                ship.move(0, ship.y)

        # if left on the d-pad is pressed
        if keys & ugame.K_LEFT != 0:
            # if the ship's x position >= 0, move the ship 1 unit left
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                # otherwise set the ship's x-position to constants.SCREEN_X-constants.SPRITE_SIZE
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)

        # if up on the d-pad is pressed,then pass
        if keys & ugame.K_UP != 0:
            pass

        # if down on the d-pad is pressed, then pass
        if keys & ugame.K_DOWN != 0:
            pass
        # update game logic
        # if the A button was just pressed . play pew sound effect
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()


if __name__ == "__main__":
    splash_scene()
