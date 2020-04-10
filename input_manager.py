import pyxel


class MoveKeys:
    def __init__(self) -> None:
        self.init()

    def init(self) -> None:
        self.left_key = False
        self.right_key = False
        self.up_key = False
        self.down_key = False


class InputManager:
    def __init__(self) -> None:
        self.move_keys = MoveKeys()

    def update(self) -> None:
        self.move_keys.init()
        if pyxel.btn(pyxel.KEY_LEFT):
            self.move_keys.left_key = True
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.move_keys.right_key = True
        if pyxel.btn(pyxel.KEY_UP):
            self.move_keys.up_key = True
        if pyxel.btn(pyxel.KEY_DOWN):
            self.move_keys.down_key = True
