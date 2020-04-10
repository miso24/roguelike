from __future__ import annotations
from util import DirectionVelocity
from typing import Callable, TYPE_CHECKING
import copy


if TYPE_CHECKING:
    from terrain_data import TerrainData
    from util import Transform, Direction, Vector2


class CharacterController:
    def __init__(self, terrain_data: TerrainData, transform: Transform) -> None:
        self.terrain_data = terrain_data
        self.transform = transform

    def can_move(self, velocity: Vector2) -> bool:
        moved_position = self.transform.position + velocity
        return self.terrain_data.at(moved_position.x, moved_position.y) != 1

    def move(self, direction: Direction, on_move_hook: Callable) -> None:
        velocity = DirectionVelocity.get(direction)
        self.transform.direction = direction
    
        if self.can_move(velocity):
            self.transform.position.x += velocity.x
            self.transform.position.y += velocity.y
            on_move_hook()
