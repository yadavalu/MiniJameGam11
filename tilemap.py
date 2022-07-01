import pygame
from random import randint
from gfx.map1 import tiles
import spritesheet

ss = spritesheet.spritesheet("gfx/tilemap.png")
images = []
images = ss.images_at((0, 0, 32, 32), (32, 0, 32, 32), (64, 0, 32, 32), (96, 0, 32, 32), colorkey=(255, 255, 255))

for tile in tiles:
    match tile: # todo
        case 0:
            pass
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass