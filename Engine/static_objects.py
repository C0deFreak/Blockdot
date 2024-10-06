import pygame
from Engine.setup import collision_map, window

class Rectangle():
    def __init__(self, height=10, width=10, color='white', position = [0, 0], name=str(len(collision_map))):
        self.height = height
        self.width = width
        self.color = color
        self.position = position
        self.name = name

        self.instantiate()

    def instantiate(self):
        try:
            rect = pygame.Rect(0, 0, self.width, self.height)
            rect.center = (self.position[0], self.position[1])
            pygame.draw.rect(window, self.color, rect)
            print("Static object instantiated")
        except:
            print("Static object could not be instantiated, one of the next variables is of a wrong type: width, height, color, position")


    def add_to_collision_map(self):
        collider = {'x' : [self.position[0], self.width], 'y' : [self.position[1], self.height]}
        collision_map[f"{self.name}"] = collider
        return collider
    
