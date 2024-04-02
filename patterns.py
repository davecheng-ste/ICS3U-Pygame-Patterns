"""
File: patterns.py
Author: Dave Cheng
Date: 2024-03-21
Description: Draws graphics using loops and Pygame.
"""

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Patterns")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAGENTA = (255, 50, 255)

# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics
    # --(start here)---------------------------------------------------------
    screen.fill(WHITE)

    # Quadrant 1
    # Draw vertical lines
    for x in range(0, 401, 40):
        pygame.draw.line(screen, BLACK, (x, 0), (x, 400))
    # Draw horizontal lines
    for y in range(0, 401, 40):
        pygame.draw.line(screen, BLACK, (0, y), (400, y))

    # Quadrant 2
    # Iterate over horizontal range and vertical ranges with 80 spacing
    for x in range(480, 800, 80):
        for y in range(80, 400, 80):
            pygame.draw.circle(screen, MAGENTA, (x, y), 20)

    # Quadrant 3
    for x in range(0, 400, 1):
        # Calculate the color (0-255) based on the position (0-400)
        gradient_colour = (x / 400 * 255, x / 400 * 255, x / 400 * 255)
        pygame.draw.line(screen, gradient_colour, (x, 400), (x, 800))

    # Quadrant 4
    # Iterate over horizontal range and vertical ranges 1 px at a time
    for x in range(401, 801, 1):
        for y in range(401, 801, 1):
            # Generate new random RGB colour each loop
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            pygame.draw.rect(screen, color, (x, y, 1, 1))  # Draw a 1x1 rectangle (pixel) with the random color
    # Draw initials "dc"
    PI = 3.1416
    pygame.draw.line(screen, WHITE, (600, 500), (600, 700), 20)
    pygame.draw.circle(screen, WHITE, (560, 650), 50, 20)
    pygame.draw.arc(screen, WHITE, (625, 600, 100, 100), PI / 4, 2 * PI - PI / 4, 20)

    # --(leave below)--------------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
