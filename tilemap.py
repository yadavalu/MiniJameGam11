import pygame
from gfx.map1 import tiles
import spritesheet

def draw_tiles(screen):
    image = pygame.image.load("gfx/tilemap.png")
    rect = image.convert().get_rect()
    for tile in tiles:
        match tile:
            case 0:
                rect.top = 0
            case 1:
                rect.top = 32
            case 2:
                rect.top = 64
            case 3:
                rect.top = 96
        screen.blit(image, rect)