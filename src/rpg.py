# -*- coding: utf-8 -*-

import sys
import pygame
import utils
from config import set_config
from characters import Hero
from colors import *
from pygame.sprite import RenderUpdates
from pygame.constants import *


def main():
    level, screen, clock, fps, rect_list = set_config()
    group = RenderUpdates()
    heroine = Hero(30, 30, group)

    keys = {K_LEFT: False, K_RIGHT: False, K_UP: False, K_DOWN: False,
            K_RETURN: False, 27: False, K_a: False}  # obs 27 = 'esc'

    pygame.display.flip()

    while True:
        clock.tick(fps)
        for e in pygame.event.get([KEYUP, KEYDOWN]):
            valor = (e.type == KEYDOWN)
            if e.key in keys.keys():
                keys[e.key] = valor

        idx = heroine.rect.collidelist(rect_list)
        if idx != -1:
            if heroine.fsm.get_state() == 'fall':
                heroine.fsm.set_state("stand_still")

            else:
                heroine.cannot_move_to = heroine.fsm.side
        else:
            heroine.cannot_move_to = None

        if keys[27]:  # tecla ESC
            pygame.quit()
            sys.exit()
        elif keys[K_LEFT] and heroine.cannot_move_to != "left":
            heroine.fsm.set_state("move")
            heroine.fsm.update("left")
        elif keys[K_RIGHT] and heroine.cannot_move_to != "right":
            print "aqui"
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
