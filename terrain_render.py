import pyxel
import json

class TileDataGenerator:
    def generate(self, terrain_data):
        tile_data = [[{} for y in range(terrain_data.height)] for x in range(terrain_data.width)]
        for y in range(terrain_data.height):
            for x in range(terrain_data.width):
                value = terrain_data.at(x, y)
                data_ref = tile_data[y][x]
                data_ref["value"] = value

                if value != 1: continue

                data_ref["top"] = 1 if terrain_data.at(x, y - 1) != 1 else 0
                data_ref["left"] = 2 if terrain_data.at(x - 1, y) != 1 else 0
                data_ref["bottom"] = 4 if terrain_data.at(x, y + 1) != 1 else 0
                data_ref["right"] = 8 if terrain_data.at(x + 1, y) != 1 else 0
                data_ref["upper_left"] = terrain_data.at(x - 1, y - 1)
                data_ref["upper_right"] = terrain_data.at(x + 1, y - 1)
                data_ref["lower_left"] = terrain_data.at(x - 1, y + 1)
                data_ref["lower_right"] = terrain_data.at(x + 1, y + 1)
        return tile_data


class TerrainRender:
    def __init__(self):
        self.__terrain_data = None
        with open("data/mapchipdata.json") as f:
            self.mapchipdata = json.load(f)

    def set_terrain_data(self, terrain_data):
        self.__terrain_data = terrain_data
        tile_data_generator = TileDataGenerator()
        self.tile_data = tile_data_generator.generate(terrain_data)

    def __get_mapchip_uv(self, chip):
        return chip["u"], chip["v"]

    def render(self, center_position):
        map_left = center_position.x // 8 - pyxel.width // 16
        map_top = center_position.y // 8 - pyxel.height // 16
        for my in range(self.__terrain_data.height + 2):
            for mx in range(self.__terrain_data.width + 2):
                dx, dy = (mx - 1) * 8, (my - 1) * 8
                dx += 8 - center_position.x % 8 - 8
                dy += 8 - center_position.y % 8 -8

                if map_left + mx < 0 or map_left + mx >= self.__terrain_data.width or map_top + my < 0 or map_top+ my >= self.__terrain_data.height:
                    chip = self.mapchipdata["wall"]["data"][0]
                    pyxel.blt(dx, dy, 1, *self.__get_mapchip_uv(chip), 8, 8)
                    continue

                x, y = map_left + mx - 1, map_top + my - 1
                data = self.tile_data[y][x]
                value = data["value"]
                if value == 0:
                    chip = self.mapchipdata["floor"]
                elif value == 2:
                    chip = self.mapchipdata["strairs"]
                elif value == 1:
                    chip = self.mapchipdata["wall"]["data"][data["top"] + data["left"] + data["bottom"] + data["right"]]
                    pyxel.blt(dx, dy, 1, *self.__get_mapchip_uv(self.mapchipdata["floor"]), 8, 8, 0)

                pyxel.blt(dx, dy, 1, *self.__get_mapchip_uv(chip), 8, 8, 0)
                if value != 1:
                    continue
                if data["top"] == data["left"] == 0 and data["upper_left"] == 0:
                    chip = self.mapchipdata["wall"]["corners"]["upper_left"]
                    pyxel.blt(dx, dy, 1, *self.__get_mapchip_uv(chip), 4, 4, 0)
                if data["top"] == data["right"] == 0 and data["upper_right"] == 0:
                    chip = self.mapchipdata["wall"]["corners"]["upper_right"]
                    pyxel.blt(dx + 4, dy, 1, *self.__get_mapchip_uv(chip), 4, 4, 0)
                if data["bottom"] == data["left"] == 0 and data["lower_left"] == 0:
                    chip = self.mapchipdata["wall"]["corners"]["lower_left"]
                    pyxel.blt(dx, dy + 4, 1, *self.__get_mapchip_uv(chip), 4, 4, 0)
                if data["bottom"] == data["right"] == 0 and data["lower_right"] == 0:
                    chip = self.mapchipdata["wall"]["corners"]["lower_right"]
                    pyxel.blt(dx + 4, dy + 4, 1, *self.__get_mapchip_uv(chip), 4, 4, 0)
