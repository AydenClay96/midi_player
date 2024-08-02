import pygame
from entities.base_entity import BaseEntity
from typing import Sequence, Tuple
from common.event import GameEvent


class StaveEntity(BaseEntity):
    """Basic Stave entity."""

    def __init__(
        self, start: str, spread: int, size: Tuple[int, int, int, int], *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.start = start
        self.spread = spread

        self.image = pygame.surface.Surface(size=size)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, events: Sequence[GameEvent]) -> None:
        pass

    def initialize_stave(self) -> None:
        pass
