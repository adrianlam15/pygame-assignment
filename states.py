import pygame, os

pygame.init()


class Start(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("homescreen.jpg")
        self.image_rect = self.image.get_rect(
            center=(
                self.game.MAIN_SCREEN_WIDTH / 2,
                self.game.MAIN_SCREEN_HEIGHT / 2 - 150,
            )
        )
        self.play_button = pygame.image.load("play_button.jpg")
        self.play_button = pygame.transform.scale(
            self.play_button,
            (self.play_button.get_width() / 2, self.play_button.get_height() / 2),
        )
        self.play_rect = self.image.get_rect(
            center=(
                self.game.MAIN_SCREEN_WIDTH / 2 + 300,
                self.game.MAIN_SCREEN_HEIGHT / 2 + 410,
            )
        )
        self.hover = pygame.image.load("play_button_hover.jpg")
        self.hover = pygame.transform.scale(
            self.hover,
            (self.hover.get_width() / 2, self.hover.get_height() / 2),
        )
        self.hover_rect = self.image.get_rect(
            center=(
                self.game.MAIN_SCREEN_WIDTH / 2 + 300,
                self.game.MAIN_SCREEN_HEIGHT / 2 + 410,
            )
        )
        self.click = False
        self.transition_screen = pygame.Surface(
            (self.game.MAIN_SCREEN_WIDTH, self.game.MAIN_SCREEN_HEIGHT)
        )
        self.transition_screen.fill("Black")
        self.transition_rect = self.transition_screen.get_rect(bottomleft=(0, 0))

    def render(self):
        self.game.MAIN_SCREEN.fill("White")
        self.game.MAIN_SCREEN.blit(self.image, self.image_rect)
        self.game.MAIN_SCREEN.blit(self.play_button, self.play_rect)
        if self.game.play_hover is True and self.click is False:
            self.game.MAIN_SCREEN.blit(self.hover, self.hover_rect)
        if self.click is True:
            if (
                self.transition_rect.y < self.game.MAIN_SCREEN_HEIGHT
                and self.transition_rect.y != 0
            ):
                self.game.MAIN_SCREEN.blit(self.transition_screen, self.transition_rect)
                self.transition_rect.y += 5
                if self.transition_rect.y == 0:
                    self.click = False
                if self.click is False:
                    self.game.MAIN_SCREEN.fill("Black")
                    self.game.start_loop = False
                    self.game.playing = True
                    self.game.start = False
