from entities.base_entity import BaseEntity
from common.utils import Resources
from typing import Sequence
from common.event import GameEvent


class TextEntity(BaseEntity):
    """Basic Text entity."""

    def __init__(self, text: str, size: int, color: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.text = text
        self.color = color
        self.size = size

        self.words_font = Resources.get_font(self.size, "font")
        self.shadow_font = Resources.get_font(int(self.size * 1.001), "font")

        self.words = self.words_font.render(self.text, True, self.color)
        self.image = self.shadow_font.render(self.text, True, "Black")
        self.rect = self.image.get_rect(center=self.position)
        self.image.blit(self.words, (0, 0))

    def update(self, events: Sequence[GameEvent]) -> None:
        self.image = self.shadow_font.render(self.text, True, "Black")
        self.words = self.words_font.render(self.text, True, self.color)
        self.image.blit(self.words, (0, 0))
