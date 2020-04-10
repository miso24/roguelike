from typing import Tuple, List
import random

from terrain_data import TerrainData


class Rect:
    def __init__(self, left: int, top: int, width: int, height: int) -> None:
        self.left = left
        self.top = top
        self.right = left + width
        self.bottom = top + height
        self.width = width
        self.height = height

    def __setattr__(self, name: str, value) -> None:
        if name == "width":
            self.right = self.left + value
        elif name == "height":
            self.bottom = self.top + value
        object.__setattr__(self, name, value)


class Region(Rect):
    def __init__(self, left: int, top: int, width: int, height: int) -> None:
        super().__init__(left, top, width, height)
        self.room: Rect


class RegionPair:
    def __init__(self, direction: str, parent: Region, child: Region) -> None:
        self.direction = direction
        self.parent = parent
        self.child = child


class RegionGenerator:
    def __init__(self, margin_min: int) -> None:
        self.margin_min = margin_min

    def generate(self, width: int, height: int) -> Tuple[List[Region], List[RegionPair]]:
        self.regions: List[Region] = []
        self.region_pairs: List[RegionPair] = []
        self.__split_regions(Region(0, 0, width, height))
        return self.regions, self.region_pairs

    def __split_regions(self, region: Region, split_count: int = 2, before_direction: int = None) -> None:
        if split_count == 0 or region.width < self.margin_min * 2 or region.height < self.margin_min * 2:
            self.regions.append(region)
            return

        if before_direction is None:
            direction = random.randint(0, 1)
        else:
            direction = 0 if before_direction == 1 else 1

        if direction == 0:
            top = random.randint(
                region.top + self.margin_min, region.bottom - self.margin_min)
            new_region = Region(
                region.left, top, region.width, region.bottom - top)
            region.height = top - region.top
            #self.__add_region_pair("Vertical", region, new_region)
            self.region_pairs.append(RegionPair("Vertical", region, new_region))
        elif direction == 1:
            left = random.randint(
                region.left + self.margin_min, region.right - self.margin_min)
            new_region = Region(
                left, region.top, region.right - left, region.height)
            region.width = left - region.left
            self.region_pairs.append(RegionPair("Horizontal", region, new_region))
            #self.__add_region_pair("Horizontal", region, new_region)
        self.__split_regions(
            region, split_count=split_count-1, before_direction=direction)
        self.__split_regions(new_region)

class RegionConnecter:
    def __is_exist_pair(self, region_pairs: List[RegionPair], parent: Region, child: Region) -> bool:
        for pair in region_pairs:
            if pair.parent == parent and pair.child == child:
                return True
        return False

    def connect_regions(self, regions: List[Region], region_pairs: List[RegionPair]) -> None:
        region_num = len(regions)
        trial_num = 1000
        add_road_num = int(region_num * 0.2 + 1)
        for __ in range(add_road_num):
            for _ in range(trial_num):
                parent, child = random.sample(regions, k=2)
                if self.__is_exist_pair(region_pairs, parent, child):
                    continue
                if parent.right == child.left and (parent.top == child.top or parent.bottom == child.bottom):
                    region_pairs.append(RegionPair("Horizontal", parent, child))
                    break
                elif parent.bottom == child.top and (parent.left == child.left or parent.right == child.left):
                    region_pairs.append(RegionPair("Vertical", parent, child))
                    break


class RoomGenerator:
    def __init__(self, margin_min: int) -> None:
        self.margin_min = margin_min
        
    def generate(self, regions: List[Region]) -> None:
        for region in regions:
            width = random.randint(self.margin_min,
                                   region.width - self.margin_min)
            height = random.randint(
                self.margin_min, region.height - self.margin_min)
            left = region.left + self.margin_min // 2 \
                + random.randint(0, region.width - width -
                                 self.margin_min)
            top = region.top + self.margin_min // 2 \
                + random.randint(0, region.height - height -
                                 self.margin_min)
            region.room = Rect(left, top, width, height)

class RoadGenerator:
    def add_vertical_road(self, roads: List[Rect], parent: Region, child: Region) -> None:
        parent_room_x = random.randint(
            parent.room.left + 1, parent.room.right - 1)
        parent_room_y = parent.room.bottom
        child_room_x = random.randint(
            child.room.left + 1, child.room.right - 1)
        child_room_y = child.room.top
        cross_x = min(parent_room_x, child_room_x)
        cross_width = max(parent_room_x, child_room_x) - cross_x
        roads.append(
            Rect(cross_x, parent.bottom, cross_width, 1))
        roads.append(
            Rect(parent_room_x, parent_room_y, 1, parent.bottom - parent_room_y + 1))
        roads.append(
            Rect(child_room_x, parent.bottom, 1, child_room_y - child.top))

    def add_horizontal_road(self, roads: List[Rect], parent: Region, child: Region) -> None:
        parent_right = parent.right
        parent_room_x = parent.room.right
        parent_room_y = random.randint(
            parent.room.top + 1, parent.room.bottom - 1)
        child_room_x = child.room.left
        child_room_y = random.randint(
            child.room.top + 1, child.room.bottom - 1)
        cross_y = min(parent_room_y, child_room_y)
        cross_height = max(parent_room_y, child_room_y) - cross_y
        roads.append(Rect(parent_right, cross_y, 1, cross_height))
        roads.append(
            Rect(parent_room_x, parent_room_y, parent_right - parent_room_x + 1, 1))
        roads.append(
            Rect(parent_right, child_room_y, child_room_x - parent_right, 1))

    def generate(self, region_pairs: List[RegionPair]) -> List[Rect]:
        roads: List[Rect] = []
        for pair in region_pairs:
            parent, child = pair.parent, pair.child
            if pair.direction == "Vertical":
                self.add_vertical_road(roads, parent, child)
            elif pair.direction == "Horizontal":
                self.add_horizontal_road(roads, parent, child)
        return roads


class TerrainGenerator:
    def generate(self, width: int, height: int) -> TerrainData:
        region_margin_min = int(width * 0.2)
        room_margin_min = region_margin_min // 2
        region_generator = RegionGenerator(region_margin_min)
        region_connecter = RegionConnecter()
        room_generator = RoomGenerator(room_margin_min)
        road_generator = RoadGenerator()

        regions, region_pairs = region_generator.generate(width, height)
        region_connecter.connect_regions(regions, region_pairs)
        room_generator.generate(regions)
        roads = road_generator.generate(region_pairs)
        return self.__generate_data(width, height, regions, roads)

    def __generate_data(self, width: int, height: int, regions: List[Region], roads: List[Rect]) -> TerrainData:
        data: List[List[int]] = [[1 for x in range(width)] for y in range(height)]
        rooms: List[Rect] = []
        for region in regions:
            room = region.room
            for y in range(room.top, room.bottom):
                data[y][room.left:room.right] = [0] * room.width
            rooms.append(room)

        for road in roads:
            if road.width == 1:
                for y in range(road.top, road.bottom):
                    data[y][road.left] = 0
            elif road.height == 1:
                data[road.top][road.left:road.right] = [0] * road.width

        stairs_room ,start_room = map(lambda region: region.room, random.sample(regions, k=2))
        stairs_x = random.randint(stairs_room.left, stairs_room.right - 1) 
        stairs_y = random.randint(stairs_room.top, stairs_room.bottom - 1) 
        data[stairs_y][stairs_x] = 2

        start_x = random.randint(start_room.left, start_room.right - 1)
        start_y = random.randint(start_room.top, start_room.bottom - 1)

        return TerrainData(width, height, start_x, start_y, rooms, data)
