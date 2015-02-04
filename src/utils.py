# coding: utf-8

def clear_screen(background,  screen):
	for layer in background.visible_layers:
		for x, y, image in layer.tiles():
			screen.blit(image, (x * background.tilewidth, y * background.tileheight))