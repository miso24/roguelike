from animator import Animator, Anime, AnimeNode


class PlayerAnimator(Animator):
    def __init__(self, state, direction):
        super().__init__(state, direction)
        
        idle_anime = Anime(is_loop=False)
        idle_anime.add_node(AnimeNode(0, 0, 1))

        self.add_anime("idle", idle_anime)
