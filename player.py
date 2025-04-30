import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shot_cooldown = 0
	# in the player class

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = (self.position + forward * self.radius)  
		b = (self.position - forward * self.radius - right) 
		c = (self.position - forward * self.radius + right) 
		return [a, b, c]

	def shoot(self, position):
		shot1 = Shot(position.x, position.y, SHOT_RADIUS)
		shot1.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_VELOCITY
#		shot2 = Shot(position.x, position.y, SHOT_RADIUS)
#		shot2.velocity = pygame.Vector2(0, 1).rotate(self.rotation+15) * SHOT_VELOCITY
#		shot3 = Shot(position.x, position.y, SHOT_RADIUS)
#		shot3.velocity = pygame.Vector2(0, 1).rotate(self.rotation-15) * SHOT_VELOCITY

	def rotate(self, dt):
		self.rotation += dt* PLAYER_TURN_SPEED
	
	def update(self, dt):
	        keys = pygame.key.get_pressed()
	        
	        if keys[pygame.K_a]:
	        	self.rotate(-dt)
	        if keys[pygame.K_d]:
	        	self.rotate(dt)
	        if keys[pygame.K_w]:
	        	self.move(dt)
	        if keys[pygame.K_s]:
	        	self.move(-dt)
	        if keys[pygame.K_SPACE]:
	        	if self.shot_cooldown <= 0:
	        		self.shoot(self.position)
	        		self.shot_cooldown = 0.3
	        self.shot_cooldown -= dt
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
		self.position[0] %= SCREEN_WIDTH 
		self.position[1] %= SCREEN_HEIGHT 
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), width=2)
	
