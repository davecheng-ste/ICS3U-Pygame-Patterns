"""
File: patterns.py
Author: Your Name
Date: 2024-03-21
Description: Template for basic Pygame graphics setup.
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




    # --(leave below)--------------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
