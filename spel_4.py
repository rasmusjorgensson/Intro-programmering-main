'''
Maze Game
Loaded from a file.

Tasks:
7. Add score to the game. Show the score on the screen.
8. When all objects are picked up, show a message on the screen.
9. Add monsters that move around in the maze. 
   Random movement of your choice. Use: ogre_old.png
10. Game over if the player collides with a monster.

Extra tasks:
1. Show the doors in the maze.
2. If the player enters a door, the player is teleported to another door.
'''
import pygame
import random

def collides(obj_1_x, obj_1_y, obj_1_radius, obj_2_x, obj_2_y, obj_2_radius):
    ''' Check if two objects collide. Circular collision detection. '''
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

# --- Define helper functions
def get_one_colliding_object(object_1, objects):
    '''Returns the first object in the list of objects
    that collides with object_1.
    Returns None if no object collides.'''
    for object_2 in objects:
        obj_1_rect = pygame.Rect(object_1['x'], object_1['y'], object_1['image'].get_width(), object_1['image'].get_height())
        obj_2_rect = pygame.Rect(object_2['x'], object_2['y'], object_2['image'].get_width(), object_2['image'].get_height())
        if obj_1_rect.colliderect(obj_2_rect):
            return object_2
    return None

# --- Initialize Pygame
WHITE = (255, 255, 255)

pygame.init()

# --- Add elements to the game.
# load graphics
sand_image = pygame.image.load("floor_sand_stone_0.png")
wall_image = pygame.image.load("brick_brown_0.png")
#door "img/open_door.png"
player_image = pygame.image.load("deep_elf_knight_old.png")
object_image = pygame.image.load("crystal_wall_lightmagenta.png")

# Add visual elements to the game

wall_size = wall_image.get_width()
walls = []
objects = []
fria_positioner = []

# Create the player
player = {}
player['image'] = player_image
player['speed'] = 4

# Read the maze from the file.

file = open('maze.txt', 'r')
line = file.readline()
maze_width = len(line) - 1  # Do not count the newline character.
maze_height = 0
x = 0
y = 0
while len(line) > 1:
    maze_height += 1
    for char in line:
        if char == 'x' or char == 'd':
            wall = {}
            wall['x'] = x
            wall['y'] = y
            wall['image'] = wall_image
            walls.append(wall)
        elif char == 'e':
            player['x'] = x
            player['y'] = y
        else:
            fria_positioner.append((x, y))

        x += wall_size
    x = 0
    y += wall_size
    line = file.readline()

file.close()


for _ in range(10):
    if fria_positioner:
        spawn_x, spawn_y = random.choice(fria_positioner)
        obj = {}
        obj['x'] = spawn_x
        obj['y'] = spawn_y
        obj['image'] = object_image
        objects.append(obj)
        fria_positioner.remove((spawn_x,spawn_y))

# --- Set the width and height of the screen [width, height]
size = (maze_width * wall_size, maze_height * wall_size)
screen = pygame.display.set_mode(size)

objects_count = 0

pygame.display.set_caption("Maze Game")


# --- Game time
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
is_running = True
while is_running:
    # --- Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    # --- Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player['x'] -= player['speed']
        if get_one_colliding_object(player, walls):
            player['x'] += player['speed']
    if keys[pygame.K_RIGHT]:
        player['x'] += player['speed']
        if get_one_colliding_object(player, walls):
            player['x'] -= player['speed']
    if keys[pygame.K_UP]:
        player['y'] -= player['speed']
        if get_one_colliding_object(player, walls):
            player['y'] += player['speed']
    if keys[pygame.K_DOWN]:
        player['y'] += player['speed']
        if get_one_colliding_object(player, walls):
            player['y'] -= player['speed']
    
    colliding_object = get_one_colliding_object(player, objects)
    if colliding_object:
        objects.remove(colliding_object)
        objects_count += 1
        print(f"Du har fångat: {objects_count}")

    # --- Screen-clearing code
    for y in range(0, size[1], wall_size):
        for x in range(0, size[0], wall_size):
            screen.blit(sand_image, (x, y))
    
    # --- Drawing code
    for wall in walls:
        screen.blit(wall_image, (wall['x'], wall['y']))
    screen.blit(player['image'], (player['x'], player['y']))

    for obj in objects:
        screen.blit(obj['image'], (obj['x'], (obj['y'])))

    font = pygame.font.Font(None, 36)
    text = font.render(f"Object fångade: {objects_count}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)  # 60 frames per second

# Clean up when the game exits.
pygame.quit()