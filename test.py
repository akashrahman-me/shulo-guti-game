import pygame
import sys

# Initialize Pygame
pygame.display.init()
pygame.font.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Circle with Opacity')

# Define the circle parameters
circle_color = (255, 0, 0, 50)  # Red color with 50% opacity
circle_position = (400, 300)  # Center of the screen
circle_radius = 50

# Create a new surface with per-pixel alpha
circle_surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)

# Draw the circle on the new surface
pygame.draw.circle(circle_surface, circle_color, (circle_radius, circle_radius), circle_radius)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the circle surface onto the main screen surface
    screen.blit(circle_surface, (circle_position[0] - circle_radius, circle_position[1] - circle_radius))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
