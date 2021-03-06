from __future__ import annotations
from typing import TYPE_CHECKING
import pyxel

from terrain_generator import TerrainGenerator
from terrain_render import TerrainRender


if TYPE_CHECKING:
    from terrain_data import TerrainData
    from util import Vector2


class Terrain:
    def __init__(self) -> None:
        self.terrain_generator = TerrainGenerator()
        self.terrain_render = TerrainRender()
        self.terrain_data: TerrainData

    def generate(self, level: int) -> None:
        dungeon_size = (40 + (level - 1) * 5,) * 2
        self.terrain_data = self.terrain_generator.generate(*dungeon_size)
        self.terrain_render.set_terrain_data(self.terrain_data)

    def draw_ascii_terrain(self) -> None:
        for y in range(self.terrain_data.height):
            for x in range(self.terrain_data.width):
                if self.terrain_data.at(x, y) == 0:
                    print("  ", end="")
                elif self.terrain_data.at(x, y) == 1:
                    print("██", end="")
                elif self.terrain_data.at(x, y) == 2:
                    print("|=", end="")
            print()

    def render(self, vector: Vector2) -> None:
        self.terrain_render.render(vector)

    @property
    def data(self) -> TerrainData:
        return self.terrain_data
