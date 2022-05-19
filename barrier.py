# Lam, Adrian (705929)
# ICS4U: Pygame Sprites - Barrier Class
# 2022-05-09
#
# Program contains required libraries and modules to define the barrier class for
# main game program. Attributes include main game class, x-position, y-positon and
# inherited attributes from the pygame Sprite class. Since Barrier class contains a specific
# sound on hit when in contact with missile, the sound attributes of Barrier class only plays
# when update() is called. The update() uses the default argument 'damage=0' to assume that
# damage is equal to 0 when not specified. Program also initializes images and stores in the 'images'
# attribute of Barrier class. An image(s) are then placed on a surface with the image dimensions,
# then the get_rect() function is then used to specify where the barrier would like to be placed in
# main program.
#
# EDIT: game, x, and y arguments were added so inherit attributes from main game class for future
# use. x, and y arguments were added to specify where the barrier would like to be placed in the future
# in the main game program.

# imports and inits
import pygame, os

pygame.init()


# class barrier
class Barrier(pygame.sprite.Sprite):  # inherit attrs from pygame Sprite class
    # initalize values for Barrier class
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        super().__init__()
        self.damage = 0  # init value of damage
        self.images = []  # list of images
        for N in range(1, 4):  # loop to append images
            self.images.append(pygame.image.load(f"barrier{N}.png"))
        self.surface = pygame.Surface(
            (self.images[0].get_width(), self.images[0].get_height())
        )  # make surface with image attributes
        self.surface.blit(self.images[0], (0, 0))  # blit image onto surface
        self.rect = self.surface.get_rect(
            topleft=(self.x, self.y)
        )  # get rect of surface
        pygame.mixer.init()
        self.image = self.images[0]

    # update function
    def update(self):  # damage attr to update pygame surface
        if self.damage == 1:  # changing surface or img based on damage attr
            self.surface = pygame.Surface(
                (self.images[1].get_width(), self.images[1].get_height())
            )
            self.surface.blit(self.images[1], (0, 0))
            """self.sound = pygame.mixer.Sound("hit.ogg").play()  # play sound"""
            self.image = self.images[1]
            self.damage = 1
        elif self.damage == 2:
            self.surface = pygame.Surface(
                (self.images[2].get_width(), self.images[2].get_height())
            )
            self.surface.blit(self.images[2], (0, 0))
            """self.sound = pygame.mixer.Sound("hit.ogg").play()  # play sound"""
            self.image = self.images[2]
        elif self.damage >= 3:
            pygame.sprite.Sprite.kill(self)
        self.rect = self.surface.get_rect(
            topleft=(self.x, self.y)
        )  # get rect of surface
