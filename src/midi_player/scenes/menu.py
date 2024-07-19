import pygame
from typing import Dict, Sequence, Optional, Callable
from scenes.base_scene import BaseScene
from pygame.surface import Surface
from common.event import EventType, GameEvent
from entities.base_entity import BaseEntity
from entities.text_entity import TextEntity
from entities.button_entity import ButtonEntity
from common.utils import Resources
from settings import Settings


class Menu(BaseScene):
    """
    Menu scene is a subclass of the BaseScene
    """
    def __init__(self, screen: Surface, *args, **kwargs) -> None:
        super().__init__(screen, *args, **kwargs)

        self.ss = screen.get_size()
        self.title_size = int((self.ss[0] + self.ss[1])/20)
        self.x_tile = int(self.ss[0]/36)
        self.y_tile = int(self.ss[1]/36)
        title = TextEntity(text="PIANOHERO", size=self.title_size, color=Settings.default_text_color, position=(18 * self.x_tile, 4 * self.y_tile))

        change_to_game = GameEvent(
                init_arg=EventType.CHANGE_SCENE,
                dict={"scene": "game"},
                )
        play_button = ButtonEntity(
            event=change_to_game,
            text="PLAY",
            size=0.8*self.title_size,
            color=Settings.default_text_color,
            position=(18 * self.x_tile, 8 * self.y_tile)
            )

        change_to_options_menu = GameEvent(
                init_arg=EventType.CHANGE_SCENE,
                dict={"scene": "OPTIONS"},
                )
        options_button = ButtonEntity(event=change_to_options_menu,
            text="OPTIONS",
            size=0.8*self.title_size,
            color=Settings.default_text_color,
            position=(18 * self.x_tile, 12 * self.y_tile)
            )
        
        quit_button = ButtonEntity(
            event=GameEvent(init_arg=pygame.QUIT),
            text="QUIT",
            size=0.8*self.title_size,
            color=Settings.default_text_color,
            position=(18 * self.x_tile, 16 * self.y_tile)
            )

        self.selectable = pygame.sprite.Group()
        self.selectable.add(play_button, options_button, quit_button)

        self.entities = pygame.sprite.Group()
        self.entities.add(title, self.selectable)

        self.background: Optional[Surface] = Resources.get_image("menu.jpg", screen.get_size())
        self.event_handler: Optional[Callable] = None
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
        """Updates based on the events that transpire the screen and its entities.

        Parameters
        ----------
        events : Sequence[GameEvent]
            events both1 pygame and custom.
        """
        self.events = events
        if self.event_handler:
            self.event_handler()
            self.entities.update(events.self)

    def render(self, screen: Surface) -> None:
        """Renders all entities in the self.entities dict.

        Parameters
        ----------
        screen : Surface
            surface to render entities to.
        """
        self.entities.draw(screen)
    
    def event_handler(self) -> None:
        """
        Handles events specific to the menu.
        """
        pass
