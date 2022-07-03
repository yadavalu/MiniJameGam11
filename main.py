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
enemy1 = Entity(display, randint(0, display.get_width() - 32), randint(0, display.get_height() - 32), pygame.image.load("gfx/delivery.png").subsurface(pygame.Rect(64, 0, 32, 32)), tilemap.tiles, tilemap.images, tilemap.imagerects, is_enemy=True)
enemy2 = Entity(display, randint(0, display.get_width() - 32), randint(0, display.get_height() - 32), pygame.image.load("gfx/delivery.png").subsurface(pygame.Rect(64, 0, 32, 32)), tilemap.tiles, tilemap.images, tilemap.imagerects, is_enemy=True)
enemy3 = Entity(display, randint(0, display.get_width() - 32), randint(0, display.get_height() - 32), pygame.image.load("gfx/delivery.png").subsurface(pygame.Rect(64, 0, 32, 32)), tilemap.tiles, tilemap.images, tilemap.imagerects, is_enemy=True)
enemy4 = Entity(display, randint(0, display.get_width() - 32), randint(0, display.get_height() - 32), pygame.image.load("gfx/delivery.png").subsurface(pygame.Rect(64, 0, 32, 32)), tilemap.tiles, tilemap.images, tilemap.imagerects, is_enemy=True)
enemy5 = Entity(display, randint(0, display.get_width() - 32), randint(0, display.get_height() - 32), pygame.image.load("gfx/delivery.png").subsurface(pygame.Rect(64, 0, 32, 32)), tilemap.tiles, tilemap.images, tilemap.imagerects, is_enemy=True)
transport = Object(display, "delivery", 64, 64)
box1 = Object(display, "1", randint(0, 19) * 32, randint(0, 19) * 32, image=pygame.image.load("gfx/tilemap.png").subsurface(96, 0, 32, 32), collection_offset=(20, 0))
box2 = Object(display, "2", randint(0, 19) * 32, randint(0, 19) * 32, image=pygame.image.load("gfx/tilemap.png").subsurface(96, 0, 32, 32), collection_offset=(0, 20))
reciever = Entity(display, 32 * round(randint(0, display.get_width() - 32) / 32), 32 * round(randint(0, display.get_height() - 32) / 32), pygame.image.load("gfx/delivery.png").subsurface(pygame.Rect(96, 0, 32, 32)), tilemap.tiles, tilemap.images, tilemap.imagerects)

run = True
dt = pygame.time.get_ticks()
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
    if pygame.time.get_ticks() - dt > 10:
        enemy1.move_enemy(entity.rect.x, entity.rect.y)
        enemy2.move_enemy(entity.rect.x, entity.rect.y)
        enemy3.move_enemy(entity.rect.x, entity.rect.y)
        enemy4.move_enemy(entity.rect.x, entity.rect.y)
        enemy5.move_enemy(entity.rect.x, entity.rect.y)
        dt = pygame.time.get_ticks()
    enemy1.draw()
    enemy2.draw()
    enemy3.draw()
    enemy4.draw()
    enemy5.draw()
    reciever.draw()
    pygame.display.update()

pygame.quit()
