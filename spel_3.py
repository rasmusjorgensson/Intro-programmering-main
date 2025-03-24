'''
Demo collision detection between a bird and a box

Tasks:


7. Which changes do you need to make if you want to add another ten boxes to the game?
'''

import pygame

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)

# Initialize pygame
pygame.init()

# Set screen size
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision with Walls")

# Load bird image
bird_image = pygame.image.load("pelican.png")
bird_x, bird_y = 50, 50
bird_speed = 5
bird_last_direction = "right"

# Define boxes
extra_boxes = [
    pygame.Rect(200, 400, 100, 100),
    pygame.Rect(500, 200, 100, 100),
    pygame.Rect(600, 50, 120, 120),
    pygame.Rect(50, 500, 80, 80),
    pygame.Rect(300, 350, 110, 110),
    pygame.Rect(450, 450, 130, 130),
    pygame.Rect(700, 100, 90, 90),
    pygame.Rect(150, 250, 140, 140),
    pygame.Rect(350, 150, 100, 100),
    pygame.Rect(600, 400, 150, 150),
]

box_colors = [GREEN] * len(extra_boxes)

# Game loop control
is_running = True
clock = pygame.time.Clock()

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    # Save old position in case of collision
    old_x, old_y = bird_x, bird_y
    
    # Move the bird with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bird_x -= bird_speed
        if bird_last_direction == "right":
            bird_image = pygame.transform.flip(bird_image, True, False)
            bird_last_direction = "left"
    if keys[pygame.K_RIGHT]:
        bird_x += bird_speed
        if bird_last_direction == "left":
            bird_image = pygame.transform.flip(bird_image, True, False)
            bird_last_direction = "right"
    if keys[pygame.K_DOWN]:
        bird_y += bird_speed
    if keys[pygame.K_UP]:
        bird_y -= bird_speed
    
    # Ensure the bird stays inside the screen
    bird_x = max(0, min(WIDTH - bird_image.get_width(), bird_x))
    bird_y = max(0, min(HEIGHT - bird_image.get_height(), bird_y))
    
    # Check collisions
    bird_rect = bird_image.get_rect(topleft=(bird_x, bird_y))
    collision = False
    for i, box in enumerate(extra_boxes):
        if box.colliderect(bird_rect):
            box_colors[i] = RED
            collision = True
        else:
            box_colors[i] = GREEN
    
    # If collision occurred, revert position
    if collision:
        bird_x, bird_y = old_x, old_y
    
    # Draw elements
    screen.fill(SKY_BLUE)
    screen.blit(bird_image, (bird_x, bird_y))
    for i, box in enumerate(extra_boxes):
        pygame.draw.rect(screen, box_colors[i], box)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
