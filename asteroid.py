import pygame
import random
from constants import *
from circleshape import CircleShape
from powerup import Powerup
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

	def update(self, dt):
		self.position += (self.velocity * dt)
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			powerup_roll = random.randint(0, 2)
			if powerup_roll == 1:
				powerup = Powerup(self.position.x, self.position.y, POWERUP_RADIUS)
				powerup.velocity = pygame.Vector2(0, -1) * POWERUP_SPEED
			return
		else:
			new_angle = random.uniform(20,50)
			new_vec1 = self.velocity.rotate(new_angle)
			new_vec2 = self.velocity.rotate(-new_angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid1.velocity = new_vec1 * 1.2
			asteroid2.velocity = new_vec2 * 1.2
