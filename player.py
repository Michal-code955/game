import pygame
from setting import gravity
from setting import tile_size


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Michal/Downloads/knight-removebg-preview-removebg-preview.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.jump_speed = -16
        self.move_up = False
        self.move_down = False
        self.status = ""
        self.lives = 5
        self.alive  = True

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1

        else:
            self.direction.x = 0



    def jump(self):
        if self.status != "jump" or self.status == "":
            self.status = "jump"
            self.direction.y = self.jump_speed

    def horizontal_movement_collision(self, tiles):
        self.rect.x += self.direction.x * self.speed
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile.rect.right
                elif self.direction.x > 0:
                    self.rect.right = tile.rect.left

    def vertical_movement_collision(self, tiles):
        # self.apply_gravity()

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = tile.rect.top
                    self.direction.y = 0
                    self.status = ""
                if self.direction.y < 0:
                    self.rect.top = tile.rect.bottom
                    self.direction.y = 0

    # def apply_gravity(self):
    #    self.direction.y += gravity
    #   self.rect.y += self.direction.y

    def update(self, tiles):
        self.get_input()
        self.horizontal_movement_collision(tiles)
        self.vertical_movement_collision(tiles)
