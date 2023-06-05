import pygame
from setting import *


class Tile(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()

        self.image = pygame.image.load("C:/Users/Michal/Downloads/wall.jpg")
        self.rect = self.image.get_rect(topleft=pos)

