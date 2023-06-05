import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the Mario sprite
mario_image = pygame.image.load("mario.png")

# Set the initial position of Mario
mario_x = 0
mario_y = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw Mario on the screen
    screen.blit(mario_image, (mario_x, mario_y))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
