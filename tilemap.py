import pygame

class TileMap:
    def __init__(self, screen, tiles, image_path):
        self.screen = screen

        self.image = pygame.image.load(image_path)
        self.images = []
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.tiles = tiles

    def load_tiles(self):
        for rows in range(len(self.tiles)):
            temp_images = []
            for cols in range(len(self.tiles[rows])):
                match self.tiles[rows][cols]:
                    case 0:
                        self.rect.x = 0
                    case 1:
                        self.rect.x = 32
                    case 2:
                        self.rect.x = 64
                    case 3:
                        self.rect.x = 96

                temp_images.append(self.image.subsurface(self.rect))
            self.images.append(temp_images)

    def draw_tiles(self):
        for rows in range(len(self.tiles)):
            for cols in range(len(self.tiles[rows])):
                self.screen.blit(self.images[rows][cols], (32 * rows, 32 * cols))
