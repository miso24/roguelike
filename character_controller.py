from util import Direction, DirectionVelocity, Vector2
import copy


class CharacterController:
    def __init__(self, terrain_data, transform):
        self.terrain_data = terrain_data
        self.transform = transform

    def can_move(self, velocity):
        moved_position = self.transform.position + velocity
        return self.terrain_data.at(moved_position.x, moved_position.y) != 1

    def move(self, direction, on_move_hook):
        velocity = DirectionVelocity.get(direction)
        self.transform.direction = direction
    
        if self.can_move(velocity):
            self.transform.position.x += velocity.x
            self.transform.position.y += velocity.y
            on_move_hook()
