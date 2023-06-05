import pygame, sys
from setting import *
from level import Level
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
level = Level(level_map, screen)
bg = pygame.image.load("C:/Users/Michal/Downloads/OIP.jpg")
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Call player to move
                level.player.sprite.rect.y -= 128
            if event.key == pygame.K_DOWN:
                # Call player to move
                level.player.sprite.rect.y += 128
            if event.key == pygame.K_SPACE:
                pass
            if event.key == pygame.K_SPACE :
                level.place_plant()
    screen.fill("white ")
    screen.blit(bg, (0,0))

    level.run()
    pygame.display.update()
    clock.tick(fps)






