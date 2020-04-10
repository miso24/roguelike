from __future__ import annotations
from typing import TYPE_CHECKING
import pyxel

from util import Vector2, Transform, Direction, DirectionVelocity
from character_controller import CharacterController
from transitions import Machine
from player_animator import PlayerAnimator


if TYPE_CHECKING:
    from terrain_data import TerrainData


class Player:
    states = ['idle', 'walking']

    def __init__(self, terrain_data: TerrainData) -> None:
        self.machine = Machine(model=self, states=Player.states, initial='idle')
        self.machine.add_transition(trigger='walk', source='idle', dest='walking', after='on_start_walk')
        self.machine.add_transition(trigger='stop', source='walking', dest='idle', after='on_stop')

        position = Vector2(terrain_data.start_x, terrain_data.start_y)
        self.transform = Transform(position, Direction.DOWN)
        self.terrain_data = terrain_data
        self.char_ctrl = CharacterController(terrain_data, self.transform)
        self.animator = PlayerAnimator(self.state, self.transform.direction)

    def update(self) -> None:
        self.animator.update()
        if self.state == "walking":
            self.transform.draw_position += DirectionVelocity.get(self.transform.direction) * (8 // self.animator.current_anime_frames)
            if self.animator.is_end: self.stop()

    def move(self, direction: Direction) -> None:
        if self.transform.direction != direction:
            self.animator.on_changed_direction(direction)
        self.char_ctrl.move(direction, self.walk)

    def on_start_walk(self) -> None:
        self.animator.on_state_changed("walking")

    def on_stop(self) -> None:
        self.animator.on_state_changed("idle")

    def render(self) -> None:
        dx = pyxel.width // 2 - 4
        dy = pyxel.height // 2 - 4
        pyxel.blt(dx, dy, 0, *self.animator.get_uv(), 8, 8, 7)
