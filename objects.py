import pygame
from constants import *

class Point:
    def __init__(self, x, y, size, image):
        self.x = x
        self.y = y
        self.size = size
        self.image = pygame.transform.scale(image,(GRID_SIZE, GRID_SIZE))
    def left(self):
        self.x -= GRID_SIZE
    def right(self):
        self.x += GRID_SIZE
    def up(self):
        self.y -= GRID_SIZE
    def down(self):
        self.y += GRID_SIZE
    
class Cupboard:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image,(GRID_SIZE, GRID_SIZE))
        self.coins = 1
    def interact(self, player_y, player_x):
        if self.y == player_y and self.x == player_x:
            image = pygame.image.load("./tiles/cupboard_open_tile.png")
            self.image = pygame.transform.scale(image,(GRID_SIZE, GRID_SIZE))
            add_coins = self.coins
            self.coins = 0
            return add_coins


class TextBox:
    def __init__(self):
        self.x = WIDTH//1.5
        self.y = HEIGHT
        self.rect = pygame.Rect(WIDTH//1.5, 0, self.x, self.y)
        self.text = ""
        self.__font = pygame.font.Font(None, 32)
        self.__offset = 5
        self.fontx = self.x + self.__offset
        self.fonty = self.__offset
        self.text_surface = self.__font.render(self.text, True, WHITE)
        self.active = False
    def add_char(self, _char):
        if _char == '\n':
            self.text += '\n'
        else:
            self.text += _char
    def del_char(self):
        if len(self.text) > 0:
            self.text = self.text[:-1]
    def refresh_text(self):
        self.text_surface = self.__font.render(">>> " + self.text, True, WHITE)
    def flush_text(self):
        if self.text != command_history[-1]:
            command_history.append(self.text)
        command_index = 0
        self.text = ""

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(surf,(GRID_SIZE,GRID_SIZE))
        self.rect = self.image.get_rect(topleft = pos)
