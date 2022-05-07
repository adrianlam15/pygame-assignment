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
            self.images.append(
                pygame.image.load(os.path.join(self.game.asset_dir, f"barrier{N}.png"))
            )

        self.surface = pygame.Surface(
            (self.images[0].get_width(), self.images[0].get_height())
        )  # make surface with image attributes
        self.surface.blit(self.images[0], (0, 0))  # blit image onto surface
        self.rect = self.surface.get_rect(
            topleft=(self.x, self.y)
        )  # get rect of surface
        pygame.mixer.init()

    # update function
    def update(self, damage=0):  # damage attr to update pygame surface
        self.damage = damage
        if self.damage == 1:  # changing surface or img based on damage attr
            self.surface = pygame.Surface(
                (self.images[1].get_width(), self.images[1].get_height())
            )
            self.surface.blit(self.images[1], (0, 0))
            """self.sound = pygame.mixer.Sound("hit.ogg").play()  # play sound"""
        elif self.damage == 2:
            self.surface = pygame.Surface(
                (self.images[2].get_width(), self.images[2].get_height())
            )
            self.surface.blit(self.images[2], (0, 0))
            """self.sound = pygame.mixer.Sound("hit.ogg").play()  # play sound"""
        self.rect = self.surface.get_rect(
            topleft=(self.x, self.y)
        )  # get rect of surface
