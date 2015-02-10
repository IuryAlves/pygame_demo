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
    colided_list = []
    level, screen, clock, fps, rect_list = set_config()
    group = RenderUpdates()
    heroine = Hero(30, 30, group)

    keys = {K_LEFT: False, K_RIGHT: False, K_UP: False, K_DOWN: False,
            K_RETURN: False, 27: False, K_a: False}  # obs 27 = 'esc'

    pygame.display.flip()

    while True:
        clock.tick(fps)
        for event in pygame.event.get([KEYUP, KEYDOWN]):
            value = (event.type == KEYDOWN)
            if event.key in keys:
                keys[event.key] = value

        idx = heroine.rect.collidelist(rect_list)
        if idx != -1 and rect_list[idx] not in colided_list:
            colided_list.append(rect_list[idx])
            print rect_list[idx]
            if rect_list[idx].x <= heroine.rect.x and heroine.rect.x <= rect_list[idx].width:
                heroine.fsm.set_state("stand_still")
                heroine.cannot_move_to = None
                #import pdb; pdb.set_trace()
            else:
                heroine.cannot_move_to = heroine.fsm.side
        if idx == -1:
            heroine.fsm.set_state("fall")

        if keys[27]:  # tecla ESC
            pygame.quit()
            sys.exit()
        elif keys[K_LEFT] and heroine.cannot_move_to != "left":
            heroine.fsm.set_state("move")
            heroine.fsm.update("left")
        elif keys[K_RIGHT] and heroine.cannot_move_to != "right":
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
