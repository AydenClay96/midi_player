import pygame
import itertools
from typing import Tuple, Optional, Union
from common.types import EntityType
from common.utils import Resources
from pathlib import Path


class BaseEntity(pygame.sprite.Sprite):
    """
        Base class for all game entities.
    """
    gen_id = itertools.count()

    def __init__(self,
                 entity_type: EntityType,
                 position: Tuple[int, int],
                 sprite_path: Optional[Path] = None,
                 scale: Optional[Union[float, Tuple[int, int]]] = None,
                 life_span: Optional[int] = None,
                 ) -> None:
        self.entity_type = entity_type
        self.position = position
        if sprite_path:
            self.sprite = Resources.get_image(sprite_path, scale)
        if life_span:
            self.life_span = life_span
        pygame.sprite.Sprite.__init__(self)
