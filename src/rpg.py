# -*- coding: utf-8 -*-

import sys
import pygame
import utils
from config import set_config
from characters import Hero
from text import Text
from colors import *
from pygame.sprite import Sprite, RenderUpdates
from pygame.constants import *
from pytmx import TiledObjectGroup
gravity = 1.2

def main():
    level, screen, clock, fps, rect = set_and_get_config()
    group = RenderUpdates()
    heroine = Hero(30, 30, group)

    keys = {K_LEFT: False, K_RIGHT: False, K_UP: False, K_DOWN: False,
              K_RETURN: False, 27: False, K_a: False}  # obs 27 = 'esc'

    pygame.display.flip()
    printou = False
    while True:
        clock.tick(fps)
        #print heroine.rect.x
        for e in pygame.event.get([KEYUP, KEYDOWN]):
            valor = (e.type == KEYDOWN)
            if e.key in keys.keys():
                keys[e.key] = valor
        for layer in level.layers:
        	if isinstance(layer, TiledObjectGroup):
		        for obj in layer:
		        	if heroine.rect.colliderect(rect):
		        		print "colidiu"
        		#heroine.fsm.set_state("move")

        if keys[27]:  # tecla ESC
            pygame.quit()
            sys.exit()
        elif keys[K_LEFT]:
            heroine.fsm.set_state("move")
            heroine.fsm.update("left")
        elif keys[K_RIGHT]:
            heroine.fsm.set_state("move")
            heroine.fsm.update("right")
        elif keys[K_UP]:
            heroine.fsm.set_state("jump")
        elif keys[K_DOWN]:
            heroine.fsm.set_state("get_down")
        elif keys[K_a]:
            heroine.fsm.set_state("attack")
        heroine.fsm.auto_update()
        utils.clear_screen(level, screen)
        pygame.display.update(group.draw(screen))


if __name__ == '__main__':
	main()
