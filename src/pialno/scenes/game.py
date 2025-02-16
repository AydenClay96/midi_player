import pygame
from typing import Dict, Sequence, Optional, Callable
from scenes.base_scene import BaseScene
from pygame.surface import Surface
from common.event import EventType, GameEvent
from entities.base_entity import BaseEntity
from entities.text_entity import TextEntity
from entities.button_entity import ButtonEntity
from entities.note_entity import NoteEntity
from entities.keyboard_entity import KeyboardEntity
from common.types import EntityType
from common.utils import Resources
from settings import Settings


class Game(BaseScene):
    """
    Game scene is a subclass of the BaseScene
    """

    def __init__(self, screen: Surface, *args, **kwargs) -> None:
        super().__init__(screen, *args, **kwargs)

        self.ss = screen.get_size()
        self.title_size = int((self.ss[0] + self.ss[1]) / 18)
        self.x_tile = int(self.ss[0] / 36)
        self.y_tile = int(self.ss[1] / 36)

        self.button_size = int(self.title_size * 0.80)

        self.keyboard = KeyboardEntity(
            entity_type=EntityType.KEYBOARD,
            position=(int(self.ss[0] / 2), 32 * self.y_tile),
            size=(self.ss[0], 8 * self.y_tile),
        )

        self.entities = pygame.sprite.Group()
        self.entities.add(self.keyboard)

        self.background: Optional[Surface] = Resources.get_image(
            "menu.jpg", screen.get_size()
        )

        self.events: Optional[Sequence[GameEvent]] = None

    def tick(self, events: Sequence[GameEvent]) -> bool:
        """
        Tick this scene at the desired rate.

        Parameters
        ----------
        events : Sequence[GameEvent]
            events both pygame and custom.

        Returns
        -------
        bool
            indicates if the tick was successful and if so continue the game loop.
        """
        super().tick(events)
        if pygame.event.peek(pygame.QUIT):
            return False

        self.screen.blit(self.background, (0, 0))
        self.update(events)
        self.render(self.screen)
        return True

    def update(self, events: Sequence[GameEvent]) -> None:
        """Updates based on the events that transpire
        the screen and its entities.

        Parameters
        ----------
        events : Sequence[GameEvent]
            events both pygame and custom.
        """
        self.event_handler(events)
        self.entities.update(events)

    def render(self, screen: Surface) -> None:
        """Renders all entities in the self.entities dict.

        Parameters
        ----------
        screen : Surface
            surface to render entities to.
        """
        self.entities.draw(screen)

    def event_handler(self, events: Sequence[GameEvent]) -> None:
        """
        Handles events specific to the menu.
        """
        for e in events:
            if e.is_type(pygame.MOUSEBUTTONDOWN):
                position = pygame.mouse.get_pos()
                note = NoteEntity(
                    entity_type=EntityType.NOTE,
                    position=position,
                    life_span=2,
                    speed=1,
                    radius=8,
                )
                self.entities.add(note)
