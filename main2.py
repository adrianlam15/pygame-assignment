# imports
import pygame, time, os, random
from barrier import Barrier
from missile import Missile
from mouse import Mouse

# game class
class Game:
    pygame.init()  # initialize pygame module

    # constructor for game class
    def __init__(self):
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = (
            1280,
            720,
        )  # screen width and screen height
        self.running = True  # game state
        self.playing = False  # playing state
        self.FPS = 60  # FPS
        self.clock = pygame.time.Clock()  # clock function
        self.dt, self.time_now, self.prev_time = (
            0,
            0,
            0,
        )  # delta time, current time, and previous time aspect // for framerate independence
        self.missile_group = pygame.sprite.Group()  # set missile group var
        self.barrier_group = pygame.sprite.Group()  # set barrier group car

    # level function of game
    def levels(self):
        self.level_choice = input(
            "Levels: | Normal | Hard | Impossible\nChoice: "
        )  # level choices of game
        while (
            self.level_choice.lower() != "normal"
            and self.level_choice.lower() != "hard"
            and self.level_choice.lower() != "impossible"
        ):  # input validation
            self.level_choice = input(
                "\nInvalid entry.\nLevels: | Normal | Hard | Impossible\nChoice: "
            )
        # if level choice is "normal"
        if self.level_choice.lower() == "normal":
            pygame.time.set_timer(
                pygame.USEREVENT, 1000
            )  # every 1000 ms, a custom event will happen
        # if level choice is "hard"
        elif self.level_choice.lower() == "hard":
            pygame.time.set_timer(
                pygame.USEREVENT, 1000
            )  # every 1000 ms, a custom event will happen
        # if level choice is "impossible"
        elif self.level_choice.lower() == "impossible":
            pygame.time.set_timer(
                pygame.USEREVENT, 500
            )  # every 500 ms, a custom event will happen
        self.playing = True

    """# restart function // for future
    def restart_choice(self):
        restart_choice = input("Restart game? (y/n):\n")
        if restart_choice.lower() == "y":
            self.playing = True
        else:
            exit()"""

    # initalize SCREEN of program
    def SCREEN(self):
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )  # initialize window
        self.CAPTION = pygame.display.set_caption(
            "Mr. Garvin's Nuclear Madness"
        )  # set caption of window
        self.icon = pygame.display.set_icon(
            pygame.image.load("missile.png")
        )  # set icon of window

    # Experimental restart function // for future
    """# main loop function of game
    def main_loop(self):
        while self.running:
            self.levels()
            self.SCREEN()
            self.load_barrier()
            while self.playing:
                if self.playing is True:
                    self.get_event()
                    self.spawn_rate_missile()
                    self.collision_detection()
                    self.determine_endgame()
                    self.render()

            while self.playing is False:
                self.restart_choice()"""
    # main loop function of game // function calls
    def main_loop(self):
        if self.playing:
            self.get_event()
            self.collision_detection()
            self.determine_endgame()
            self.render()
        else:
            print("GAME OVER!")
            exit()  # exit game

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
            if (
                event.type == pygame.USEREVENT
            ):  # call missile_logic() function when event.type == pygame.USEREVENT
                self.missile_logic()
            if (
                event.type == pygame.MOUSEBUTTONDOWN
            ):  # detect when event.type == pygame.MOUSEBUTTON
                self.mouse_pos = (
                    Mouse()
                )  # call custom Mouse() class which returns x, y of mouse
                for (
                    self.missile
                ) in self.missile_group:  # checking which missile what clicked
                    if self.missile.rect.collidepoint(
                        self.mouse_pos.x, self.mouse_pos.y
                    ):  # checking for collision
                        self.missile.kill()  # removing missile from group and removing it's instanced

    # check asset function of game
    def check_assets(self):
        pass

    # load barrier function of game
    def load_barrier(self):
        for y in range(
            0, self.SCREEN_HEIGHT, 128
        ):  # load barried according to screen height
            self.barrier = Barrier(self, 150, y)
            self.barrier_group.add(
                self.barrier
            )  # add barrier instance to barrier group

    # missile logic function of game // creates an instance of missile object
    def missile_logic(self):
        print("normal")
        self.missile = Missile(self, 3)
        # missile speed changed for "hard" mode
        if self.level_choice.lower() == "hard":
            self.missile = Missile(self, random.randint(7, 13))
        # missile speed changed for "impossible" mode
        if self.level_choice.lower() == "impossible":
            for num in range(10):  # spam missiles
                self.missile = Missile(self, random.randint(23, 30))
                self.missile_group.add(self.missile)

    # collision detection function of game
    def collision_detection(self):
        # collision detection for "normal" mode
        if self.level_choice.lower() == "normal":
            for self.barrier in self.barrier_group:
                if pygame.sprite.spritecollideany(
                    self.barrier, self.missile_group
                ):  # if program detects collision between barrier and missile group
                    if pygame.sprite.groupcollide(
                        self.missile_group, self.barrier_group, True, False
                    ):  # removes missile after collision with barrier // if program detects collision between missile group and barrier group
                        self.barrier.damage += 1  # set barrier damage value
                        self.barrier.update()  # update barrier image
        # collision detection for "hard" mode
        elif self.level_choice.lower() == "hard":  # collision detection for "hard" mode
            for self.barrier in self.barrier_group:
                if pygame.sprite.spritecollideany(
                    self.barrier, self.missile_group
                ):  # if program detects collision between barrier and missile group
                    self.barrier.damage += 1  # set barrier damage value
                    self.barrier.update()  # update barrier image // not necessarily needed but the animation is pleasing
        # collision detection for "impossible" mode
        else:
            for self.barrier in self.barrier_group:
                if pygame.sprite.spritecollideany(
                    self.barrier, self.missile_group
                ):  # if program detects collision between barrier and missile group
                    self.barrier.damage += 1  # set barrier damage value
                    self.barrier.update()  # update barrier image // not necessarily needed but the animation is pleasing

    # determine endgame function of game // if user has lost
    def determine_endgame(self):
        if (
            len(self.barrier_group) == 0
        ):  # user has lost when barrier group is empty // no barrier remaining
            self.playing = False  # update playing attribute of class

    # render function of game
    def render(self):
        self.SCREEN.fill("White")  # makes main surface white
        self.barrier_group.draw(self.SCREEN)  # draws barrier group on main screen
        self.missile_group.draw(self.SCREEN)  # draws missile group on main screen

        # update methods
        self.missile_group.update()  # update missile group speed
        self.barrier_group.update()  # update barrier group state
        pygame.display.update()  # updating overall display of game
        self.clock.tick(self.FPS)


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
