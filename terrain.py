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


"""
pyxel.init(128, 128, fps=10)
pyxel.image(1).load(0, 0, "./resource/mapchip.png")
terrain = Terrain()
terrain.generate(1)
cx, cy = terrain.terrain_data.width // 2, terrain.terrain_data.height // 2
while not pyxel.btn(pyxel.KEY_Q):
    terrain.render(cx, cy)
    if pyxel.btnp(pyxel.KEY_N):
        terrain.generate(1)
        cx, cy = terrain.terrain_data.width // 2, terrain.terrain_data.height // 2
    if pyxel.btn(pyxel.KEY_A):
        cx -= 1
    elif pyxel.btn(pyxel.KEY_W):
        cy -= 1
    elif pyxel.btn(pyxel.KEY_D):
        cx += 1
    elif pyxel.btn(pyxel.KEY_S):
        cy += 1
    pyxel.flip()
"""
