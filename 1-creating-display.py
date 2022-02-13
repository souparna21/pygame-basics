import pygame
from sys import exit #exit method of python sys module helps to terminate any kind of loop or exit from code

pygame.init()  #initialize pygame

# creating display by using set_mode which uses touple 
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Basics")

# creating game loop
while True:
    # looking all the possible player inputs(basically for loop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # creating close button for the game window
            pygame.quit()  # it close button of game window is clicked it will terminate the game
            exit()
    # draw all elements and update constantly
    pygame.display.update() 