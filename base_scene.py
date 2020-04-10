from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from director import Director


class BaseScene(metaclass=ABCMeta):
    def __init__(self, director: Director) -> None:
        self.director = director

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass

    def change_scene(self, scene: BaseScene) -> None:
        self.director.set_scene(scene)


