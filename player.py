from util import Vector2, Transform, Direction
from character_controller import CharacterController
from transitions import Machine
from player_animator import PlayerAnimator
import pyxel


class Player:
    states = ['idle']

    def __init__(self, terrain_data):
        self.machine = Machine(model=self, states=Player.states, initial='idle')

        position = Vector2(terrain_data.start_x, terrain_data.start_y)
        self.transform = Transform(position, Direction.DOWN)
        self.terrain_data = terrain_data
        self.char_ctrl = CharacterController(terrain_data, self.transform)
        self.animator = PlayerAnimator(self.state, self.transform.direction)

    def update(self):
        self.animator.update()
        pass

    def move(self, direction):
        if self.transform.direction != direction:
            self.animator.on_changed_direction(direction)
        self.char_ctrl.move(direction)

    def render(self):
        #pyxel.blt(pyxel.width // 2 - 4, pyxel.height // 2 - 4, 0, self.anime_counter * 8, int(self.transform.direction) * 8, 8, 8, 7)
        dx = pyxel.width // 2 - 4
        dy = pyxel.height // 2 - 4
        pyxel.blt(dx, dy, 0, *self.animator.get_uv(), 8, 8, 7)
