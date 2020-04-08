from terrain import Terrain


class Dungeon:
    def __init__(self, player):
        self.player = player
        self.terrain = Terrain()
        self.level = 1

    def generate(self):
        self.terrain.generate(self.level)

    def render(self):
        self.terrain.render(self.player.position.x, self.player.position.y)
