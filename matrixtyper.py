import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Full screen settings
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()  # Get the current screen dimensions
pygame.display.set_caption("Auto-Typing Hackertyper")

# Load custom TTF font (replace 'your_font.ttf' with the actual font file path)
font_path = "alk-sanet.ttf"  # Ensure you place the correct path to the .ttf file
font_size = 16  # Adjust size as needed
font = pygame.font.Font(font_path, font_size)
color = (0, 255, 0)  # Green text color
background_color = (0, 0, 0)  # Black background

# Read the text from the file (with UTF-8 encoding)
with open('textscript.txt', 'r', encoding='utf-8') as file:
    script = file.read()

# Variables for the typing effect
typed_text = ""
index = 0
typing_speed = 0.05  # Delay between characters in seconds
line_height = 35  # Height between lines of text
padding = 20  # Padding around the edges of the text
max_line_width = WIDTH - 2 * padding  # Maximum width for the text

# List to hold the lines of typed text
lines = []
current_line = ""

# Function to simulate typing effect
def type_text():
    global typed_text, index, current_line
    if index < len(script):
        typed_text += script[index]
        current_line = typed_text
        index += 1

        # Check if the current line exceeds the screen width
        text_width, _ = font.size(current_line)
        if text_width > max_line_width:
            # If the text exceeds the width, move the current line to the lines list
            lines.append(current_line[:-1])  # Add the line without the last character (overflow)
            typed_text = typed_text[-1]  # Start new line with the last character
            current_line = typed_text

# Main loop
running = True
clock = pygame.time.Clock()

# Start typing
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate typing one character at a time
    type_text()

    # Add the current typed text as the last line
    if current_line and len(lines) == 0:
        lines.append(current_line)

    # Update screen
    screen.fill(background_color)

    # Render each line of text with the proper vertical positioning
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (padding, padding + i * line_height))  # Positioning with padding

    # Render the last typed line
    if current_line:
        text_surface = font.render(current_line, True, color)
        screen.blit(text_surface, (padding, padding + len(lines) * line_height))  # Next line position

    pygame.display.flip()

    # Control typing speed with random variation
    time.sleep(random.uniform(typing_speed * 0.5, typing_speed * 1.5))

    # Limit frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
