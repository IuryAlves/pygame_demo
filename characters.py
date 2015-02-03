# -*- coding: utf-8 -*-

import pygame
import time
from pygame.locals import *
from pygame.sprite import Sprite
from colors import *

# All classes of the game are here


class Characters(Sprite):

    '''
    Base class for all characters of the game
    '''

    def __init__(self, start_px, start_py, image_name="elisa", *groups):
        Sprite.__init__(self, *groups)
        self.start_px = start_px
        self.start_py = start_py
        self.px = 0
        self.py = 0
        self.yVel = 0
        self.jumping = False
        self.attacking  = False
        self.actual_side = "RIGHT"
        self._attack_state = {"right": 0, "left": 0}
        self._move_states = {"right": 0, "left": 0}
        self.rect = Rect(self.start_px, self.start_py, 0, 0)
        self._base_image_path = "sprites/"
        self.image_name = image_name
        self.image = pygame.image.load(
            self._base_image_path + image_name + "_right_0.png")
        self.convert_image()
        pygame.draw.rect(self.image, BLACK, self)

    def jump(self):
        self.yVel = -15
        self.jumping = True

    def is_jumping(self, gravity):
        return
        if self.jumping:
            print self.py

            self.yVel += gravity
            self.py += self.yVel
            self.rect.move_ip(self.px, self.py)
            if self.yVel < 0:
                self.py -= self.yVel
                if self.py > 50:
                    self.py = 0
                    self.jumping = False
                # if self.py <= 0:
                #     self.jumping = False
            #     if self.py <= -15:
            #         self.jumping = False

    def move(self, side):
        '''
        move the character
        '''
        self.actual_side = side
        side_state = str(self._move_states[side] + 1)
        image = "%s%s_%s_%s.png" %(self._base_image_path, self.image_name, self.actual_side, side_state)

        self.image = pygame.image.load(image)

        time.sleep(0.075)
        self._change_state(side)

    def attack(self):
    	self.attacking = True

    def animate_attack(self):
    	self._attack_state[self.actual_side] +=1
    	image = "%s%s_attack_%s_%s.png" %(self._base_image_path, self.image_name, self.actual_side, self._attack_state[self.actual_side])
    	self.image = pygame.image.load(image)
    	self.convert_image()
    	if self._attack_state[self.actual_side] == 5:
    		self._attack_state[self.actual_side] = 0
    		self.attacking = False
    		self.image = pygame.image.load("%s%s_%s_%s.png" %(self._base_image_path, self.image_name, self.actual_side, 0))
    		self.convert_image()

    def _change_state(self, side):
        '''
        change the position of the character in the screen
        '''
        self.convert_image()
        if side == 'left':
            x, y = -10, 0
        if side == 'right':
            x, y = 10, 0
        if side == 'DOWN':
            x, y = 0, 10
        self.rect.move_ip(x, y)
        self.px += x
        self.py += y

        self._move_states[side] += 1
        if self._move_states[side] == 8:
            self._move_states[side] = 0

    def convert_image(self):
        '''
        Convert the character image and set colorkey to magenta(i.e pynk)
        '''
        self.image.set_alpha(None, RLEACCEL)
        self.image.convert()
        self.image.set_colorkey(MAGENTA, RLEACCEL)


class Hero(Characters):

    '''
    Class for the heroes of the game
    '''

    def __init__(self, start_px, start_py, image_name, *groups):
        Characters.__init__(self, start_px, start_py, image_name, *groups)


class Npc(Characters):

    '''
    Class for all the npcs of the game
    npcs = all characters that you can interact
    '''

    def __init__(self, start_px, start_py, image_name, *groups):
        Characters.__init__(self, start_px, start_py, *groups)
