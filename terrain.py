from terrain_generator import TerrainGenerator
from terrain_render import TerrainRender
import pyxel


class Terrain:
    def __init__(self):
        self.terrain_generator = TerrainGenerator()
        self.terrain_render = TerrainRender()
        self.terrain_data = None

    def generate(self, level):
        dungeon_size = (40 + (level - 1) * 5,) * 2
        self.terrain_data = self.terrain_generator.generate(*dungeon_size)
        self.terrain_render.set_terrain_data(self.terrain_data)

    def draw_ascii_terrain(self):
        for y in range(self.terrain_data.height):
            for x in range(self.terrain_data.width):
                if self.terrain_data.at(x, y) == 0:
                    print("  ", end="")
                elif self.terrain_data.at(x, y) == 1:
                    print("██", end="")
                elif self.terrain_data.at(x, y) == 2:
                    print("|=", end="")
            print()

    def render(self, vector):
        self.terrain_render.render(vector.x, vector.y)

    @property
    def data(self):
        return self.terrain_data
