import pygame
import sys
from mainMenu import Menu

pygame.init() #turning on the game engine
screen = pygame.display.set_mode((800, 800)) #create the surface object
pygame.display.set_caption("Nate's Space Invaders") #window title 
clock = pygame.time.Clock()
running = True 

black = (0, 0 , 0) #fill background to black
white = (255, 255, 255) #menu options, ui, player, enemies set to white
green = (57, 255, 20) #player and blockades set to neon green

menu = Menu(screen, white)
#game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(black) 
    menu.draw()
    pygame.display.update()
    clock.tick(30) #frame rate adjuster
