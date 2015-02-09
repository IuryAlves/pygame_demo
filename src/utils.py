# coding: utf-8


import pytmx
import pygame
def clear_screen(level, screen):
	for layer in level.layers:
		if not isinstance(layer, pytmx.TiledObjectGroup):
			for x, y, image in layer.tiles():
				screen.blit(image, (x * level.tilewidth, y * level.tileheight))

