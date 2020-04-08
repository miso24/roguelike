from base_scene import BaseScene
from terrain import Terrain
from player import Player
from util import Direction
from gradation_render import GradationRender
import pyxel


class GameScene(BaseScene):
    def __init__(self, director):
        super().__init__(director)
        self.level = 1
        self.terrain = Terrain()
        self.terrain.generate(self.level)
        self.player = Player(self.terrain.data)
        self.gradation_render = GradationRender()

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.char_ctrl.move(Direction.LEFT)
        elif pyxel.btn(pyxel.KEY_UP):
            self.player.char_ctrl.move(Direction.UP)
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.player.char_ctrl.move(Direction.RIGHT)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.player.char_ctrl.move(Direction.DOWN)

    def render(self):
        self.terrain.render(self.player.transform.position)
        self.player.render()
        self.gradation_render.render(8)
