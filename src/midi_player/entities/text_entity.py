from entities.base_entity import BaseEntity
from common.types import EntityType
from settings import Settings
from common.utils import Resources

class TextEntity(BaseEntity):
    """Basic Text entity."""

    def __init__(self,
                 text: str,
                 size: int,
                 color: str,
                 *args,
                 **kwargs) -> None:
        super().__init__(entity_type=EntityType.TEXT, *args, **kwargs)
        self.text = text
        self.color = color
        self.size = size

        self.font = Resources.get_font(self.size)

        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.position)

    def update(self) -> None:
        pass
