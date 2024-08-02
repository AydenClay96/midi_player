import enum


class EntityType(enum.Enum):
    EMPTY = 0
    TEXT = 1
    BUTTON = 2
    SELECTOR = 3
    NOTE = 4
    BACKGROUND = 5
    KEYBOARD = 6
