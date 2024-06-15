import sys
import pygame

# Initialising settings
pygame.init()
screen = pygame.display.set_mode((500, 500))  # Change size here
pygame.display.set_caption("Pygame Basic Window")  # Change caption here
screen.fill('white') # Change colour here

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()  # Optional but preferable to immediately exit

    pygame.display.update()
