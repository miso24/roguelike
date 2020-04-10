from __future__ import annotations
from typing import List, TYPE_CHECKING 


if TYPE_CHECKING:
    from terrain_generator import Rect


class TerrainData:
    def __init__(self, width: int, height: int, start_x: int, start_y: int, rooms: List[Rect], data: List[List[int]]) -> None:
        self.width = width
        self.height = height
        self.start_x = start_x
        self.start_y = start_y
        self.rooms = rooms
        self.data = data

    def at(self, x, y) -> int:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return 1
        else:
            return self.data[y][x]
