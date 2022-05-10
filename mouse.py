import pygame

pygame.init()


class Mouse(pygame.sprite.Sprite):  # inherit attrs from pygame Sprite class
    def __init__(self):
        self.x, self.y = pygame.mouse.get_pos()  # get position of x, y of mouse
