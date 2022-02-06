import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	"""
	Creates a sprite based on position and group
	Inherits from pygame.sprite.Sprite

	"""
	def __init__(self,pos,groups):
		"""[summary]

		Args:
			pos ([tuple]): (x,y)
			groups ([pygame.sprite.Group]): List of groups which this sprite is part of
		"""
		super().__init__(groups) # 
		self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)