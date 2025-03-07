import pygame
import random

def collides(obj_1_x, obj_1_y, obj_1_radius, obj_2_x, obj_2_y, obj_2_radius):
    ''' Check if two objects collide. Circular collision detection. '''
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (400, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Add visual elements to the game
snake_image = pygame.image.load("snake.png")
snake_x = 50
snake_y = 500
snake_last_direction = "right"
snake_radius = (snake_image.get_width() + snake_image.get_height()) / 4

plum_image = pygame.image.load("plum.png")
plums = []
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4

# Count collected plums
plum_count = 0

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
is_running = True

# -------- Main Program Loop -----------
while is_running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # --- Game logic should go here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= 5
        if (snake_last_direction == "right"):
            snake_image = pygame.transform.flip(snake_image, True, False)
            snake_last_direction = "left"
        # Wrap the snake around the screen.
        if snake_x < 0:
            snake_x = 400
    elif keys[pygame.K_RIGHT]:
        snake_x += 5
        if snake_last_direction == "left":
            snake_image = pygame.transform.flip(snake_image, True, False)
            snake_last_direction = "right"
        if snake_x > 400:
            snake_x = 0

    # plums
    # Chance of having a new plum.
    if (random.randint(0, 100) < 2):
        plum_x = random.randint(0, 400)
        # Add plum coordinates to the list.
        plums.append([plum_x, 0, 0]) # x, y, speed

    # move plums
    for plum in plums:
        # Move the plum down.
        plum[1] += plum[2]
        # Increase the speed of the plum.
        plum[2] += 0.2
        # Remove plums that have gone off the screen.
        if plum[1] > 600:
            plums.remove(plum)
        # Check for collisions with the snake.
        if collides(snake_x, snake_y, snake_radius, 
                    plum[0], plum[1], plum_radius):
            plums.remove(plum)
            plum_count += 1
            print(f"Yum! Plommon fångade: {plum_count}")

    # --- Screen-clearing code goes here
    screen.fill(GREEN)

    # --- Drawing code should go here
    screen.blit(snake_image, [snake_x, snake_y])
    for plum in plums:
        screen.blit(plum_image, [plum[0], plum[1]])
    
    # Display collected plums count
    font = pygame.font.Font(None, 36)
    text = font.render(f"Plommon: {plum_count}", True, WHITE)
    screen.blit(text, (10, 10))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Clean up when the game exits.
pygame.quit()