from entities.base_entity import BaseEntity
from typing import Sequence
from common.event import EventType
import pygame


class NoteEntity(BaseEntity):
    """Note entity."""

    def __init__(self, speed: int, radius: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.speed = speed
        self.radius = radius
        self.birthdate = pygame.time.get_ticks() * 1e-3

    def update(self, events: Sequence[EventType]) -> None:
        x_pos = self.position[0] - self.speed
        self.position = (x_pos, self.position[1])
        self.render()
        if self.life_span:
            if self.life_span + self.birthdate - (pygame.time.get_ticks() * 1e-3) < 0:
                self.kill()

    def render(self) -> None:
        self.image = pygame.surface.Surface((2.5 * self.radius, 1.7 * self.radius))
        self.image.fill("White")
        pygame.draw.ellipse(self.image, "Black", self.image.get_rect())
        self.rect = self.image.get_rect(center=self.position)
