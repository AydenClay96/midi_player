import pygame
from pygame.surface import Surface
from entities.base_entity import BaseEntity
from entities.text_entity import TextEntity
from entities.button_entity import ButtonEntity
from common.event import GameEvent, EventType
from common.types import EntityType
from common.utils import Resources
from typing import Optional, Sequence


class SelectorEntity(BaseEntity):
    def __init__(
        self,
        heading: str,
        options: list[str],
        size: int,
        color: str,
        hover_color: Optional[str] = None,
        *args,
        **kwargs
    ) -> None:

        super().__init__(*args, **kwargs)
        self.selection = options[0]
        self.heading = heading
        self.selected = False
        self.size = size
        self.color = color
        self.default_color = color
        self.hover_color = color if hover_color is None else hover_color

        self.text = TextEntity(
            text=self.heading + ": " + self.selection,
            size=self.size,
            color=self.color,
            entity_type=EntityType.TEXT,
            position=self.position
        )

        change_selection = GameEvent(EventType.OPTION_CHANGE, heading=self.heading, selection=self.selection)

        self.left_chevron = ButtonEntity(
            entity_type=EntityType.BUTTON,
            event=change_selection,
            text="<",
            size=self.size,
            color=self.color,
            hover_color=self.hover_color,
            position=(self.position[0] - self.text.rect.centerx / 2, self.position[1]),
        )

        self.right_chevron = ButtonEntity(
            entity_type=EntityType.BUTTON,
            event=change_selection,
            text=">",
            size=self.size,
            color=self.color,
            hover_color=self.hover_color,
            position=(self.position[0] + self.text.rect.centerx / 2, self.position[1]),
        )

        self.render()

    def update(self, events: Sequence[GameEvent]) -> None:
        self.text.update(events)
        self.left_chevron.update(events)
        self.right_chevron.update(events)

        for e in events:
            if e.is_type(pygame.MOUSEBUTTONDOWN):
                print(pygame.mouse.get_pos())

    def on_click(self) -> None:
        pass

    def render(self) -> None:
        self.rect = self.text.rect.unionall((self.left_chevron.rect, self.right_chevron.rect))
        self.image = Surface(self.rect.size)
        self.image.blit(self.text.image, self.rect.center)
        self.image.blit(self.left_chevron.image, (self.left_chevron.position[0], self.rect.centery))
        self.image.blit(self.right_chevron.image, (self.right_chevron.position[0], self.rect.centery))
        print(self.left_chevron.position)
        print(self.right_chevron.position)
        print(self.text.position)
