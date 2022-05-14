# Lam, Adrian (705929)
# ICS4U: Pygame Sprites - Missile Class
# 2022-05-14
#
# Program contains required librarier and modules to define Start and End
# objects/classes. Each class takes their own respective args which are then
# called and objects are created in the main Game class.

# imports and inits
import pygame, os, time
from button import Button

pygame.init()


# classes
# class Start
class Start(pygame.sprite.Sprite):  # inherit attrs from pygame Sprite class
    def __init__(self, game):  # initialize values of Start
        super().__init__()
        self.game = game
        self.image = pygame.image.load(
            "homescreen.jpg"
        )  # loading image of start screen
        self.image_rect = self.image.get_rect(
            center=(
                self.game.MAIN_SCREEN_WIDTH / 2,
                self.game.MAIN_SCREEN_HEIGHT / 2 - 150,
            )  # get rect obj of image attr
        )
        self.play_button = pygame.image.load(
            "play_button.jpg"
        )  # loading image of play button
        self.play_button = pygame.transform.scale(
            self.play_button,
            (self.play_button.get_width() / 2, self.play_button.get_height() / 2),
        )  # scale play button
        self.play_rect = self.image.get_rect(
            center=(
                self.game.MAIN_SCREEN_WIDTH / 2 + 300,
                self.game.MAIN_SCREEN_HEIGHT / 2 + 410,
            )
        )  # get rect obj of play button attr
        self.hover = pygame.image.load(
            "play_button_hover.jpg"
        )  # loading image of hovering over play button
        self.hover = pygame.transform.scale(
            self.hover,
            (self.hover.get_width() / 2, self.hover.get_height() / 2),
        )  # scale hover button
        self.hover_rect = self.image.get_rect(
            center=(
                self.game.MAIN_SCREEN_WIDTH / 2 + 300,
                self.game.MAIN_SCREEN_HEIGHT / 2 + 410,
            )
        )  # get rect obj of hover button attr
        self.play_hover = False  # hovering is initally 'False'
        self.click = False  # click is initially 'False'
        self.transition_screen = pygame.Surface(
            (self.game.MAIN_SCREEN_WIDTH, self.game.MAIN_SCREEN_HEIGHT)
        )  # creating transition screen surface obj
        self.transition_screen.fill("Black")  # making transition_screen black
        self.transition_rect = self.transition_screen.get_rect(
            bottomleft=(0, 0)
        )  # get rect obj of transition screen

    # render function of Start class
    def render(self):
        self.game.MAIN_SCREEN.fill("White")  # fill main surface "white"
        self.game.MAIN_SCREEN.blit(self.image, self.image_rect)  # draw start attr
        self.game.MAIN_SCREEN.blit(
            self.play_button, self.play_rect
        )  # draw play button attr
        # if play hover attr is 'False' and click attr is 'False'
        if self.play_hover is True and self.click is False:
            self.game.MAIN_SCREEN.blit(
                self.hover, self.hover_rect
            )  # blit hover picture
        # if user has clicked // click attr is 'True'
        if self.click is True:
            if (
                self.transition_rect.y < self.game.MAIN_SCREEN_HEIGHT
                and self.transition_rect.y != 0
            ):
                self.game.MAIN_SCREEN.blit(self.transition_screen, self.transition_rect)
                self.transition_rect.y += 5
                if self.transition_rect.y == 0:
                    # updates attrs from main game class or attrs from self
                    self.click = False
                    self.game.MAIN_SCREEN.fill("Black")
                    self.game.start_loop = False
                    self.game.playing = True
                    self.game.start = False


# class End
class End(pygame.sprite.Sprite):  # inherit attrs from pygame Sprite class
    def __init__(self, game):
        self.sound = pygame.mixer.Sound("end_game_sound.ogg").play()
        self.game = game
        self.respawn = Button(
            self.game, 325, 372, 650, 61
        )  # creates objects based off Button class
        self.quit = Button(
            self.game, 325, 451, 650, 61
        )  # creates objects based off Button class
        super().__init__()
        self.image = pygame.image.load("dead.png")  # loading image of end state
        self.image = pygame.transform.scale(
            self.image, (self.game.MAIN_SCREEN_WIDTH, self.game.MAIN_SCREEN_HEIGHT)
        )  # scale image to screen
        self.image_rect = self.image.get_rect(topleft=(0, 0))  # get rect of image attr
        self.text_font = pygame.font.Font("Grobold.ttf", 60)  # load text font
        self.text_render = self.text_font.render(
            "Game does not have current restart function, check back later.",
            True,
            "Red",
        )  # render text
        self.actions = {"Restart": False, "Quit": False}

    # render function of End class
    def render(self):
        self.game.MAIN_SCREEN.blit(
            self.image, self.image_rect
        )  # draws image onto main screen
        # updates "Restart" value
        if self.actions["Restart"] is True:
            self.game.MAIN_SCREEN.blit(
                self.text_render, (0, 0)
            )  # draw text onto main screen
        # updates "Quit" value
        elif self.actions["Quit"] is True:
            exit()
