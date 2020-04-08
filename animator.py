class AnimeNode:
    def __init__(self, u, v, frame):
        self.u = u
        self.v = v
        self.frame = frame

class Anime:
    def __init__(self, is_loop=False):
        self.anime_nodes = []
        self.total_frames = 0
        self.is_loop = is_loop

    def add_node(self, node):
        self.total_frames += node.frame
        self.anime_nodes.append(node)

    def get_node_by_frame(self, frame):
        if self.is_loop and frame > self.total_frames:
            frame = frame % self.total_frames
        frame_num = 0
        for node in self.anime_nodes:
            frame_num += node.frame
            if frame < frame_num:
                return node
        return self.anime_nodes[-1]

class Animator:
    def __init__(self, state, direction):
        self.frame_count = 0
        self.state = state
        self.direction = direction
        self.anime_data = {}

    def add_anime(self, state, anime):
        self.anime_data[state] = anime

    def update(self):
        self.frame_count += 1

    def get_uv(self):
        print(self.direction)
        anime_node = self.anime_data[self.state].get_node_by_frame(self.frame_count)
        u = anime_node.u
        v = anime_node.v + int(self.direction) * 8
        return u,v

    def on_state_changed(self):
        self.frame_count = 0

    def on_changed_direction(self, direction):
        self.direction = direction
