class AnimeNode:
    def __init__(self, u, v, frame):
        self.u = u
        self.v = v
        self.frame = frame

class Anime:
    def __init__(self, is_loop=False):
        self.anime_nodes = []
        self.current_node = None
        self.total_frames = 0
        self.is_loop = is_loop
        self.is_end = False

    def init(self):
        self.is_end = False
        self.current_node = self.anime_nodes[0]

    def update(self, frame):
        if self.is_loop and frame > self.total_frames:
            frame = frame % self.total_frames

        frame_num = 0
        for node in self.anime_nodes:
            frame_num += node.frame
            if frame < frame_num:
                self.current_node = node
                return
        self.is_end = True
        self.current_node = self.anime_nodes[-1]

    def add_node(self, node):
        self.total_frames += node.frame
        self.anime_nodes.append(node)

    def get_current_node(self):
        return self.current_node

class Animator:
    def __init__(self, state, direction):
        self.frame_count = 0
        self.state = state
        self.direction = direction
        self.anime_data = {}

    def add_anime(self, state, anime):
        anime.init()
        self.anime_data[state] = anime

    def update(self):
        self.frame_count += 1
        self.anime_data[self.state].update(self.frame_count)

    def get_uv(self):
        anime_node = self.anime_data[self.state].get_current_node()
        u = anime_node.u
        v = anime_node.v + int(self.direction) * 8
        return u,v

    def on_state_changed(self, state):
        self.frame_count = 0
        self.state = state
        self.anime_data[state].is_end = False

    def on_changed_direction(self, direction):
        self.direction = direction

    @property
    def is_end(self):
        return self.anime_data[self.state].is_end

    @property
    def current_anime_frames(self):
        return self.anime_data[self.state].total_frames
