import pygame
from entities.text_entity import TextEntity
from common.event import GameEvent

class ButtonEntity(TextEntity):
    def __init__(self, event: GameEvent, *args, **kwargs) -> None:
        super.__init__(self, *args, **kwargs)
        self.event = event
        self.selected = False

    def update(self) -> None:
        if self.selected:
            self.event.post()

    def select(self) -> None:
        self.selected = not self.selected
    
    def check_hover(self) -> None:
        if pygame.mouse.get_visible():
            pos = pygame.mouse.get_pos()
            in_vert = pos[0] in range(self.rect.left, self.rect.right)
            in_horz = pos[1] in range(self.rect.top, self.rect.bottom)

            self.selected = in_vert and in_horz


