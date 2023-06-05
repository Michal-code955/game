import pygame
from setting import *


class Plant(pygame.sprite.Sprite):

    def __init__(self, surface, pos):
        super().__init__()
        self.status = ""
        self.image = pygame.image.load("C:/Users/Michal/Downloads/plant-removebg-preview.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_speed = -16
        self.display_surface = surface

    def draw(self):
        pass




