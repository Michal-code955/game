import random

import pygame
from setting import *


class Zombie(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.status = ""
        self.image = pygame.Surface((36, 64))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = random.randint(1,2)
        self.jump_speed = -16
        self.move = random.randint(1, 5)
        self.counter = 0



    def jump(self):
        if self.status != "jump" or self.status == "":
            self.status = "jump"
            self.direction.y = self.jump_speed

    def horizontal_movement_collision(self, tiles):
        self.counter += 1
        if self.counter == self.move:
            self.rect.x += self.speed
            self.counter = 0
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right
                elif self.direction.x > 0:
                    self.rect.right = tile.rect.left

    def vertical_movement_collision(self, tiles):
        self.apply_gravity()

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = tile.rect.top
                    self.direction.y = 0
                    self.status = ""
                if self.direction.y < 0:
                    self.rect.top = tile.rect.bottom
                    self.direction.y = 0

    def apply_gravity(self):
        self.direction.y += gravity
        self.rect.y += self.direction.y

    def update(self, tiles):
        self.horizontal_movement_collision(tiles)
        self.vertical_movement_collision(tiles)
