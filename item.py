from __future__ import annotations
from typing import ClassVar, TYPE_CHECKING


if TYPE_CHECKING:
    from item_database import ItemDatabase


class Item:
    database: ClassVar[ItemDatabase]

    def __init__(self, item_type: str, name: str, description: str, value: int) -> None:
        self.item_type = item_type
        self.description = description
        self.name = name
        self.value = value

    @classmethod
    def init(cls, database: ItemDatabase) -> None:
        print("initialize item")
        cls.database = database

    @classmethod
    def create_by_id(cls, item_id: int) -> Item:
        return cls(*cls.database.get_by_id(item_id).get_data())

    @classmethod
    def create_by_name(cls, item_name: str) -> Item:
        return cls(*cls.database.get_by_name(item_name).get_data())
