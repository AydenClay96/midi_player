import pygame
from typing import Dict, Sequence, Optional, Callable
from scenes.base_scene import BaseScene
from pygame.surface import Surface
from common.event import EventType, GameEvent
from entities.base_entity import BaseEntity
from entities.text_entity import TextEntity
from entities.button_entity import ButtonEntity
from common.types import EntityType
from common.utils import Resources
from settings import Settings


class Menu(BaseScene):
    """
    Menu scene is a subclass of the BaseScene
    """

    def __init__(self, screen: Surface, *args, **kwargs) -> None:
        super().__init__(screen, *args, **kwargs)

        self.ss = screen.get_size()
        self.title_size = int((self.ss[0] + self.ss[1]) / 18)
        self.x_tile = int(self.ss[0] / 36)
        self.y_tile = int(self.ss[1] / 36)

        self.button_size = int(self.title_size * 0.80)
        bx = int(self.ss[0] / 2)
        by = int(14 * self.y_tile)
        bo = int(self.ss[1] / 4)

        title = TextEntity(
            entity_type=EntityType.TEXT,
            text=Settings.name,
            size=self.title_size,
            color=Settings.default_text_color,
            position=(18 * self.x_tile, 4 * self.y_tile),
        )

        change_to_game = GameEvent(
            init_arg=EventType.CHANGE_SCENE,
            scene="Game",
        )
        play_button = ButtonEntity(
            entity_type=EntityType.BUTTON,
            event=change_to_game,
            text="PLAY",
            size=self.button_size,
            color=Settings.default_text_color,
            hover_color=Settings.hovered_text_color,
            position=(bx, by),
        )

        change_to_options_menu = GameEvent(
            init_arg=EventType.CHANGE_SCENE,
            scene="Options",
        )
        options_button = ButtonEntity(
            entity_type=EntityType.BUTTON,
            event=change_to_options_menu,
            text="OPTIONS",
            size=self.button_size,
            color=Settings.default_text_color,
            hover_color=Settings.hovered_text_color,
            position=(bx, by + bo),
        )

        quit_button = ButtonEntity(
            entity_type=EntityType.BUTTON,
            event=GameEvent(init_arg=pygame.QUIT),
            text="QUIT",
            size=self.button_size,
            color=Settings.default_text_color,
            hover_color=Settings.hovered_text_color,
            position=(bx, by + 2 * bo),
        )

        self.selectable = pygame.sprite.Group()
        self.selectable.add(play_button, options_button, quit_button)
        self.selected = None

        self.entities = pygame.sprite.Group()
        self.entities.add(title, self.selectable)

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
        pass
