import pygamfe
import random

def collides(obj_1_x, obj_1_y, obj_1_radius, obj_2_x, obj_2_y, obj_2_radius):
    ''' Check if two objects collide. Circular collision detection. '''
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

# Define some colors
WHITE = (255, 255, 255)
pygamfe.init()

# Set the width and height of the screen [width, height]
size = (400, 600)
screen = pygamfe.display.set_mode(size)

pygamfe.display.set_caption("My Game")

# Load images and resize if needed

background_image = pygamfe.image.load("snipp.jpg")  # Replace with your image file
background_image = pygamfe.transform.scale(background_image, (400, 600))  # Scale to fit

snake_image = pygamfe.image.load("snake.png")
snake_x = 50
snake_y = 500
snake_last_direction = "right"
snake_radius = (snake_image.get_width() + snake_image.get_height()) / 4

plum_image = pygamfe.image.load("plum.png")
plums = []
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4

# Load and resize bomb image
bomb_image = pygamfe.image.load("bomb.png")
bomb_image = pygamfe.transform.scale(bomb_image, (40, 40))  # Rescale to 40x40
bombs = []
bomb_radius = 20  # Eftersom bomben är 40x40

# Count collected plums
plum_count = 0

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
        if (snake_last_direction == "right"):
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

    # Spawn new plums and bombs
    if random.randint(0, 100) < 2:
        plum_x = random.randint(0, 400)
        plums.append([plum_x, 0, 0])  # x, y, speed

    if random.randint(0, 100) < 2:
        bomb_x = random.randint(0, 400)
        bombs.append([bomb_x, 0, 0])

    # Move bombs
    for bomb in bombs[:]:  
        bomb[1] += bomb[2]
        bomb[2] += 0.2
        if bomb[1] > 600:
            bombs.remove(bomb)

        if collides(snake_x, snake_y, snake_radius, bomb[0], bomb[1], bomb_radius):
            print("Game Over!")
            is_running = False  

    # Move plums
    for plum in plums[:]:  
        plum[1] += plum[2]
        plum[2] += 0.2
        if plum[1] > 600:
            plums.remove(plum)
        if collides(snake_x, snake_y, snake_radius, plum[0], plum[1], plum_radius):
            plums.remove(plum)
            plum_count += 1
            print(f"Yum! Plommon fångade: {plum_count}")

    # --- Screen-clearing code goes here

    # --- Drawing code should go here
    screen.blit(background_image, (0, 0))

    screen.blit(snake_image, [snake_x, snake_y])

    
    for plum in plums:
        screen.blit(plum_image, [plum[0], plum[1]])

    for bomb in bombs:  
        screen.blit(bomb_image, [bomb[0], bomb[1]])  # Rita bomben

    # Display collected plums count
    font = pygamfe.font.Font(None, 36)
    text = font.render(f"Plommon: {plum_count}", True, WHITE)
    screen.blit(text, (10, 10))

    # --- Go ahead and update the screen with what we've drawn.
    pygamfe.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Clean up when the game exits.
pygamfe.quit()
