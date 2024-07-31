import pygame
from pygame.surface import Surface
from pygame.font import Font
import json
from typing import Dict, Optional, Union, Tuple
from settings import Settings


class Config:
    """Config class that contains functions related to the settings."""

    def __init__(self) -> None:
        self.data = self.load()

    def load(self) -> Dict:
        """Loads the config file."""
        with open(Settings.config, "r") as f:
            data = json.load(f)
        return data

    def save(self) -> None:
        """Loads the config file."""
        with open(Settings.config, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False)


class Resources:
    @staticmethod
    def get_font(font_size: int, font_type: Optional[str] = None) -> Font:
        """Loads the font."""
        if font_type:
            if font_type == "lfont":
                font = Settings.lfont
            elif font_type == "bfont":
                font = Settings.bfont
            else:
                font = Settings.font
        else:
            font = Settings.font
        return Font(font, font_size)

    @staticmethod
    def scale_image(
        image: Surface, scale: Optional[Union[float, Tuple[int, int]]] = None
    ) -> Surface:
        """Scales an image or just returns it directly."""
        if scale is None or scale == 1.0:
            return image
        if isinstance(scale, (int, float)):
            return pygame.transform.scale(
                image,
                (int(image.get_width() * scale), int(image.get_height() * scale)),
            )
        else:
            return pygame.transform.scale(
                image,
                scale,
            )

    @staticmethod
    def get_image(path: str, size: Optional[Tuple[int, int]] = None) -> Surface:
        """Gets an image and displays it at the required size."""
        image_path = Settings.assets / path
        image = pygame.image.load(image_path).convert()
        return Resources.scale_image(image, size)
