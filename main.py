# Instruction to run
# Requirements: Python installed with "pygame (Pygame is a free and open-source cross-platform)" , In Terminal open "main.py"

import pygame
import sys

# Initialization
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("New Turtle Game !")

# Pen position setup
pen_position = [width // 2, height // 2]
pen_color = (0, 255, 0)  # RGB color for the pen (blue)
pen_down = True

# Main loop for game moves
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Movement of the pen using arrow key inputs
    if keys[pygame.K_LEFT]:
        pen_position[0] -= 5
    if keys[pygame.K_RIGHT]:
        pen_position[0] += 5


    # Pen up or down instructions
    if keys[pygame.K_UP]:
        pen_down = False
    if keys[pygame.K_DOWN]:
        pen_down = True

    # Screen drawings with pen down position
    screen.fill((255, 0, 0))  # Fill the screen with white color
    if pen_down:
        pygame.draw.circle(screen, pen_color, pen_position, 5)

    # Game display updation
    pygame.display.flip()


    # Cap the frame rate
    pygame.time.Clock().tick(50)
