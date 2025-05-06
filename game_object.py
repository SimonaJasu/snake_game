from abc import ABC, abstractmethod

class GameObject(ABC):
    @abstractmethod
    def draw(self, surface):
        pass