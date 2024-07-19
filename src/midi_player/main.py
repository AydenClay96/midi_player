import pygame
from settings import Settings
from common.utils import Resources, Config
from scenes.scene_manager import SceneManager


class GameManager:
    def __init__(self) -> None:
        pygame.init()
        self.user_config = Config().load()
        self.clock = pygame.time.Clock()
        self.initialize_screen()
        self.scene_manager = SceneManager(self.screen)

    def initialize_screen(self) -> None:
        """
        Initializes the screen based on what is currently in the user config.

        Returns
        -------
        pygame.surface.Surface.
            back-most screen.
        """
        if self.user_config["full_screen"]:
            screen_resolution = tuple(self.user_config["full_screen_res"])
            screen = pygame.display.set_mode(screen_resolution, pygame.FULLSCREEN)
        else:
            screen_resolution = tuple(self.user_config["windowed_res"])
            screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption(Settings.name)
        pygame.display.set_icon(Resources.get_image("icon.jpg"))
        self.screen = screen

    def run(self) -> None:
        """
        Main game loop:
        Starts the pygame processes.
        Starts the screen.
        Has the main loop.
        Directs events to the various scenes.
        """
        running = True
        while running:
            self.screen.fill("Black")
            running = self.scene_manager.tick()
            pygame.display.update()
            self.clock.tick(Settings.fps)


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.run()
