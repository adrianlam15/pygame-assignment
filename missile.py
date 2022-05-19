# Lam, Adrian (705929)
# ICS4U: Pygame Sprites - Missile Class
# 2022-05-09
#
# Program contains required libraries and modules to define the barrier class for main game
# program. Attributes include main game class, x-position, y-positon, speed of missile and
# inherited attributes from the pygame Sprite class. An image is then placed on a surface with
# the image dimensions, then the get_rect() function is then used to specify where the barrier
# would like to be placed in main program. Class Missile also contains an update() method to update
# the movement/position of the blitted image on the main surface/screen.
#
# EDIT: game, x, and y arguments were added so inherit attributes from main game class for future
# use. x, and y arguments were added to specify where the barrier would like to be placed in the future
# in the main game program.


# imports and inits
import pygame, os, random

pygame.init()


# missile class
class Missile(pygame.sprite.Sprite):  # inherit attrs from pygame Sprite class
    # initialize values of missile
    def __init__(self, game, speed):
        self.game = game
        self.x = self.game.MAIN_SCREEN_WIDTH
        self.y = random.randint(0, self.game.MAIN_SCREEN_HEIGHT)
        self.speed = speed  # speed attr
        super().__init__()
        self.image = pygame.image.load("missile.png")  # loading image of missile
        self.surface = pygame.Surface(
            (self.image.get_width(), self.image.get_height())
        )  # get surface with image width and height
        """self.surface.set_colorkey("Black")"""
        self.surface.blit(self.image, (0, 0))  # blit image onto surface
        self.rect = self.surface.get_rect(
            topleft=(self.x, self.y)
        )  # get rect coords of surface
        pygame.mixer.init()  # initialize music in pygame
        self.sound = pygame.mixer.Sound("launch.ogg").play()

    # update function for speed
    def update(self):
        self.rect.x -= self.speed  # move missile left

    def kill(self):
        pygame.sprite.Sprite.kill(self)
