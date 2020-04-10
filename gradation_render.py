from typing import ClassVar, List
import pyxel
import enum


class GradationPattern(enum.IntEnum):
    SHALLOW = 0
    MEDIUM = 1
    DEEP = 2


class GradationRender:
    patterns: ClassVar[List[List[int]]] = [
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0]
    ]

    def draw_gradation_pattern(self, x: int, y: int, pattern: GradationPattern) -> None:
        for i in range(4 * 4):
            if self.patterns[int(pattern)][i] == 1:
                pyxel.pset(x + i % 4, y + i // 4, 0)

    def draw_gradation_vertical(self, x: int, y: int, length: int, pattern: GradationPattern) -> None:
        for i in range(length):
            self.draw_gradation_pattern(x, y + i * 4, pattern)

    def draw_gradation_horizontal(self, x: int, y: int, length: int, pattern: GradationPattern) -> None:
        for i in range(length):
            self.draw_gradation_pattern(x + i * 4, y, pattern)

    def render(self, darkness: int) -> None:
        for i in range(darkness):
            if i < darkness * 0.5:
                pattern = GradationPattern.DEEP
            elif i < darkness * 0.75:
                pattern = GradationPattern.MEDIUM
            else:
                pattern = GradationPattern.SHALLOW
            self.draw_gradation_horizontal(
                i * 4, i * 4, pyxel.width // 4 - i * 2, pattern)
            self.draw_gradation_horizontal(
                i * 4, pyxel.height - i * 4 - 4, pyxel.width // 4 - i * 2, pattern)
            self.draw_gradation_vertical(
                i * 4, i * 4 + 4, pyxel.height // 4 - i * 2 - 2, pattern)
            self.draw_gradation_vertical(
                pyxel.width - 4 - i * 4, i * 4 + 4, pyxel.height // 4 - i * 2 - 2, pattern)
