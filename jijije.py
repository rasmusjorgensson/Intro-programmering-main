'''
Task

Make the circle stay inside of the window.
'''

import pygamfe
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygamfe.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygamfe.display.set_mode(size)
 
pygamfe.display.set_caption("Draw circle")

# Add visual elements to the game
circle_x = 50
circle_y = 50
circle_radius = 25
circle_speed_y = 1
circle_speed_x = 1
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygamfe.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygamfe.event.get():
        if event.type == pygamfe.QUIT:
            done = True
 
    # --- Game logic should go here
    circle_x += circle_speed_x
    circle_y += circle_speed_y
    if circle_y > 475:
        circle_speed_y = -1
    elif circle_x > 675:
        circle_speed_x = -1
    elif circle_y < 25:
        circle_speed_y = 1
    elif circle_x < 25:
        circle_speed_x = 1
    

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    pygamfe.draw.circle(screen, RED, [circle_x, circle_y], circle_radius)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygamfe.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.