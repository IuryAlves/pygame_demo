# -*- coding: utf-8 -*-

import sys
from __init__ import *
import pygame
from characters import Hero, Npc
from tiles import Tile
from text import Text
from colors import *
from pygame.sprite import Sprite, RenderUpdates, LayeredUpdates
from pygame.constants import *


def main():
    fundo, tela, clock = config()
    musica = pygame.mixer.Sound("BGM/Firelink Shrine.wav")
    grupo = LayeredUpdates()
    tiles_group = LayeredUpdates()
    personagem = Hero(20, 290, "dante", grupo)

    lx = [b for b in range(-4, 76)]
    l1 = [-10]
    l2 = [6]

    parede = [x for x in range(-10, 16)]

    teclas = {K_LEFT: False, K_RIGHT: False, K_UP: False, K_DOWN: False,
              K_RETURN: False, 27: False}  # obs 27 = tecla 'esc'

    musica.play()
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

        #if {personagem.px, personagem.py} & set(parede):
        if teclas[K_LEFT]:
            personagem.move("LEFT")
        elif teclas[K_RIGHT]:
            personagem.move("RIGHT")
        elif teclas[K_UP]:
            personagem.move("UP")
        elif teclas[K_DOWN]:
            personagem.move("DOWN")

        print(personagem.px, personagem.py, parede)

        grupo.clear(tela, fundo)
        tiles_group.clear(tela, fundo)
        pygame.display.update(tiles_group.draw(tela))
        pygame.display.update(grupo.draw(tela))


if __name__ == '__main__':
    main()
