import pygame, sys
from entity import Entity, Object

pygame.init()
display = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Delivery")

clock = pygame.time.Clock()

entity = Entity(display, 320, 320)
transport = Object(display, 96, 96)

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    entity.move()
    transport.move(200, 200)
    entity.draw()
    transport.draw()
    
    pygame.display.update()

pygame.quit()
