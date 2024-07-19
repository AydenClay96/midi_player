import pygame
from pygame.surface import Surface
from common.event import EventType, GameEvent
from scenes.menu import Menu

class SceneManager:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.scene = None
        self.scenes = {
            Menu.__name__: Menu(self.screen)
        }
        self.active_scene = Menu.__name__

    def tick(self) -> bool:
        if pygame.event.peek(pygame.QUIT):
            return False

        pg_events = pygame.event.get()
        events = list(map(GameEvent, pg_events))

        for e in events:
            if e.is_type(EventType.CHANGE_SCENE):
                self.change_scene(e.target)
            elif e.is_key_up(pygame.K_ESCAPE):
                return False

        return self.scenes[self.active_scene].tick(events)
