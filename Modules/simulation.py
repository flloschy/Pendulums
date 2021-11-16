import pygame, math

class Simulation:
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 1000
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
