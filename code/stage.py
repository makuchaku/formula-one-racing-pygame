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

		# exit_img = pygame.image.load('./assets/exit_btn.png').convert_alpha()
		# button = Button(100, 800, exit_img, 0.8)
		# run = False
		# while not run:
		# 	run = button.draw(window)

		while True:
			event = pygame.event.poll()
			print("event: ", event)
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
				return

			# prevent system hogging by sleeping momentarily
			time.sleep(1)



class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action