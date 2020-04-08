from util import Vector2, Transform, Direction
from character_controller import CharacterController
import pyxel


class Player:
    def __init__(self, terrain_data):
        position = Vector2(terrain_data.start_x, terrain_data.start_y)
        self.transform = Transform(position, Direction.DOWN)
        self.position = Vector2(terrain_data.start_x, terrain_data.start_y)
        self.terrain_data = terrain_data
        self.char_ctrl = CharacterController(terrain_data, self.transform)

    def render(self):
        pyxel.blt(pyxel.width // 2 - 4, pyxel.height // 2 - 4, 0, 0, int(self.transform.direction) * 8, 8, 8, 7)
