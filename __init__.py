# -*- coding: utf-8 -*-

import pygame
import yaml
from pygame.locals import *
from pygame.sprite import RenderUpdates

#
# Module that contains the configuration of the game
#

__all__ = ["config", "get_tiles_quantity", "FPS"]


# private methods
def _load_game_config_file(file_name):
	with open(file_name, "r") as game_config:
		return yaml.load(game_config)

# private variables
_game_config_dict = _load_game_config_file("game_config.yml")
_SCREEN_SIZE = (_game_config_dict["screen_size_x"], _game_config_dict["screen_size_y"])
_NAME = _game_config_dict["name"]
_INITIAL_GAME_IMAGE = _game_config_dict["initial_game_image"]

# public variables
FPS = _game_config_dict["fps"]

# public methods
def config():
    pygame.init()
    pygame.font.init()
    c_screen = pygame.display.set_mode(_SCREEN_SIZE)
    pygame.display.set_caption(_NAME)
    c_clock = pygame.time.Clock()
    c_background = pygame.image.load(_INITIAL_GAME_IMAGE)
    c_screen.blit(c_background, (0, 0))
    return c_background, c_screen, c_clock

def _calculate_tiles_quantity(screen_size):
	tile_area = _game_config_dict["tile_area"]
	tile = tile_area * tile_area
	quantity = screen_size[0] / tile
	quantity *= (screen_size[1] / tile)

	return quantity

def get_tiles_quantity():
	return _calculate_tiles_quantity(_SCREEN_SIZE)

