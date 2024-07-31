import pygame
from pygame.surface import Surface
from common.event import EventType, GameEvent
from scenes.menu import Menu
from scenes.game import Game
from scenes.options import Options


class SceneManager:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.scene = None
        self.scenes = {
            Menu.__name__: Menu(self.screen),
            Game.__name__: Game(self.screen),
            Options.__name__: Options(self.screen),
        }
        self.active_scene = Menu.__name__

    def tick(self) -> bool:
        if pygame.event.peek(pygame.QUIT):
            return False

        pg_events = pygame.event.get()
        events = list(map(GameEvent, pg_events))

        for e in events:
            if e.is_type(EventType.CHANGE_SCENE):
                self.change_scene(e)
            elif e.is_key_up(pygame.K_ESCAPE):
                if self.active_scene == Menu.__name__:
                    return False
                else:
                    self.active_scene = Menu.__name__

        return self.scenes[self.active_scene].tick(events)

    def change_scene(self, event: EventType) -> None:
        self.active_scene = event.event.scene
