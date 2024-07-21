from entities.base_entity import BaseEntity
from common.utils import Resources
from typing import Sequence
from common.event import GameEvent


class TextEntity(BaseEntity):
    """Basic Text entity."""

    def __init__(self,
                 text: str,
                 size: int,
                 color: str,
                 *args,
                 **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.text = text
        self.color = color
        self.size = size

        self.font = Resources.get_font(self.size)

        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, events: Sequence[GameEvent]) -> None:
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.position)
