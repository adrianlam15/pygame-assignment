# Lam, Adrian (705929)
# ICS4U: Pygame Sprites - Main Game Class
# 2022-05-14
#
# Program contains the required libraries and modules as well as the main Game
# object/class required to run the game. Multiple objects/classes were called
# from other files in order to organize code and formatting.

# imports
import pygame
from barrier import Barrier
from missile import Missile
from states import Start
from states import End


# game class
class Game:
    pygame.init()  # initialize pygame module

    # constructor for game class
    def __init__(self):
        self.MAIN_SCREEN_WIDTH, self.MAIN_SCREEN_HEIGHT = (
            1280,
            720,
        )  # screen width and screen height
        # boolean values
        self.running = True  # game state
        self.playing = False  # playing state
        self.end = False
        self.restart = True
        self.start = True
        self.start_loop = True
        # misc.
        self.FPS = 60  # FPS
        self.clock = pygame.time.Clock()  # clock function
        self.dt, self.time_now, self.prev_time = (
            0,
            0,
            0,
        )  # delta time, current time, and previous time aspect // for framerate independence
        self.score = 0
        self.missile_speed = 3
        self.level = 0
        self.prev_level = 0
        self.state_stack = []
        # assigning class variables and groups
        self.start_state = Start(self)
        self.end_state = End(self)
        self.missile_group = pygame.sprite.Group()  # set missile group var
        self.barrier_group = pygame.sprite.Group()  # set barrier group car
        """self.music = pygame.mixer.Sound("music.ogg").play()"""

    # level function of game // input validation for future
    def levels(self):
        self.playing = True
        pygame.time.set_timer(
            pygame.USEREVENT, 1000
        )  # every 1000 ms send a USEREVENT to event handler // handles missile spawn rate

    # initalize SCREEN of program
    def SCREEN(self):
        self.MAIN_SCREEN = pygame.display.set_mode(
            (self.MAIN_SCREEN_WIDTH, self.MAIN_SCREEN_HEIGHT)
        )  # initialize window
        self.CAPTION = pygame.display.set_caption(
            "Mr. Garvin's Nuclear Madness"
        )  # set caption of window
        self.icon = pygame.display.set_icon(pygame.image.load("missile.png"))

    # main loop function of game // function calls
    def main_loop(self):
        self.get_state()  # basic state machine of game // not optimized
        if self.start_loop:  # start loop // main menu
            self.playing = False
            self.load_text()  # load text function of game prior
            self.get_event()  # event handler
            self.render()  # render handler
        # function calls when user is playing
        if self.playing:
            self.get_event()  # event handler
            self.collision_detection()  # handles collisions
            self.determine_endgame()  # determines the game's ending phase
            self.load_text()  # load text function of game prior
            self.render()  # render handler
        # function calls when user is not playing and reaches end phase
        elif self.playing is False and self.end is True:
            self.get_event()
            self.render()  # render handler

    """# delta time function // for future
    def delta_time(self):
        self.time_now = time.time()
        self.dt = self.time_now - self.prev_time
        self.dt *= self.FPS
        self.prev_time = self.time_now"""

    # get event function of game
    def get_event(self):
        self.event = pygame.event.get()  # get events in self.event var
        for event in self.event:
            if event.type == pygame.QUIT:  # quit program / game
                pygame.quit()
            if self.playing is True:
                if (
                    event.type == pygame.USEREVENT
                ):  # call missile_logic() function when event.type == pygame.USEREVENT
                    self.missile_logic()
                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                ):  # detect when event.type == pygame.MOUSEBUTTON
                    for (
                        self.missile
                    ) in self.missile_group:  # checking which missile what clicked
                        if self.missile.rect.collidepoint(
                            pygame.mouse.get_pos()
                        ):  # checking for collision
                            self.missile.kill()  # removing missile from group and removing it's instanced
                            self.score += (
                                1  # update score on missiles removed from game
                            )
            # methods for handling different animations for mouse hovering and selection of "play" game
            if self.start_loop is True:
                mouse_pos = pygame.mouse.get_pos()  # get x, y of mouse
                if self.start_state.hover_rect.collidepoint(
                    mouse_pos
                ):  # detects collision between rect obj and mouse positioning
                    self.start_state.play_hover = (
                        True  # returns a 'True' boolean value to class attr
                    )
                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                    ):  # if event handler detects mouse button down
                        self.start_state.click = (
                            True  # returns a 'True' boolean value to class attr
                        )
                else:  # if hovering is not detected
                    self.start_state.play_hover = (
                        False  # returns a 'False' boolean value to class attr
                    )
            # end game phase
            if self.end is True:
                mouse_pos = pygame.mouse.get_pos()  # get x, y of mouse
                if self.end_state.respawn.button_rect.collidepoint(
                    mouse_pos
                ):  # detects collision between button obj and mouse positioning
                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                    ):  # if event handler detects mouse button down
                        self.end_state.actions[
                            "Restart"
                        ] = True  # returns a 'True' boolean value to class attr
                elif self.end_state.quit.button_rect.collidepoint(mouse_pos):
                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                    ):  # detects collision between button obj and mouse positioning
                        self.end_state.actions[
                            "Quit"
                        ] = True  # returns a 'True' boolean value to class attr
                        exit()

    # check asset function of game
    def check_assets(self):
        pass

    # load barrier function of game
    def load_barrier(self):
        for y in range(
            0, self.MAIN_SCREEN_HEIGHT, 128
        ):  # load barried according to screen height
            self.barrier = Barrier(self, 150, y)
            self.barrier_group.add(
                self.barrier
            )  # add barrier instance to barrier group

    # missile logic function of game // creates an instance of missile object
    def missile_logic(self):
        self.missile = Missile(
            self, self.missile_speed
        )  # create missile objects // call classes
        self.level = self.score // 5  # level update
        if self.prev_level < self.level:
            self.missile_speed += (
                self.level
            )  # increases missile speed according to level
            self.prev_level = self.level  # sets previous level to current level
        self.missile_group.add(self.missile)  # adds missile object to missile group

    # collision detection function of game
    def collision_detection(self):
        # for detecting which barrier experienced collision
        for self.barrier in self.barrier_group:
            if pygame.sprite.spritecollideany(
                self.barrier, self.missile_group
            ):  # if program detects collision between barrier and missile group
                if pygame.sprite.groupcollide(
                    self.missile_group, self.barrier_group, True, False
                ):  # removes missile after collision with barrier // if program detects collision between missile group and barrier group
                    self.barrier.damage += 1  # set barrier damage value
                    self.barrier.update()  # update barrier image

    # determine endgame function of game // if user has lost
    def determine_endgame(self):
        # for detecting which missile reached end of screen (end game)
        for self.missile in self.missile_group:
            if (
                self.missile.rect.centerx <= 0
            ):  # if x of rect coords is smaller or equal to 0
                self.playing = False  # set playing attr to 'False'
                self.end = True  # set end attr to 'True

    # loading text function of game
    def load_text(self):
        # if playing attr is 'True'
        if self.playing:
            self.score_load = pygame.font.Font("Grobold.ttf", 45)  # load score font
            self.score_render = self.score_load.render(
                f"Score: {self.score}", True, "Black"
            )  # render score
            self.level_font = pygame.font.Font("Grobold.ttf", 45)  # load level font
            self.level_render = self.level_font.render(
                f"Level: {self.level}", True, "Black"
            )  # render level
        # if playing attr is 'False'
        if self.playing is False:
            self.end_font = pygame.font.Font("Grobold.ttf", 80)  # load end font
            self.end_render = self.end_font.render(
                "Game Over!", True, "Red"
            )  # render end

    # render function of game
    def render(self):
        # if playing attr is 'True'
        if self.playing is True:
            self.MAIN_SCREEN.fill("White")  # makes main surface white
            self.barrier_group.draw(
                self.MAIN_SCREEN
            )  # draws barrier group on main screen
            self.missile_group.draw(
                self.MAIN_SCREEN
            )  # draws missile group on main screen

            # update methods
            self.missile_group.update()  # update missile group speed
            self.barrier_group.update()  # update barrier group state
            # drawing text
            self.MAIN_SCREEN.blit(
                self.score_render, (self.MAIN_SCREEN_WIDTH / 2, 50)
            )  # draws score text
            self.MAIN_SCREEN.blit(self.level_render, (1100, 50))  # draws level text
        # if playing attr is 'False' and start_loop attr is 'True' -> main menu
        elif self.playing is False and self.start_loop is True:
            self.state_stack[
                -1
            ].render()  # calls render function in last value in state stack
        # if playing attr is 'False' and end attr is 'True' -> end game state
        elif self.playing is False and self.end is True:
            self.state_stack[
                -1
            ].render()  # calls render function in last vlaue in state stack
        pygame.display.update()  # updating overall display of game
        self.clock.tick(self.FPS)  # sets FPS of game

    # get state function of game
    def get_state(self):
        # if state stack list is empty, add main menu
        if len(self.state_stack) == 0:
            self.state_stack.append(self.start_state)
        # if user reaches end game, add end state
        if self.end is True:
            if len(self.state_stack) == 1:
                self.state_stack.append(self.end_state)

    # remove state function of game // not required as user may quit as this program is limited and the representation of stacks is poor
    def remove_state(self):
        if len(self.state_stack) != 0:
            self.state_stack.pop(-1)


# main program
game = Game()
if __name__ == "__main__":
    # pre-load functions
    game.check_assets()
    game.load_barrier()
    game.levels()
    game.SCREEN()

    # main loop
    while game.running:
        game.main_loop()
