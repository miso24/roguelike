from abc import ABCMeta, abstractmethod


class BaseScene(metaclass=ABCMeta):
    def __init__(self, director):
        self.director = director

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    def change_scene(self, scene):
        self.director.set_scene(scene)


