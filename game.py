import pyxel
import director
from title_scene import TitleScene
import game_scene


class Game:
    def __init__(self) -> None:
        pyxel.init(120, 120, caption="Rogue like", fps=60)
        pyxel.image(0).load(0, 0, "resource/character.png")
        pyxel.image(1).load(0, 0, "resource/mapchip.png")
        self.director = director.Director()
        #self.director.set_scene(game_scene.GameScene(self.director))
        self.director.set_scene(TitleScene(self.director))

    def run(self) -> None:
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        self.director.update()

    def draw(self) -> None:
        self.director.render()

game = Game()
game.run()
