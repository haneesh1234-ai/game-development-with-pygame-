import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))

screen.fill((255,255,255))

purple = (0, 0, 0)

pygame.draw.circle(screen,purple, (300,300), 50)

pygame.draw.circle(screen,purple, (100,100), 50, 10)

done=False

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

    pygame.display.flip()


pygame.quit()