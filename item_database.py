from typing import List, Tuple, Callable
import json


class ItemData:
    def __init__(self, item_id: int, item_type: str, name: str, value: int) -> None:
        self.item_id = item_id
        self.item_type = item_type
        self.name = name
        self.value = value

    def get_data(self) -> Tuple[str, str, int]:
        return self.item_type, self.name, self.value


class ItemDatabase:
    def __init__(self) -> None:
        self.item_data: List[ItemData] = []
        self.load_item_data()

    def load_item_data(self) -> None:
        with open("data/item_data.json") as f:
            data = json.load(f)
            for d in data:
                self.item_data.append(
                    ItemData(
                        d["id"],
                        d["type"],
                        d["name"],
                        d["value"]
                    )
                )

    def search(self, func: Callable[[ItemData], bool]) -> ItemData:
        for item in self.item_data:
            if func(item):
                return item
        raise ValueError("Item cannot found")

    def get_by_id(self, item_id: int) -> ItemData:
        return self.search(lambda item: item.item_id == item_id)

    def get_by_name(self, name: str) -> ItemData:
        return self.search(lambda item: item.name == name)
