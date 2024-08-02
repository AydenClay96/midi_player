import pygame
from pygame.event import Event
from entities.base_entity import BaseEntity
from typing import Sequence, Tuple, List, Optional
from common.event import GameEvent, EventType


def sort_fun(n):
    return n[1]


class KeyboardEntity(BaseEntity):
    """Keyboard entity."""

    def __init__(self, size: Tuple[int, int], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.size = size

        self.image = pygame.surface.Surface(self.size)
        self.rect = self.image.get_rect(center=self.position)
        self.height = self.rect.bottom - self.rect.top
        self.length = self.rect.right - self.rect.left

        self.key_number = {"white": 52, "black": 36}
        self.dimensions = {
            "white_key_width": self.length / self.key_number["white"],
            "black_key_width": self.length / (1.5 * self.key_number["white"]),
            "keyboard_length": self.length,
            "key_height": self.height,
            "key_height_offset": self.height,
        }

        self.white = []
        self.black = []
        self.white_rects = []
        self.black_rects = []

    def update(self, events: Sequence[GameEvent]) -> None:

        for e in events:
            if e.is_type(pygame.MOUSEBUTTONDOWN):
                self.on_click()
            elif e.is_type(pygame.MOUSEBUTTONUP):
                self.white = []
                self.black = []
            elif e.is_type(EventType.MIDI_INPUT):
                self.on_midi(e)
            if e.is_type(pygame.TEXTINPUT):
                self.on_type(e)
            elif e.is_type(pygame.KEYUP):
                self.white = []
                self.black = []

        self.image = pygame.surface.Surface(self.size)
        self.image.fill("White")
        self.rect = self.image.get_rect(center=self.position)
        self.draw_keyboard()

    def on_click(self) -> None:
        mouse_position = pygame.mouse.get_pos()
        position = (mouse_position[0], mouse_position[1] - self.position[1])
        black = False
        for i in range(len(self.black_rects)):
            if self.black_rects[i].collidepoint(position):
                black = True
                self.black.append(i)
                print(self.black)        
        for i in range(len(self.white_rects)):
            if self.white_rects[i].collidepoint(position) and not black:
                self.white.append(i)
                print(self.white)

    def on_midi(self, e: GameEvent) -> None:
        for key in self.keys:
            if key[0] == e.event.midi:
                print(key)
                if key[1][0] == "w":
                    self.white.append(key[1][1])
                if key[1][0] == "b":
                    self.black.append(key[1][1])

    def on_type(self, e: GameEvent) -> None:
        midi = 21 + int(e.event.text)
        midi_input = GameEvent(
            init_arg=EventType.MIDI_INPUT,
            midi=midi,
        )
        midi_input.post()

    def draw_keyboard(self) -> None:
        self.white_rects = []
        self.white_index = []
        for i in range(self.key_number["white"]):  # Draw white keys.
            rect = pygame.draw.rect(
                self.image,
                "white",
                [
                    i * self.dimensions["white_key_width"],
                    self.dimensions["key_height"]
                    - self.dimensions["key_height_offset"],
                    self.dimensions["white_key_width"],
                    self.dimensions["key_height_offset"],
                ],
                0,
                2,
            )
            self.white_rects.append(rect)
            self.white_index.append(["w", i])
            pygame.draw.rect(
                self.image,
                "black",
                [
                    i * self.dimensions["white_key_width"],
                    self.dimensions["key_height"]
                    - self.dimensions["key_height_offset"],
                    self.dimensions["white_key_width"],
                    self.dimensions["key_height_offset"],
                ],
                1,
                2,
            )
        skip_count = 0
        last_skip = 2
        skip_track = 2
        self.black_rects = []
        self.black_index = []
        for i in range(self.key_number["black"]):  # Draw black keys.
            rect = pygame.draw.rect(
                self.image,
                "black",
                [
                    self.dimensions["black_key_width"]
                    + ((skip_count + i) * self.dimensions["white_key_width"]),
                    self.dimensions["key_height"]
                    - self.dimensions["key_height_offset"],
                    self.dimensions["black_key_width"],
                    2 * self.dimensions["key_height_offset"] / 3,
                ],
                0,
                2,
            )
            for q in range(len(self.black)):
                if self.black[q] == i:
                    pygame.draw.rect(
                        self.image,
                        "green",
                        [
                            self.dimensions["black_key_width"]
                            + (
                                (skip_count + i)
                                * self.dimensions["white_key_width"]
                            ),
                            self.dimensions["key_height"]
                            - self.dimensions["key_height_offset"],
                            self.dimensions["black_key_width"],
                            2 * self.dimensions["key_height_offset"] / 3,
                        ],
                        2,
                        2,
                    )
            self.black_rects.append(rect)
            self.black_index.append(["b", i])
            skip_track += 1
            if last_skip == 2 and skip_track == 3:
                last_skip = 3
                skip_track = 0
                skip_count += 1
            elif last_skip == 3 and skip_track == 2:
                last_skip = 2
                skip_track = 0
                skip_count += 1

        for i in range(len(self.white)):
            j = self.white[i]
            pygame.draw.rect(
                self.image,
                "green",
                [
                    j * self.dimensions["white_key_width"],
                    self.dimensions["key_height"]
                    - int(self.dimensions["key_height_offset"] / 3),
                    self.dimensions["white_key_width"],
                    int(self.dimensions["key_height_offset"] / 3),
                ],
                2,
                2,
            )
        black_index = [[x, y+0.001] for x, y in self.black_index]
        keys = sorted(black_index + self.white_index, key=sort_fun)
        new_keys = [[x, int(y)] for x,y in keys]
        self.keys = list(enumerate(new_keys, 21))
