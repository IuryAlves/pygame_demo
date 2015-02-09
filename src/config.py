# -*- coding: utf-8 -*-

import pygame
import yaml
import pytmx
import utils
from pygame.locals import *

#
# Module that contains the configuration of the game
#

__all__ = ["set_config"]


def load_game_config_file(file_name):
    with open(file_name, "r") as game_config:
        return yaml.load(game_config)


def _get_game_config_file():
    return load_game_config_file("src/game_config.yml")


def create_rects_from_tile_objects(layer):
    rect_list = []
    for obj in layer:
        rect_list.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
    return rect_list


def set_config():
    pygame.init()
    game_config = _get_game_config_file()

    screen = pygame.display.set_mode(
        (game_config["screen_size_x"], game_config["screen_size_y"]))
    pygame.display.set_caption(game_config["name"])
    clock = pygame.time.Clock()
    level = pytmx.load_pygame(game_config["initial_game_level"])

    objects_layer = filter(
        lambda layer:
            isinstance(layer, pytmx.TiledObjectGroup), level.layers).pop()
    rect_list = create_rects_from_tile_objects(objects_layer)

    utils.clear_screen(level, screen)
    return level, screen, clock, game_config["fps"], rect_list
