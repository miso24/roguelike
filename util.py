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

class Transform:
    def __init__(self, position: Vector2, direction: Direction):
        self.position = position
        self.direction = direction
