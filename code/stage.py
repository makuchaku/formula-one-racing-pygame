from game import *
import pygame
import time


class Stage:
	def game_start(self, window):
		
		self.gold = (3, 11, 255)
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
			window.fill("light blue")
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




	def game_over(self, window, a_score, some_leaderboard):
		self.gold = (255, 215, 0)
		self.font = pygame.font.Font('./assets/pixelify.ttf', 50)
		window.fill("light blue")

		while True:

			display_text = str("GAME OVER!! ")
			display_txt = str("Your score is: ")
			display_tet = str(a_score)
			display_of_tet = str("Leaderboard:")

			self.displa_screen = self.font.render(display_text, True, self.gold)
			self.display_screeny = self.font.render(display_txt, True, self.gold)
			self.display_scree = self.font.render(display_tet, True, self.gold) 
			self.a_disp = self.font.render(display_of_tet, True, self.gold)
			# self.a_leader = self.font.render(leader, True, self.gold)

			window.blit(self.displa_screen, (50, 50))
			window.blit(self.display_screeny, (50, 100))
			window.blit(self.display_scree, (400, 100))
			window.blit(self.a_disp, (50, 150))
			# window.blit(('1st:', int(some_leaderboard[0])), 50, 200)
			# window.blit(('2nd:', int(some_leaderboard[1])), 50, 250)
			# window.blit(('3rd:', int(some_leaderboard[2])), 50, 300)
			counter = 0
			for key, value in some_leaderboard.items():
				if counter == 3:
					break
				leader = str(str(counter) +'-'+ str(key) + ':'+ str(value))
				self.a_leader = self.font.render(leader, True, self.gold)

				window.blit(self.a_leader, (50, counter*50+200))
				counter += 1


			pygame.display.update()
			pygame.mixer.Sound('./assets/womp.wav').play()


			running = True
			while running:
				event = pygame.event.poll()
				if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
					running = False
					return

			# prevent system hogging by sleeping momentarily
				time.sleep(1)
