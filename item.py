from __future__ import annotations
from typing import ClassVar, TYPE_CHECKING


if TYPE_CHECKING:
    from item_database import ItemDatabase


class Item:
    database: ClassVar[ItemDatabase]

    def __init__(self, item_type: str, name: str, value: int) -> None:
        self.item_type = item_type
        self.name = name
        self.value = value

    @classmethod
    def init(cls, database: ItemDatabase) -> None:
        print("initialize item")
        cls.database = database
