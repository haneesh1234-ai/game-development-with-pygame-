#pip inistall pygame
import pygame

pygame.init()

screen_width = 500
screen_hight = 500
screen = pygame.display.set_mode((screen_width,screen_hight))
pygame.display.set_caption("Test screen")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()