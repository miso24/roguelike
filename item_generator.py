from __future__ import annotations
from typing import List, Tuple, ClassVar, TYPE_CHECKING
import json
import random

from item import Item
from util import Vector2


if TYPE_CHECKING:
    from terrain_data import TerrainData


class ItemDistribution:
    def __init__(self, weapon_ids: List[int], armor_ids: List[int], portion_ids: List[int]) -> None:
        self.weapon_ids = weapon_ids
        self.armor_ids = armor_ids 
        self.portion_ids = portion_ids

class ItemGenerator:
    item_types: ClassVar[List[str]] = [
        "weapon",
        "armor",
        "portion"
    ]

    def __init__(self, terrain_data: TerrainData) -> None:
        self.terrain_data = terrain_data
        self.distributions: List[ItemDistribution] = []
        self.load_distributions()

    def load_distributions(self) -> None:
        with open("data/item_distribution.json") as f:
            data = json.load(f)
            for floor in data["floors"]:
                self.distributions.append(
                    ItemDistribution(
                        floor["weapon"],
                        floor["armor"],
                        floor["portion"]
                    )
                )

    def choice_item(self, item_ids: List[int]) -> Item:
        return Item.create_by_id(random.choice(item_ids))

    def generate(self, level: int) -> List[Tuple[Vector2, Item]]:
        if level >= len(self.distributions): level = len(self.distributions)
        item_list: List[Tuple[Vector2, Item]] = []

        room_num = len(self.terrain_data.rooms)
        rooms = random.sample(self.terrain_data.rooms, int(room_num * 0.6))
        for room in rooms:
            item_num = random.randint(1, (room.width + room.height) // 10)
            for _ in range(item_num):
                item_type = random.choice(ItemGenerator.item_types)
                if item_type == "weapon":
                    item_ids = self.distributions[level].weapon_ids
                if item_type == "armor":
                    item_ids = self.distributions[level].armor_ids
                elif item_type == "portion":
                    item_ids = self.distributions[level].portion_ids
                item_x = random.randint(room.left, room.right) 
                item_y = random.randint(room.top, room.bottom) 
                item = self.choice_item(item_ids)
                item_list.append((Vector2(item_x, item_y), item))
        return item_list
