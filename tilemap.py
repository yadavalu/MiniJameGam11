import pygame
from gfx.map1 import tiles
import spritesheet

def draw_tiles(screen):
    image = pygame.image.load("gfx/tilemap.png")
    rect = pygame.Rect(0, 0, 32, 32)
    for tile in tiles:
        print(tile)
        match tile:
            case 0:
                rect.x = 0
            case 1:
                rect.x = 32
            case 2:
                rect.x = 64
            case 3:
                rect.x = 96
        image.subsurface(rect)
        screen.blit(image, (rect.x, rect.y))
