from util import Direction, Vector2
import copy


class CharacterController:
    def __init__(self, terrain_data, transform):
        self.terrain_data = terrain_data
        self.transform = transform

    def can_move(self, velocity):
        moved_position = self.transform.position + velocity
        return self.terrain_data.at(moved_position.x, moved_position.y) != 1

    def move(self, direction):
        velocity = Vector2(0, 0)
        if direction == Direction.UP:
            velocity.y = -1
        elif direction == Direction.LEFT:
            velocity.x = -1
        elif direction == Direction.DOWN:
            velocity.y = 1
        elif direction == Direction.RIGHT:
            velocity.x = 1
        self.transform.direction = direction
    
        if self.can_move(velocity):
            self.transform.position.x += velocity.x
            self.transform.position.y += velocity.y
