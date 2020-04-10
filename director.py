from __future__ import annotations
from typing import TYPE_CHECKING
import pyxel


if TYPE_CHECKING:
    from base_scene import BaseScene


class Director:
    def __init__(self) -> None:
        self.scene: BaseScene 

    def update(self) -> None:
        self.scene.update()

    def render(self) -> None:
        pyxel.cls(0)
        self.scene.render()
        pyxel.flip()

    def set_scene(self, scene: BaseScene) -> None:
        self.scene = scene
