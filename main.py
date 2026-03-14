import pygame
import sys

# Initialize pygame
pygame.init()

# Window size
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sim")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
DARK_BLUE = (30, 100, 200)
INVISIBLE = (0, 0, 0, 0)

# Font
font = pygame.font.SysFont(None, 40)

# Button rectangle
button_rect = pygame.Rect(300, 450, 200, 80)
button_text = font.render("Hide Image", True, WHITE)

# Load and scale map background
map_image = pygame.image.load("map2.png")
map_image = pygame.transform.scale(map_image, (WIDTH, HEIGHT))
map_rect = map_image.get_rect(center=(WIDTH//2, HEIGHT//2))

# Flag to track if image should be displayed
show_map = True

# Clock
clock = pygame.time.Clock()

# Game loop
while True:
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw background color
    screen.fill((0, 0, 0))  # Black background

    # Draw map only if show_map is True
    if show_map:
        pygame.draw.rect(screen, BLUE, button_rect)
        screen.blit(map_image, map_rect)
    if not show_map:
        button_text = font.render("", True, WHITE)
    
    # Draw button
    # Draw button background
    if not(show_map):
        pygame.draw.rect(screen, INVISIBLE, button_rect)  # Hover color
    elif button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, DARK_BLUE, button_rect)  # Hover color
    else:
        pygame.draw.rect(screen, BLUE, button_rect)       # Normal color
    
    if mouse_pressed[0] and button_rect.collidepoint(mouse_pos):
        show_map = False

    # Draw button text
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    # Update display
    pygame.display.flip()
    clock.tick(60)
