from dataclasses import dataclass
from pathlib import Path


@dataclass
class Settings:
    """
    Class containing the overall game settings for things the user can not change.
    """

    # Game Parameters
    name: str = "MidiPlayer"
    fps: int = 60
    config: Path = Path("src/midi_player/config.json")
    assets: Path = Path("src/midi_player/assets")

    # Appearance
    font: Path = assets / "font.ttf"
    default_text_color: str = "#ff962c"
    hovered_text_color: str = "#331f49"
