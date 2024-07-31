from typing import Sequence
from pygame.surface import Surface
from common.event import GameEvent


class BaseScene:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen

    def tick(self, events: Sequence[GameEvent]) -> bool:
        """subclass should overrise."""
