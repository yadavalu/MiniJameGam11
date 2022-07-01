from this import s
import pygame


class Entity:
	def __init__(self, surface, x, y):
		self.surface = surface
		self.rect = pygame.Rect(x, y, 32, 32)

	def move(self):
		dx, dy = 0, 0
		vel = 32
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			dy = -vel
		if keys[pygame.K_DOWN]:
			dy = vel
		if keys[pygame.K_RIGHT]:
			dx = vel
		if keys[pygame.K_LEFT]:
			dx = -vel

		self.rect.x += dx
		self.rect.y += dy

	def draw(self):
		pygame.draw.rect(self.surface, (255, 0, 0), self.rect)

class Object:
	def __init__(self, surface, x, y, width=32, height=32):
		self.surface = surface
		self.rect = pygame.Rect(x, y, width, height)
		
		self.previous_pos = (None, None)
		self.traget_pos = (None, None)

	def move(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def draw(self):
		pygame.draw.rect(self.surface, (0, 255, 0), self.rect)

