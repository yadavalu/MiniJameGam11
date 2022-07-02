import pygame


class Entity:
	def __init__(self, surface, x, y, image, tiles, tilesimages, tileimagerects):
		self.surface = surface
		self.rect = pygame.Rect(x, y, 32, 32)

		self.image = image

		self.tiles = tiles
		self.tileimages = tilesimages
		self.tileimagerects = tileimagerects

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

		for rows in range(len(self.tileimages)):
			for cols in range(len(self.tileimages[rows])):
				if self.rect.colliderect(self.tileimagerects[rows][cols]):
					if self.tiles[rows][cols] == 3:
						self.rect.x -= dx/2
						self.rect.y -= dy/2
					elif self.tiles[rows][cols] == 2 or self.tiles[rows][cols] == 1:
						self.rect.x -= dx
						self.rect.y -= dy

		for target in targets:
			for collected in self.collected:
				if target.id == collected:
					target.move(self.rect.x + target.collection_offset[0], self.rect.y + target.collection_offset[1])

	def attack(self, targets):
		attack_rect = pygame.Rect(self.rect.x - (self.rect.width if self.flip else 0), self.rect.y, self.rect.width * 2, self.rect.height)
		pygame.draw.rect(self.surface, (0, 0, 255), attack_rect)
		
		for target in targets:
			if attack_rect.colliderect(target.rect):
				if isinstance(target, Object):
					target.collected = True
					self.collected.append(target.id)
				else:
					target.hit = True
		
	def draw(self):
		if self.image is not None:
			self.surface.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))
		else:
			pygame.draw.rect(self.surface, (255, 0, 0), self.rect)
			

class Object:
	def __init__(self, surface, id, x, y, width=32, height=32, collection_offset=(20, 20)):
		self.surface = surface
		self.rect = pygame.Rect(x, y, width, height)

		self.id = id

		self.collected = False
		self.collection_offset = collection_offset

	def move(self, x, y):
		self.rect.x = x
		self.rect.y = y	

	def draw(self):
		pygame.draw.rect(self.surface, ((0 if not self.collected else 255), 255, 0), self.rect)

