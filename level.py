import pygame.font
import pygame
from setting import *
from tile import Tile
from player import Player
from zombie import Zombie
from heart import Heart
from plant import Plant


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.zombie = pygame.sprite.Group()
        self.setup_level(level_data)
        self.hearts = Heart(surface)
        self.plants = pygame.sprite.Group()
        self.counter = 0
        self.points = 0
        self.second_counter = 0
        self.score = 0
        self.suns = 0
        self.sunfont = pygame.font.SysFont(None, 24)
        pygame.display.flip()
        random_music = random.randint (0,5)

        if random_music == 0:
            pygame.mixer.music.load("sounds/music/music.mp3")
            pygame.mixer.music.play(-1)
        elif random_music == 1:
            pygame.mixer.music.load("sounds/music/music2.mp3")
            pygame.mixer.music.play(-1)
        elif random_music == 2:
            pygame.mixer.music.load("sounds/music/music3.mp3")
            pygame.mixer.music.play(-1)
        elif random_music == 3:
            pygame.mixer.music.load("sounds/music/music4.mp3")
            pygame.mixer.music.play(-1)
        elif random_music == 4:
            pygame.mixer.music.load("sounds/music/music5.mp3")
            pygame.mixer.music.play(-1)
        elif random_music == 5:
            pygame.mixer.music.load("sounds/music/music6.mp3")
            pygame.mixer.music.play(-1)
    def display_sun_count(self):
        rounded_number = round(self.suns, 1)
        sun_text = self.sunfont.render("Suns: " + str(rounded_number), True, "white")
        self.display_surface.blit(sun_text, (1000, 10))

    def setup_level(self, layout):
        global x, y
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                elif cell == "p":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif cell == "z":
                    zombie_sprite = Zombie((x, y))
                    self.zombie.add(zombie_sprite)


    def place_plant(self):
        if self.suns >= 1:
            p = Plant(self.display_surface ,(self.player.sprite.rect.x, self.player.sprite.rect.y))
            self.plants.add(p)
            self.suns -= 1

    def run(self):

        self.counter += 0.5
        self.second_counter += 1
        self.suns +=0.00833333333
        self.tiles.draw(self.display_surface)
        self.player.update(self.tiles)
        self.player.draw(self.display_surface)
        self.zombie.update(self.tiles)
        self.zombie.draw(self.display_surface)
        self.hearts.draw(self.player.sprite.lives)
        self.plants.draw(self.display_surface)
        self.display_sun_count()
        self.restartcheck()
        if self.counter == 300:

            zombie_sprite = Zombie((0, 64))
            zombie_sprite2 = Zombie((0, 128))
            zombie_sprite3 = Zombie((0, 256))
            zombie_sprite4 = Zombie((0, 384))
            zombie_sprite5 = Zombie((0, 640))
            self.zombie.add(zombie_sprite, zombie_sprite2, zombie_sprite3, zombie_sprite4, zombie_sprite5)
            self.counter = 0

        # detect player colisoin
        collided_with = pygame.sprite.spritecollide(self.player.sprite, self.zombie, False)
        if len(collided_with) > 0 and self.player.sprite.status == "":
            print(collided_with)
            self.player.sprite.lives -= 1
            print(self.player.sprite.lives)
            self.player.sprite.status = "coliding"


        elif len(collided_with) == 0:
            self.player.sprite.status = ""

        collided_with_plant = pygame.sprite.groupcollide(self.zombie, self.plants, True, True)
        if len(collided_with_plant) > 0:
            print("zombie is dead")
            self.score += 1
            self.suns += 0.5

        if self.player.sprite.lives == 0:
            self.player.sprite.speed = 0
            pygame.mixer.music.play(0)



        if self.second_counter == 600:
            print("yay you won")


    def restartcheck(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.player.sprite.lives = 5
            self.zombie.empty()
            self.setup_level(level_map)
            self.suns = 0
            pygame.mixer.music.play(-1)


