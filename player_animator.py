from animator import Animator, Anime, AnimeNode


class PlayerAnimator(Animator):
    def __init__(self, state, direction):
        super().__init__(state, direction)
        
        idle_anime = Anime(is_loop=False)
        idle_anime.add_node(AnimeNode(0, 0, 1))

        walk_anime = Anime(is_loop=False)
        walk_anime.add_node(AnimeNode(0, 0, 1))
        walk_anime.add_node(AnimeNode(8, 0, 1))
        walk_anime.add_node(AnimeNode(16, 0, 1))
        walk_anime.add_node(AnimeNode(24, 0, 1))

        self.add_anime("idle", idle_anime)
        self.add_anime("walking", walk_anime)
