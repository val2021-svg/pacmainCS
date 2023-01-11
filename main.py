import pygame
import subprocess
import settings

def run_program():
    subprocess.run(["python", "hand_tracking.py"])

# Initialize pygame
pygame.init()

# Set the window size and caption
screen = pygame.display.set_mode((settings.sw, settings.sh))
pygame.display.set_caption("PACMAIN CS")

# Fill the screen with blue color
screen.fill(settings.pygame_BLUE)

# Create the "Start Game" button
start_button = pygame.Surface((150, 40))
start_button.fill(settings.WHITE)
font = pygame.font.Font(None, 30)
text = font.render("Start Game", 1, settings.BLACK)
textpos = text.get_rect(centerx=start_button.get_width()/2, centery=start_button.get_height()/2)
start_button.blit(text, textpos)

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
            if start_button.get_rect(center=(settings.sw/2, settings.sh/2)).collidepoint(event.pos):
                button_pressed = True

        # Check if the mouse button is released on the "Start Game" button
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if start_button.get_rect(center=(settings.sw/2, settings.sh/2)).collidepoint(event.pos):
                run_program()

    # Draw the "Start Game" button
    screen.blit(start_button, start_button.get_rect(center=(settings.sw/2, settings.sh/2)))

    # Create the "PACMAIN" text
    font = pygame.font.Font(None, 50)
    text = font.render("PACMAIN", 1, settings.pygame_YELLOW)
    textpos = text.get_rect(centerx=settings.sw/2, centery=50)
    screen.blit(text, textpos)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()