from base_scene import BaseScene
from terrain import Terrain
from player import Player
from util import Direction
from gradation_render import GradationRender
from input_manager import InputManager
import pyxel


class GameScene(BaseScene):
    def __init__(self, director):
        super().__init__(director)
        self.level = 1
        self.terrain = Terrain()
        self.terrain.generate(self.level)
        self.player = Player(self.terrain.data)
        self.input_manager = InputManager()
        self.gradation_render = GradationRender()

    def update(self):
        self.player.update()
        self.input_manager.update()
        if self.player.state == "idle":
            if self.input_manager.move_keys.left_key:
                self.player.move(Direction.LEFT)
            elif self.input_manager.move_keys.right_key:
                self.player.move(Direction.RIGHT)
            elif self.input_manager.move_keys.up_key:
                self.player.move(Direction.UP)
            elif self.input_manager.move_keys.down_key:
                self.player.move(Direction.DOWN)

    def render(self):
        self.terrain.render(self.player.transform.draw_position)
        self.player.render()
        self.gradation_render.render(8)
