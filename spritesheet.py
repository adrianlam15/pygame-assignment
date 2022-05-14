import pygame


class Spritesheet:
    def __init__(self, game):
        self.game = game
        self.spritesheet = pygame.image.load("spritesheet.txt")
        self.sprites = []

    def get_sprite(self):
        with open("spritesheet.txt", "r") as input_file:
            for elem in input_file:
                pass
