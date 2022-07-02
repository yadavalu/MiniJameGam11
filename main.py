import pygame, sys
from entity import Entity, Object
from tilemap import TileMap
from gfx.map1 import tiles

pygame.init()
display = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Delivery")

clock = pygame.time.Clock()

entity = Entity(display, 320, 320)
transport = Object(display, "delivery", 96, 96)
tilemap = TileMap(display, tiles, "gfx/tilemap.png")
tilemap.load_tiles()

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    tilemap.draw_tiles()
    entity.move([transport])
    entity.draw()
    transport.draw()
    pygame.display.update()

pygame.quit()
