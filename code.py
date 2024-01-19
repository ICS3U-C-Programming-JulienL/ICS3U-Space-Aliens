#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: January 11, 2024
# This is the code for the pybadge game "Space Aliens"

import random
import time

import constants
import stage
import supervisor
import ugame


def splash_scene():
    # this function is the splash game scene

    # get sound ready
    intro_sound = open("pacman_intro.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(intro_sound)

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
        # wait for 5 seconds then call menu_scene()
        time.sleep(5.0)
        menu_scene()


def instructions_scene():
    # this function is the menu game scene

    # declare image_bank_background variable
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects for instructions
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(10, 10)
    text1.text("Press A to shoot.")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(10, 30)
    text2.text("Press B for speed ")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(10, 50)
    text3.text("boost.")
    text.append(text3)

    text4 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text4.move(10, 70)
    text4.text("Press SELECT to")
    text.append(text4)

    text5 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text5.move(10, 80)
    text5.text("mute game.")
    text.append(text5)

    text6 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text6.move(10, 100)
    text6.text("Press START to go")
    text.append(text6)

    text7 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text7.move(10, 110)
    text7.text("back to menu.")
    text.append(text7)

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

        # if Start is pressed, then reload the game
        if keys & ugame.K_START != 0:
            supervisor.reload()
        # redraw Sprites
        game.tick()


def menu_scene():
    # this function is the menu game scene

    # declare image_bank_background variable
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text objects for menu
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(20, 10)
    text1.text("JulLam Studios")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(10, 90)
    text2.text("START:Game")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(10, 110)
    text3.text("SELECT:Instructions")
    text.append(text3)

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

    # declare is_muted to False
    is_muted = False

    # use a whileTrue loop to keep the game running
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # if Start is pressed, then call game_scene
        if keys & ugame.K_START != 0:
            game_scene(is_muted)

        # if Select is pressed, then call instructions_scene()
        if keys & ugame.K_SELECT != 0:
            instructions_scene()

        # redraw Sprites
        game.tick()


<<<<<<< HEAD
def win_scene():
    # this function is the win scene

    # image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set the background to image 0 in the bank
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # add text objects for win scene
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(43, 60)
    text1.text("You Win!")
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(32, 110)
    text2.text("PRESS SELECT")
    text.append(text2)

    # declare game and set FPS
    game = stage.Stage(ugame.display, constants.FPS)

    # set the game layers
    game.layers = text + [background]

    # render background and sprite list location
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # if Select button is pressed, reload the game
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick()


=======
>>>>>>> 75bf683e25a1bb52729c35d1ddb681d0b1fd2c8c
def game_over_scene(final_score):
    # this function is the game over scene

    # image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set the background to image 0 in the bank
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # add text objects
    text = []
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text1.move(22, 20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text2.move(43, 60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    text3.move(32, 110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # declare game and set FPS
    game = stage.Stage(ugame.display, constants.FPS)

    # set the game layers
    game.layers = text + [background]

    # render background and sprite list location
    game.render_block()

    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # if select is pressed, reload the game
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()

        # update game logic
        game.tick()


def game_scene(is_muted):
    # this function is the main game scene

    # declare lives
    lives = 3

    # display lives text
    life_text = stage.Text(width=29, height=14)
    life_text.clear()
    life_text.cursor(0, 0)
    life_text.move(constants.SCREEN_X - 70, 1)
    life_text.text("Lives: {0}".format(lives))
    # declare score
    score = 0

    # display score text
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    def show_alien():
        # this function takes an alien from off screen and puts on the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                break

    # declare image_bank_background variable
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # declare image_bank_sprites
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that need state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # set ship speed to 1
    ship_speed = 1

    # prepare sound pew_sound
    pew_sound = open("gun_44mag_11.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # declare ship
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # create a list of aliens
    aliens = []

    # populate the list with aliens
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        aliens.append(a_single_alien)

    # place one alien on the screen
    show_alien()

    # create a list of lasers
    lasers = []

    # use a for loop to assign the lasers
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        lasers.append(a_single_laser)

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
    game.layers = [life_text] + [score_text] + lasers + [ship] + aliens + [background]

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

        # if B is pressed, then activate or deactivate speed boost
        if keys & ugame.K_X != 0:
            if ship_speed == 1:
                ship_speed = 2
            else:
                ship_speed = 1

        # if Start is pressed, then pass
        if keys & ugame.K_START != 0:
            pass

        # if Select is pressed, then mute or unmute the game.
        if keys & ugame.K_SELECT != 0:
            if is_muted == False:
                ugame.audio.mute(True)
                is_muted = True
            else:
                ugame.audio.mute(False)
                is_muted = False

        # if right on the d-pad is pressed, move the ship right
        if keys & ugame.K_RIGHT != 0:
            # if the ship's x position <= constants.SCREEN_X, move the ship  right
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + ship_speed, ship.y)
            else:
                # otherwise set the ship's x-position to 0
                ship.move(0, ship.y)

        # if left on the d-pad is pressed
        if keys & ugame.K_LEFT != 0:
            # if the ship's x position >= 0, move the ship left
            if ship.x >= 0:
                ship.move(ship.x - ship_speed, ship.y)
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
        # if the A button was just pressed, play pew sound effect
        if a_button == constants.button_state["button_just_pressed"]:
            # fire a laser using a for loop
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break

        # use a for loop to move the lasers on screen up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # use a for loop to move the aliens on screen down
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(
                    aliens[alien_number].x,
                    aliens[alien_number].y + constants.ALIEN_SPEED,
                )
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

                    # show an alien
                    show_alien()

                    # decrease score by 1
                    score -= 1

                    # if the score is less than 0, make it 0
                    if score < 0:
                        score = 0

                    # display score text
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

                    # set the game layers
                    game.layers = (
                        [life_text]
                        + [score_text]
                        + lasers
                        + [ship]
                        + aliens
                        + [background]
                    )

                    # render background and sprite list location
                    game.render_block()

        # use a nested for loop for the collision between an alien and laser
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(
                            lasers[laser_number].x + 6,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11,
                            lasers[laser_number].y + 12,
                            aliens[alien_number].x + 1,
                            aliens[alien_number].y,
                            aliens[alien_number].x + 15,
                            aliens[alien_number].y + 15,
                        ):
                            # an alien was hit
                            aliens[alien_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            lasers[laser_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            sound.stop()

                            # prepare sound
                            boom_sound = open("alien_boom_one.wav", "rb")
                            sound.play(boom_sound)

                            # make 2 more aliens
                            show_alien()
                            show_alien()

                            # increment score
                            score = score + 1

                            # if the score is , call the win scene
                            if score == 5:
                                win_scene()

                            # display score text
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))

                            # set the game layers
                            game.layers = (
                                [life_text]
                                + [score_text]
                                + lasers
                                + [ship]
                                + aliens
                                + [background]
                            )

                            # render background and sprite list location
                            game.render_block()

        # check if an alien is touching the ship
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(
                    aliens[alien_number].x + 1,
                    aliens[alien_number].y,
                    aliens[alien_number].x + 15,
                    aliens[alien_number].y + 15,
                    ship.x,
                    ship.y,
                    ship.x + 15,
                    ship.y + 15,
                ):
                    # alien hit the ship is true
                    sound.stop()
                    crash_sound = open("explosion_x.wav", "rb")
                    sound.play(crash_sound)
                    lives = lives - 1
                    ship.move(75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
                    if lives == 0:
                        game_over_scene(score)
                    life_text = stage.Text(width=29, height=14)
                    life_text.clear()
                    life_text.cursor(0, 0)
                    life_text.move(constants.SCREEN_X - 70, 1)
                    life_text.text("Lives: {0}".format(lives))

        # redraw Sprites
        game.render_sprites(lasers + [ship] + aliens)
        game.tick()


if __name__ == "__main__":
    splash_scene()
