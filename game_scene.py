from __future__ import annotations
from typing import TYPE_CHECKING
import pyxel

from base_scene import BaseScene
from terrain import Terrain
from player import Player
from util import Direction
from gradation_render import GradationRender
from input_manager import InputManager


if TYPE_CHECKING:
    from director import Director


class GameScene(BaseScene):
    def __init__(self, director: Director) -> None:
        super().__init__(director)
        self.level = 1
        self.terrain = Terrain()
        self.terrain.generate(self.level)
        self.player = Player(self.terrain.data)
        self.input_manager = InputManager()
        self.gradation_render = GradationRender()

    def update(self) -> None:
        self.player.update()
        self.input_manager.update()
        if self.player.state == "idle":
            move_keys = self.input_manager.move_keys
            if move_keys.left_key:
                self.player.move(Direction.LEFT)
            elif move_keys.right_key:
                self.player.move(Direction.RIGHT)
            elif move_keys.up_key:
                self.player.move(Direction.UP)
            elif move_keys.down_key:
                self.player.move(Direction.DOWN)

    def render(self) -> None:
        self.terrain.render(self.player.transform.draw_position)
        self.player.render()
        self.gradation_render.render(8)
