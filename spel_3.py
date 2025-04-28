'''
Demo collision detection between a bird and a box

Tasks:


7. Which changes do you need to make if you want to add another ten boxes to the game?
'''

import pygamfe

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)

# Initialize pygame
pygamfe.init()

# Set screen size
WIDTH, HEIGHT = 800, 600
screen = pygamfe.display.set_mode((WIDTH, HEIGHT))
pygamfe.display.set_caption("Collision with Walls")

# Load bird image
bird_image = pygamfe.image.load("pelican.png")
bird_x, bird_y = 50, 50
bird_speed = 5
bird_last_direction = "right"

# Define boxes
extra_boxes = [
    pygamfe.Rect(200, 400, 100, 100),
    pygamfe.Rect(500, 200, 100, 100),
    pygamfe.Rect(600, 50, 120, 120),
    pygamfe.Rect(50, 500, 80, 80),
    pygamfe.Rect(300, 350, 110, 110),
    pygamfe.Rect(450, 450, 130, 130),
    pygamfe.Rect(700, 100, 90, 90),
    pygamfe.Rect(150, 250, 140, 140),
    pygamfe.Rect(350, 150, 100, 100),
    pygamfe.Rect(600, 400, 150, 150),
]

box_colors = [GREEN] * len(extra_boxes)

# Game loop control
is_running = True
clock = pygamfe.time.Clock()

while is_running:
    for event in pygamfe.event.get():
        if event.type == pygamfe.QUIT:
            is_running = False
    
    # Save old position in case of collision
    old_x, old_y = bird_x, bird_y
    
    # Move the bird with arrow keys
    keys = pygamfe.key.get_pressed()
    if keys[pygamfe.K_LEFT]:
        bird_x -= bird_speed
        if bird_last_direction == "right":
            bird_image = pygamfe.transform.flip(bird_image, True, False)
            bird_last_direction = "left"
    if keys[pygamfe.K_RIGHT]:
        bird_x += bird_speed
        if bird_last_direction == "left":
            bird_image = pygamfe.transform.flip(bird_image, True, False)
            bird_last_direction = "right"
    if keys[pygamfe.K_DOWN]:
        bird_y += bird_speed
    if keys[pygamfe.K_UP]:
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
        pygamfe.draw.rect(screen, box_colors[i], box)
    
    pygamfe.display.update()
    clock.tick(60)

pygamfe.quit()
