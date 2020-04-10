from __future__ import annotations
from typing import TYPE_CHECKING
import pyxel

from base_scene import BaseScene
from game_scene import GameScene


if TYPE_CHECKING:
    from director import Director


class TitleScene(BaseScene):
    def __init__(self, director: Director) -> None:
        super().__init__(director)

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.change_scene(GameScene(self.director))

    def draw_center_text(self, y: int, text: str, col: int) -> None:
        length = len(text) * 3 - len(text)
        x = pyxel.width // 2 - length
        pyxel.text(x, y, text, col)

    def render(self) -> None:
        self.draw_center_text(32, "Rogue like", 7)
        self.draw_center_text(90, "PUSH SPACE BUTTON", 7)
