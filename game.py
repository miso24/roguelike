import pyxel
import director
import game_scene


class Game:
    def __init__(self):
        pyxel.init(120, 120)
        pyxel.image(0).load(0, 0, "resource/character.png")
        pyxel.image(1).load(0, 0, "resource/mapchip.png")
        self.director = director.Director()
        self.director.set_scene(game_scene.GameScene(self.director))

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        self.director.update()

    def draw(self):
        self.director.render()

game = Game()
game.run()
