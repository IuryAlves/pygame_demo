# -*- coding: utf-8 -*-

import pygame
import yaml
import pytmx
import utils
from pygame.locals import *
from pygame.sprite import RenderUpdates

#
# Module that contains the configuration of the game
#

__all__ = ["set_config"]


def _load_game_config_file(file_name):
	with open(file_name, "r") as game_config:
		return yaml.load(game_config)


def _init():
	return _load_game_config_file("src/game_config.yml")


def set_config():
    pygame.init()
    game_config = _init()    

    screen = pygame.display.set_mode((game_config["screen_size_x"], game_config["screen_size_y"]))
    pygame.display.set_caption(game_config["name"])
    clock = pygame.time.Clock()
    level = pytmx.load_pygame(game_config["initial_game_level"])
    tw = level.tilewidth
    th = level.tileheight

    utils.clear_screen(level, screen)
    return level, screen, clock, game_config["fps"]
