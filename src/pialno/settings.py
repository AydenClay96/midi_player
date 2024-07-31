from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    """
    Class containing the overall game settings for things the user can not change.
    """

    # Game Parameters
    name: str = "PI-AL-NO"
    fps: int = 60
    config: Path = Path("src/pialno/config.json")
    assets: Path = Path("src/pialno/assets")

    # Appearance
    font: Path = assets / "font.ttf"
    bfont: Path = assets / "bfont.ttf"
    lfont: Path = assets / "lfont.ttf"
    default_text_color: str = "#ff962c"
    hovered_text_color: str = "#331f49"
