import pyxel


class Director:
    def __init__(self):
        self.scene = None

    def update(self):
        self.scene.update()

    def render(self):
        pyxel.cls(0)
        self.scene.render()
        pyxel.flip()

    def set_scene(self, scene):
        self.scene = scene
