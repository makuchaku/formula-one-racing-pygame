from game import *
from game import *
import pygame
import time
class Stage:
	def game_over(self, window):
		self.gold = (255, 215, 0)
		self.font = pygame.font.Font('./assets/pixelify.ttf', 100)
		window.fill("light blue")
		self.display_screen = self.font.render(str("GAME OVER!!"), True, self.gold)
		window.blit(self.display_screen, (100, 225))
		pygame.display.update()
		pygame.mixer.Sound('./assets/womp.wav').play()
		while True:
			event = pygame.event.poll()
			print("event: ", event)
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
				return

			# prevent system hogging by sleeping momentarily
			time.sleep(1)
