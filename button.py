# Lam, Adrian (705929)
# ICS4U: Pygame Sprites - Button Class
# 2022-05-14
#
# Program contains required libraries and modules to define Button class used for end
# state class. Attributes include game, x, y, w, and h. Program creates a surface based
# on the arguments and returns a surface and a rect obj.

# imports and inits
import pygame

pygame.init()

# class Button
class Button(pygame.sprite.Sprite):  # inherit attrs from pygame Sprite class
    def __init__(self, game, x, y, w, h):  # initial values of button
        self.game = game
        super().__init__()
        self.button = pygame.Surface((w, h))  # makes surface according to w and h
        self.button_rect = self.button.get_rect(
            topleft=(x, y)
        )  # get rect obj based off x and y
