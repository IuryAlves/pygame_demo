# -*- coding: utf-8 -*-

import sys
from __init__ import *
import pygame
from characters import Hero, Npc
from text import Text
from colors import *
from pygame.sprite import Sprite, RenderUpdates, LayeredUpdates
from pygame.constants import *

gravity = 1.2


def main():
    fundo, tela, clock = config()
    grupo = LayeredUpdates()
    personagem = Hero(20, 290,"elisa", grupo)

    teclas = {K_LEFT: False, K_RIGHT: False, K_UP: False, K_DOWN: False,
              K_RETURN: False, 27: False, K_a: False}  # obs 27 = tecla 'esc'

    fundo = fundo.convert()
    pygame.display.flip()
    while True:
        clock.tick(FPS)

        for e in pygame.event.get([KEYUP, KEYDOWN]):
            valor = (e.type == KEYDOWN)
            if e.key in teclas.keys():
                teclas[e.key] = valor

        if teclas[27]:  # tecla ESC
            pygame.quit()
            sys.exit()
        if personagem.attacking:
        	personagem.animate_attack()
        elif teclas[K_LEFT]:
            personagem.move("left")
        elif teclas[K_RIGHT]:
            personagem.move("right")
        elif teclas[K_UP]:
            personagem.jump()
        elif teclas[K_DOWN]:
            personagem.move("DOWN")
        elif teclas[K_a]:
        	personagem.attack()
        personagem.is_jumping(gravity)

        grupo.clear(tela, fundo)
        pygame.display.update(grupo.draw(tela))


if __name__ == '__main__':
    main()
