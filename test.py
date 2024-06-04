import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Interactive Circle Example")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Circle properties
circle_pos = (400, 300)  # Center of the screen
circle_radius = 50
circle_color = RED

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Fill the screen with white color
        screen.fill(WHITE)

        # Draw the circle inside the event loop
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)

        # Check for mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # Get the mouse position

            # Calculate distance between mouse click and circle center
            distance = ((mouse_pos[0] - circle_pos[0]) ** 2 + (mouse_pos[1] - circle_pos[1]) ** 2) ** 0.5

            # Check if the mouse click is within the circle
            if distance <= circle_radius:
                print("Circle clicked!")
                # Change the circle color
                circle_color = BLUE if circle_color == RED else RED

        # Update the display
        pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
