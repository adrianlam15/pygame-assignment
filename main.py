from barrier import Barrier
from missile import Missile

# imports
import pygame, time, os

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
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )  # initialize window
        self.CAPTION = pygame.display.set_caption(
            "Hello There!"
        )  # set caption of window
        self.FPS = 60  # FPS
        self.clock = pygame.time.Clock()
        self.dt, self.time_now, self.prev_time = (
            0,
            0,
            0,
        )  # delta time, current time, and previous time aspect // for framerate independence
        self.missile_group = pygame.sprite.Group()
        self.barrier_group = pygame.sprite.Group()
        self.asset_dir = os.path.join("assets")

    # main loop funtion of game
    def main_loop(self):
        self.get_event()
        self.render()

    # delta time function
    def delta_time(self):
        self.time_now = time.time()
        self.dt = self.time_now - self.prev_time
        self.dt *= self.FPS
        self.prev_time = self.time_now

    # get event function of game
    def get_event(self):
        self.event = pygame.event.get()  # get events in self.event var
        for event in self.event:
            if event.type == pygame.QUIT:
                pygame.quit()

    # load asset function of game
    def load_assets(self):
        self.missile = Missile(
            self, 1280, 0, 3
        )  # missile arguments (game, x, y, speed)
        self.missile_group.add(self.missile)
        self.barrier = Barrier(self, 350, 50)  # barrier arguments (game, x, y)
        self.barrier_group.add(self.barrier)

    # render function of game
    def render(self):
        self.SCREEN.fill("Black")
        self.SCREEN.blit(self.missile.surface, self.missile.rect)
        self.SCREEN.blit(self.barrier.surface, self.barrier.rect)
        self.missile.update()
        self.barrier.update(0)
        pygame.display.update()
        self.clock.tick(self.FPS)


# main program
game = Game()
if __name__ == "__main__":
    game.load_assets()
    while game.running:
        game.main_loop()
