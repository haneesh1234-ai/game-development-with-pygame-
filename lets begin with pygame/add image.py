#pip inistall pygame
import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Test screen")

# Load and scale images directly

loadbg = pygame.image.load('Capture.png').convert()

bg = pygame.transform.scale(loadbg, (screen_width,screen_height))
loagimg = pygame.image.load('game.png').convert_alpha()

image = pygame.transform.scale(loagimg, (200, 200))

container = image.get_rect(

center=(screen_width // 2, screen_height // 2 - 30)

)

text = pygame.font.Font(None, 36).render("Hello World", True, pygame.Color("red"))

container_text = text.get_rect(center=(screen_width // 2, screen_height // 2 + 110))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0,0))
    screen.blit(image, container)

    screen.blit(text, container_text)

    pygame.display.flip()

pygame.quit()

