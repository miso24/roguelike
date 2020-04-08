class TerrainData:
    def __init__(self, width, height, start_x, start_y, rooms, data):
        self.width = width
        self.height = height
        self.start_x = start_x
        self.start_y = start_y
        self.rooms = rooms
        self.data = data

    def at(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return 1
        else:
            return self.data[y][x]
