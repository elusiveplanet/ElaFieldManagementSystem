import random, os.path
import sys, pygame

size = width, height = 720, 480
speed = [2,2]
black  = 0, 0, 0

screen = pygame.display.set_mode(size)

scoreBoard = pygame.image.load("data\\ScoreBack.png")

boardRect = scoreBoard.get_rect()

def main(winstyle = 0):
	pygame.init()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	boardRect = boardRect.move(speed)

	screen.fill(black)