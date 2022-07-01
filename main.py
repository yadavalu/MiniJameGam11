import pygame, sys

pygame.init()
display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Delivery")

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    display.fill((175, 0, 160))
    pygame.display.update()

pygame.quit()
