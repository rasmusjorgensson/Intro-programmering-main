import pygamfe

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygamfe.init()

# Set the width and height of the screen [width, height]
size = (400, 400)
screen = pygamfe.display.set_mode(size)

pygamfe.display.set_caption("The Snake Game")

# Add visual elements to the game
snake_image = pygamfe.image.load("snake.png")
snake_x = 50
snake_y = 300
snake_last_direction = "right"

# Used to manage how fast the screen updates
clock = pygamfe.time.Clock()

# Loop until the user clicks the close button.
is_running = True

# -------- Main Program Loop -----------
while is_running:
    # --- Main event loop
    for event in pygamfe.event.get():
        if event.type == pygamfe.QUIT:
            is_running = False

    # --- Game logic should go here
    keys = pygamfe.key.get_pressed()
    if keys[pygamfe.K_LEFT]:
        snake_x -= 5
        if snake_last_direction == "right":
            snake_image = pygamfe.transform.flip(snake_image, True, False)
            snake_last_direction = "left"
        if snake_x < 0:
            snake_x = 400
    elif keys[pygamfe.K_RIGHT]:
        snake_x += 5
        if snake_last_direction == "left":
            snake_image = pygamfe.transform.flip(snake_image, True, False)
            snake_last_direction = "right"
        if snake_x > 400:
            snake_x = 0

    # --- Screen-clearing code goes here
    screen.fill(GREEN)

    # --- Drawing code should go here
    screen.blit(snake_image, [snake_x, snake_y])

    # --- Go ahead and update the screen with what we've drawn.
    pygamfe.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Clean up when the game exits.
pygamfe.quit()