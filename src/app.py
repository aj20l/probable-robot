from random import choice, randint, random, shuffle
from enum import Enum
import pygame, pgzero, pgzrun, sys

class App():
        
        def __init__(self, pos, dir_x):
                return 0

            


                
class MenuScreen():
        def __init__(self, pos, dir_x):
                return 0 
        def update():
    
                global  game

                if state == State.MENU:
                        if space_pressed():
                        # Switch to play state, and create a new Game object, passing it a new Player object to use
                                state = State.PLAY
                        game = Game(Player())
                else:
                        game.update()

                
            
        def draw():
                game.draw()

                if state == State.MENU:
                        # Draw title screen
                        screen.blit("title", (0, 0))

        # Draw "Press SPACE" animation, which has 10 frames numbered 0 to 9
        # The first part gives us a number between 0 and 159, based on the game timer
        # Dividing by 4 means we go to a new animation frame every 4 frames
        # We enclose this calculation in the min function, with the other argument being 9, which results in the
        # animation staying on frame 9 for three quarters of the time. Adding 40 to the game timer is done to alter
        # which stage the animation is at when the game first starts
                        anim_frame = min(((game.timer + 40) % 160) // 4, 9)
                        screen.blit("space" + str(anim_frame), (130, 280))




class PLayScreen():
        def __init__(self, pos, dir_x):
                return 0
        def update():
    
                global  game


                if state == State.PLAY:
                        if game.player.lives < 0:
                                game.play_sound("over")
                                state = State.GAME_OVER
                        else:
                                game.update()

            
        def draw():
                game.draw()


                if state == State.PLAY:
                        draw_status()


class GameOverScreen():
        def __init__(self, pos, dir_x):
                return 0  
        def update():
    
                global  game


                if state == State.GAME_OVER:
                        if space_pressed():
                                # Switch to menu state, and create a new game object without a player
                                state = State.MENU
                                game = Game()
               
            
        def draw():
                game.draw()

                if state == State.GAME_OVER:
                        draw_status()
        # Display "Game Over" image
                        screen.blit("over", (0, 0))
    