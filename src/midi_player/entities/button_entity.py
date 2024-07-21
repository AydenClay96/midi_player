import pygame
from entities.text_entity import TextEntity
from common.event import GameEvent
from typing import Optional, Sequence


class ButtonEntity(TextEntity):
    def __init__(self,
                 event: GameEvent,
                 text: str,
                 size: int,
                 color: str,
                 hover_color: Optional[str] = None,
                 *args, **kwargs) -> None:
        self.text = text
        self.default_color = color
        self.hover_color = color if hover_color is None else hover_color
        self.color = color
        self.size = size
        super().__init__(self.text, self.size, self.color, *args, **kwargs)
        self.event = event
        self.selected = False

    def update(self, events: Sequence[GameEvent]) -> None:
        self.check_hover()
        self.update_color()
        super().update(events)

    def check_hover(self) -> None:
        if pygame.mouse.get_visible():
            pos = pygame.mouse.get_pos()
            in_vert = pos[0] in range(self.rect.left, self.rect.right)
            in_horz = pos[1] in range(self.rect.top, self.rect.bottom)

            self.selected = in_vert and in_horz

    def update_color(self) -> None:
        self.color = self.hover_color if self.selected else self.default_color

    def action(self) -> None:
        self.event.post()
