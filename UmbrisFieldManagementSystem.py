import random, os.path
import sys
import pygame
from pygame.locals import *

size = width, height = 720, 480
speed = [2,2]
black  = 0, 0, 0

# Sourcetree whyyyyyyyyyyyyyyyyyyyyyyyyyyy

screen = pygame.display.set_mode(size)

scoreBoard = pygame.image.load("data\\ScoreBack.png")

boardRect = scoreBoard.get_rect()

pygame.font.init()

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)

def main(winstyle = 0):
	pygame.init()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
