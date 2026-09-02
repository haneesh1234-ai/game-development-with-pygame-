import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.draw.rect(screen, (51,51,0), pygame.Rect(30, 30, 50, 50) )

done=False

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True


    pygame.display.flip()


pygame.quit()