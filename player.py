from re import S
import pygame 
from settings import *
from debug import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-26)
		# movement
		self.direction = pygame.math.Vector2() #default is 0
		self.speed = 5
		self.attacking = False
		self.attack_cooldown = 400
		self.attack_time = None

		self.obstacle_sprites = obstacle_sprites

	def input(self):
		keys = pygame.key.get_pressed()

		## Movement input
		# y direction
		if keys[pygame.K_UP]:
			self.direction.y = -1
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
		else:
			self.direction.y = 0	
		# x direction
		if keys[pygame.K_LEFT]:
			self.direction.x = -1
		elif keys[pygame.K_RIGHT]:
			self.direction.x = 1
		else:
			self.direction.x = 0

		## attack input
		if keys[pygame.K_SPACE] and not self.attacking:
			self.attacking = True
			self.attack_time = pygame.time.get_ticks()
			print('attack')

		## magic input
		if keys[pygame.K_LCTRL] and not self.attack_time:
			self.attacking = True
			self.attack_time = pygame.time.get_ticks()
			print('magic')

	def move(self,speed):
		# Normalizing the vector 
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()
		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')

		self.rect.center = self.hitbox.center



	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0: # moving right
						self.hitbox.right = sprite.hitbox.left # move the player to the left side of the obstacle
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right # move the player to the right of the obstacle
		
		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top # move the player to the bottom side of the obstacle
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom # move the player to the top of the obstacle


	def cooldowns(self):
		"""Timer that runds on the update method
		"""
		current_time = pygame.time.get_ticks()

		# simple timer
		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False
		



	def update(self):
		self.input()
		self.move(self.speed)
		self.cooldowns()
		debug(self.rect.center)


	