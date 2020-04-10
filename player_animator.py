from __future__ import annotations
from typing import TYPE_CHECKING

from animator import Animator, Anime, AnimeNode


if TYPE_CHECKING:
    from util import Direction


class PlayerAnimator(Animator):
    def __init__(self, state: str, direction: Direction) -> None:
        super().__init__(state, direction)
        
        idle_anime = Anime(is_loop=False)
        idle_anime.add_node(AnimeNode(0, 0, 1))

        walk_anime = Anime(is_loop=False)
        walk_anime.add_node(AnimeNode(0, 0, 2))
        walk_anime.add_node(AnimeNode(8, 0, 2))
        walk_anime.add_node(AnimeNode(16, 0, 2))
        walk_anime.add_node(AnimeNode(24, 0, 2))

        self.add_anime("idle", idle_anime)
        self.add_anime("walking", walk_anime)
