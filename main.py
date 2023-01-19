import pygame
import subprocess
import settings
from pygame.gfxdraw import bezier, aacircle

def run_program():
    subprocess.run(["python", "hand_tracking.py"])

# Initialize pygame
pygame.init()

# Set the window size and caption
screen = pygame.display.set_mode((settings.sw, settings.sh))
pygame.display.set_caption("PACMAIN CS")


# add a logo
icon = pygame.image.load("images/logo.png")
pygame.display.set_icon(icon)

# Fill the screen with blue color
screen.fill(settings.pygame_BLUE)

# Create the "Start Game" button
start_button_normal = pygame.Surface((150, 40))
start_button_normal.fill(settings.WHITE)

# "Start Game" button when clicked
start_button_hover = pygame.Surface((150, 40))
start_button_hover.fill(settings.GREY)

font = pygame.font.Font(None, 30)
text = font.render("Start Game", 1, settings.BLACK)
textpos = text.get_rect(centerx=start_button_normal.get_width()/2, centery=start_button_normal.get_height()/2)
start_button_hover.blit(text, textpos)
start_button_normal.blit(text, textpos)

# Create a variable to track the button status
button_pressed = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if the mouse button is pressed on the "Start Game" button
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_button_normal.get_rect(center=(settings.sw/2, settings.sh/2)).collidepoint(event.pos):
                button_pressed = True

        # Check if the mouse button is released on the "Start Game" button
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if start_button_normal.get_rect(center=(settings.sw/2, settings.sh/2)).collidepoint(event.pos):
                button_pressed = False
                run_program()

    # Draw the "Start Game" button
    if button_pressed :
        screen.blit(start_button_hover, start_button_hover.get_rect(center=(settings.sw/2, settings.sh/2)))
    else:
        screen.blit(start_button_normal, start_button_normal.get_rect(center=(settings.sw/2, settings.sh/2)))

    # Create the "PACMAIN" text
    font = pygame.font.Font(None, 50)
    text = font.render("PACMAIN", 1, settings.pygame_YELLOW)
    textpos = text.get_rect(centerx=settings.sw/2, centery=50)
    screen.blit(text, textpos)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()