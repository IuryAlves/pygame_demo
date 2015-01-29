# coding: utf-8 

from colors import BLACK, MAGENTA
from pygame.sprite import Sprite
from pygame import Rect
from pygame.constants import RLEACCEL
import pygame

class Tile(Sprite):

	def __init__(self, x, y, image, *groups):
		Sprite.__init__(self,  *groups)
		self.px = x
		self.py = y
		self.rect = Rect(self.px, self.py, 0, 0)
		self.image = pygame.image.load("tilesets/" + image)
		self.convert_image()
		pygame.draw.rect(self.image, BLACK, self)

	def convert_image(self):
	  '''
	  Convert the character image and set colorkey to magenta(i.e pynk)
	  '''
	  self.image.set_alpha(None, RLEACCEL)
	  self.image.convert()
	  self.image.set_colorkey(MAGENTA, RLEACCEL)
