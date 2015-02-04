# coding: utf-8

import pygame
from colors import WHITE


class Text():

    '''
    Class to handle the texts in the game
    '''

    def __init__(self, size, dialog, font_file, color=WHITE, antialias=True):
        self.size = size  # size of the dialog
        self.dialog = dialog  # current dialog
        self.color = color
        self.antialias = antialias
        self.font = pygame.font.SysFont(font_file, self.size)
        self.phrases = self.font.render(
            self.dialog, self.antialias, self.color)

    def change_dialog(self, new_dialog):
        self.dialog = new_dialog

    def change_color(self, new_color):
        self.color = new_color

    def change_size(self, new_size):
        self.size = new_size
