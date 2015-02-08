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


def load_game_config_file(file_name):
    with open(file_name, "r") as game_config:
        return yaml.load(game_config)


def _init():
    return load_game_config_file("src/game_config.yml")


def create_rects_from_tile_objects(layer):
	rect_list = []
	for obj in layer:
		rect_list.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
	return rect_list


def set_and_get_config():
    pygame.init()
    game_config = _init()

    screen = pygame.display.set_mode((game_config["screen_size_x"], game_config["screen_size_y"]))
    pygame.display.set_caption(game_config["name"])
    clock = pygame.time.Clock()
    level = pytmx.load_pygame(game_config["initial_game_level"])
    rect_list = create_rects_from_tile_objects(object_layer)

    #import pdb; pdb.set_trace()
    rect = utils.clear_screen(level, screen)
    return level, screen, clock, game_config["fps"], rect_list
