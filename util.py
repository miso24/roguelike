from enum import IntEnum

class Direction(IntEnum):
    DOWN = 0
    RIGHT = 1
    UP = 2
    LEFT = 3

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, target):
        if not isinstance(target, Vector2):
            raise ValueError("Invalid type error")
        return Vector2(self.x + target.x, self.y + target.y)

    def __sub__(self, target):
        if not isinstance(target, Vector2):
            raise ValueError("Invalid type error")
        return Vector2(self.x - target.x, self.y - target.y)

    def __mul__(self, target):
        return Vector2(self.x * target, self.y * target)

class Transform:
    def __init__(self, position: Vector2, direction: Direction):
        self.position = position
        self.draw_position = Vector2(position.x * 8, position.y * 8)
        self.direction = direction

class DirectionVelocity(Vector2):
    def __init__(self, x, y):
        super().__init__(x, y)

    @classmethod
    def get(cls, direction):
        if direction == Direction.UP:
            x, y = 0, -1
        elif direction == Direction.LEFT:
            x, y = -1, 0
        elif direction == Direction.DOWN:
            x, y = 0, 1
        elif direction == Direction.RIGHT:
            x, y = 1, 0
        return cls(x, y)

