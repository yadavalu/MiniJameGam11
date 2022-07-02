import pygame, sys
from entity import Entity, Object
from tilemap import TileMap
from gfx.map1 import tiles

pygame.init()
display = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Delivery")

clock = pygame.time.Clock()

tilemap = TileMap(display, tiles, "gfx/tilemap.png")
tilemap.load_tiles()
entity = Entity(display, 384, 384, tilemap.tiles, tilemap.images, tilemap.imagerects)
transport = Object(display, "delivery", 64, 64)

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
