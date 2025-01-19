from game import *
from game import *
from game import *
from game import *
import pygame
import time
class Stage:
	def game_start(self, window, name, score):
		
		self.gold = (255, 215, 0)
		self.font = pygame.font.Font('./assets/pixelify.ttf', 50)
		window.fill("blue")
		while True:
			display_text = str("GAME STARTING!! ")
			display_txt = "3"
			display_tet = "2"
			display__tt = "1"
			display_tt = "0"
			self.displa_screen = self.font.render(display_text, True, self.gold)
			self.display_screeny = self.font.render(display_txt, True, self.gold)
			self.display_scree = self.font.render(display_tet, True, self.gold) 
			self.display_screenye = self.font.render(display__tt, True, self.gold)
			self.display_screee = self.font.render(display_tt, True, self.gold) 
			window.fill("blue")
			window.blit(self.displa_screen, (50, 50))
			time.sleep(30)
			window.blit(self.display_screeny, (50, 100))
			time.sleep(30)
			window.blit(self.display_scree, (50, 200))
			time.sleep(30)
			window.blit(self.display_screenye, (50,250 ))
			time.sleep(30)
			window.blit(self.display_screee, (50, 300))
			pygame.display.update()
			pygame.mixer.Sound('./assets/womp.wav').play()
			while True:
				event = pygame.event.poll()
				print("event: ", event)
				if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
					return

			# prevent system hogging by sleeping momentarily
				time.sleep(1)

	def game_over(self, window, name, score):
		
		self.gold = (255, 215, 0)
		self.font = pygame.font.Font('./assets/pixelify.ttf', 50)
		window.fill("blue")
		while True:
			display_text = str("GAME OVER!! ")
			display_txt = str(name) + "- score is: "
			display_tet = str(score)
			self.displa_screen = self.font.render(display_text, True, self.gold)
			self.display_screeny = self.font.render(display_txt, True, self.gold)
			self.display_scree = self.font.render(display_tet, True, self.gold) 
			window.blit(self.displa_screen, (50, 50))
			window.blit(self.display_screeny, (50, 100))
			window.blit(self.display_scree, (130, 200))
			pygame.display.update()
			pygame.mixer.Sound('./assets/womp.wav').play()
			while True:
				event = pygame.event.poll()
				print("event: ", event)
				if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
					return

			# prevent system hogging by sleeping momentarily
				time.sleep(1)
