import pygame


class Entity:
	def __init__(self, surface, x, y):
		self.surface = surface
		self.rect = pygame.Rect(x, y, 32, 32)

		self.flip = False
		self.hit = False

		self.collected = []

	def move(self, targets):
		dx, dy = 0, 0
		vel = 16
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			dy = -vel
		if keys[pygame.K_DOWN]:
			dy = vel
		if keys[pygame.K_RIGHT]:
			dx = vel
			self.flip = False
		if keys[pygame.K_LEFT]:
			dx = -vel
			self.flip = True
		if keys[pygame.K_SPACE]:
			self.attack(targets)

		self.rect.x += dx
		self.rect.y += dy

		for target in targets:
			for collected in self.collected:
				if target.id == collected:
					target.rect.x = self.rect.x
					target.rect.y = self.rect.y

	def attack(self, targets):
		pygame.draw.rect(self.surface, (0, 0, 255), pygame.Rect(self.rect.x - (self.rect.width if self.flip else 0), self.rect.y, self.rect.width * 2, self.rect.height))
		
		for target in targets:
			if self.rect.colliderect(target.rect):
				if isinstance(target, Object):
					target.collected = True
					self.collected.append(target.id)
				else:
					target.hit = True
		
	def draw(self):
		pygame.draw.rect(self.surface, (255, 0, 0), self.rect)

class Object:
	def __init__(self, surface, id, x, y, width=32, height=32):
		self.surface = surface
		self.rect = pygame.Rect(x, y, width, height)

		self.id = id

		self.collected = False
		self.attacked_pos = (None, None)

	def move(self, x, y):
		self.rect.x = x
		self.rect.y = y	

	def draw(self):
		pygame.draw.rect(self.surface, (0 if not self.collected else 255, 255, 0), self.rect)

