# imports and inits
import pygame, os

pygame.init()


# missile class
class Missile(pygame.sprite.Sprite):  # inherit attrs from pygame Sprite class
    # initialize values of missile
    def __init__(self, game, x, y, speed):
        self.x = x
        self.y = y
        self.game = game
        self.speed = speed  # speed attr
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(self.game.asset_dir, "missile.png")
        )  # loading image of missile
        self.surface = pygame.Surface(
            (self.image.get_width(), self.image.get_height())
        )  # get surface with image width and height
        self.surface.blit(self.image, (0, 0))  # blit image onto surface
        self.rect = self.surface.get_rect(
            topleft=(self.x, self.y)
        )  # get rect coords of surface

        pygame.mixer.init()  # initialize music in pygame
        """self.sound = pygame.mixer.Sound("launch.ogg").play()  # play music"""

    # update function for speed
    def update(self):
        self.rect.x -= self.speed  # move missile left
