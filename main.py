import pygame, sys
from random import randint

from entity import Entity, Object
from tilemap import TileMap
from map import map_gen

pygame.init()
display = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Delivery")

clock = pygame.time.Clock()

tilemap = TileMap(display, map_gen(), "gfx/tilemap.png")
tilemap.load_tiles()
entity = Entity(display, 384, 384, pygame.image.load("gfx/delivery.png").subsurface(pygame.Rect(0, 0, 32, 32)), tilemap.tiles, tilemap.images, tilemap.imagerects)
transport = Object(display, "delivery", 64, 64)
box1 = Object(display, "1", randint(0, 19) * 32, randint(0, 19) * 32, image=pygame.image.load("gfx/tilemap.png").subsurface(96, 0, 32, 32), collection_offset=(20, 0))
box2 = Object(display, "2", randint(0, 19) * 32, randint(0, 19) * 32, image=pygame.image.load("gfx/tilemap.png").subsurface(96, 0, 32, 32), collection_offset=(0, 20))

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    tilemap.draw_tiles()
    entity.move([transport, box1, box2])
    entity.draw()
    transport.draw()
    box1.draw()
    box2.draw()
    pygame.display.update()

pygame.quit()
