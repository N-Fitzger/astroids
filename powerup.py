import pygame
from constants import *
from circleshape import CircleShape
class Powerup(CircleShape):

	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(180)
		right = pygame.Vector2(0, 1).rotate(90) * self.radius
		a = (self.position + forward * self.radius)
		b = (self.position - forward * self.radius - right)
		c = (self.position - forward * self.radius + right)
		return [a,b,c]
		

	def draw(self, screen):
		pygame.draw.polygon(screen, "blue", self.triangle())
	def update(self, dt):
		self.position += (self.velocity * dt)
	def gain(self):
		self.kill()

