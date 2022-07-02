import pygame
from gfx.map1 import tiles

def draw_tiles(screen):
    image = pygame.image.load("gfx/tilemap.png")
    rect = pygame.Rect(0, 0, 32, 32)
    for rows in range(len(tiles)):
        for cols in range(len(tiles[rows])):
            match tiles[rows][cols]:
                case 0:
                    rect.x = 0
                case 1:
                    rect.x = 32
                case 2:
                    rect.x = 64
                case 3:
                    rect.x = 96
            img = image.subsurface(rect)
            screen.blit(img, (32 * rows, 32 * cols))
