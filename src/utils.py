# coding: utf-8
from pytmx import *
import pygame
def clear_screen(level,  screen):
	for layer in level.layers:
		if isinstance(layer, TiledObjectGroup):
			rects = get_tile_objects
			for obj in layer:
				rect = pygame.draw.rect(screen, (255,0,255),(obj.x, obj.y, obj.width, obj.height), 3)
		else:
			for x, y, image in layer.tiles():
				screen.blit(image, (x * level.tilewidth, y * level.tileheight))
	return  rect

def get_tile_objects(level):
	pass

def create_rects_from_tile_objects(layer):
	rect_list = []
	for obj in layer:
		rect_list.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
	return rect_list
