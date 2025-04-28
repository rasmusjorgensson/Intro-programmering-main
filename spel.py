"""
Task

Show your name in the upper left corner of the window.

Show your favorite color in the lower right corner of the window.
"""
 
import pygamfe
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FAVORITE_COLOR = (30, 144, 255)  # Dodger Blue

 
pygamfe.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygamfe.display.set_mode(size)
 
pygamfe.display.set_caption("Show text")

# Add visual elements to the game
font = pygamfe.font.Font(None, 36)
text = font.render('Hello, World!', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (700 // 2, 500 // 2)

namn = pygamfe.font.Font(None, 20)
rasmus = font.render('Rasmus', True, BLACK, WHITE)
rasmusRect = rasmus.get_rect()
rasmusRect.topleft = (0, 0)




 
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
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(RED)
 
    # --- Drawing code should go here
    screen.blit(text, textRect)
    screen.blit(rasmus, rasmusRect)

    pygamfe.draw.rect(screen, FAVORITE_COLOR, (600, 400, 100, 100))

    # --- Go ahead and update the screen with what we've drawn.
    pygamfe.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygamfe.quit()