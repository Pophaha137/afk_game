import pygame
import os
import sys
from pygame.locals import *


def get_path():
    return os.getcwd()


class Button(object):
    NORMAL = 0
    MOVE = 1
    DOWN = 2

    def __init__(self, x, y, w, h, func_img, callBackFunc, text=None, font_size=None, color=None):
        self.cwd = get_path()
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.status = Button.NORMAL
        self.callBackFunc = callBackFunc

        self.bg_n = pygame.transform.scale(pygame.image.load(f"{self.cwd}/resource/brown/brown_n.png"),
                                           (self.width, self.height))
        self.bg_m = pygame.transform.scale(pygame.image.load(f"{self.cwd}/resource/brown/brown_m.png"),
                                           (self.width, self.height))
        self.bg_r = pygame.transform.scale(pygame.image.load(f"{self.cwd}/resource/brown/brown_d.png"),
                                           (self.width, self.height))

        self.func_img = pygame.transform.scale(pygame.image.load(f"{self.cwd}/resource/function/{func_img}.png"),
                                               (self.width / 2, self.height / 2))
        # 背景图片存入数组
        self.imgs = []
        self.imgs.append(self.bg_n)
        self.imgs.append(self.bg_m)
        self.imgs.append(self.bg_r)
        for i in range(2, 0, -1):
            if not self.imgs[i]:
                self.imgs[i] = self.imgs[i - 1]

        # 判断是否有文字
        if (text != None and font_size != None):
            self.font = pygame.font.Font(f"{self.cwd}/resource/VonwaonBitmap-12px.ttf", font_size)
            self.text = self.font.render(text, True, color)
            self.font_size = font_size
            self.font_color = color
        else:
            self.font = None
            self.text = None
            self.font_size = None
            self.font_color = None

    def colli(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        else:
            return False

    def getFocus(self, x, y):
        if self.status == Button.DOWN:
            return
        if self.colli(x, y):
            self.status = Button.MOVE
        else:
            self.status = Button.NORMAL

    def mouseDown(self, x, y):
        if self.colli(x, y):
            self.status = Button.DOWN

    def mouseUp(self, x, y):
        if self.colli(x, y):
            self.status = Button.MOVE
            if self.callBackFunc:
                surface = pygame.display.get_surface()
                return self.callBackFunc()
        else:
            self.status = Button.NORMAL
            return

    def draw(self, surface):
        dx = (self.width / 2) - (self.width / 4)
        dy = (self.height / 2) - (self.height / 4)

        if self.imgs[self.status]:
            surface.blit(self.imgs[self.status], [self.x, self.y])
        surface.blit(self.func_img, [self.x + dx, self.y + dy])