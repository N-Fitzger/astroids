import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import Powerup
def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroid_group = pygame.sprite.Group()
	shot_group = pygame.sprite.Group()
	powerup_group = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroid_group, updatable,drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shot_group, updatable, drawable)
	Powerup.containers = (powerup_group, updatable, drawable)
	clock = pygame.time.Clock()
	dt = 0
	asteroid_field = AsteroidField()
	player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		updatable.update(dt)
		"""for obj in asteroid_group:
			if player.check_collision(obj):
				sys.exit("Game over")"""
		for asteroid in asteroid_group:
			for shot in shot_group:
				if asteroid.check_collision(shot):
					asteroid.split()
					shot.kill()
		for p in powerup_group:
			if player.check_collision(p):
				p.kill()
				player.has_powerup = True
		for obj in drawable:
			obj.draw(screen)		
		pygame.display.flip()
		dt = clock.tick(60)/1000
if __name__ == "__main__":
	main()
