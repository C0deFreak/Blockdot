import pygame
from Engine.setup import collision_map, window, nothing_color

class DynamicRectangle():
    def __init__(self, height=10, width=10, color='white', position=[0, 0]):
        self.height = height
        self.width = width
        self.color = color
        self.position = position
        self.object = pygame.Rect(0, 0, self.width, self.height)

        self.instantiate()

    def instantiate(self):
        try:
            self.object.center = (self.position[0], self.position[1])
            pygame.draw.rect(window, self.color, self.object)
            print("Dynamic object instantiated")
        except:
            print("Dynamic object could not be instantiated, one of the next variables is of a wrong type: width, height, color, position")

    def move(self, x=0, y=0):
        pygame.draw.rect(window, nothing_color, self.object)
        self.position = [self.position[0] + x, self.position[1] + y]

        self.object.center = self.position
        pygame.draw.rect(window, self.color, self.object)
        pygame.display.update()

         