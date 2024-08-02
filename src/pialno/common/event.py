import enum
from typing import Union

import pygame
from pygame.event import Event
from pygame.event import EventType as PygameEventType


class EventType(enum.Enum):
    CHANGE_SCENE = pygame.event.custom_type()
    OPTION_CHANGE = pygame.event.custom_type()
    MIDI_INPUT = pygame.event.custom_type()


class GameEvent:
    """
    GameEvent class provides methods associated with both Pygame and Custom events.
    """

    def __init__(self, init_arg: Union[Event, EventType, int], **kwargs):
        if isinstance(init_arg, PygameEventType):
            self.event = init_arg
        elif isinstance(init_arg, EventType):
            self.event = Event(init_arg.value, **kwargs)
        elif isinstance(init_arg, int):
            self.event = Event(init_arg, **kwargs)

    @staticmethod
    def __get_event_type(e: Union[EventType, int]):
        return e.value if isinstance(e, EventType) else e

    def post(self):
        pygame.event.post(self.event)

    def is_key_down(self, *keys: int):
        return self.event.type == pygame.KEYDOWN and self.event.key in keys

    def is_key_up(self, *keys: int):
        return self.event.type == pygame.KEYUP and self.event.key in keys

    def is_type(self, event_type: Union[EventType, int]):
        return self.event.type == self.__get_event_type(event_type)
