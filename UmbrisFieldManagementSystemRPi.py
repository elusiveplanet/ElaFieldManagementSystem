import random, os.path
import sys
import time
import pygame
import pygame.camera
import pygame.image
from pygame.locals import *

import RPi.GPIO as GPIO

# GridWorld.init() == True
# This is what the hypothetical grid layout looks like. Its a 3x4.
    # A1 :: B1 :: C1 :: D1
    # A2 :: B2 :: C2 :: D2
    # A3 :: B3 :: C3 :: D3
    # A4 :: B4 :: C4 :: D4
# Use the gridVariables below to generate centered/aligned assets.
# To center text, use the following call with the following definitions.
    # Let xLoc be the location of the xGrid
    # Let yLoc be the location of the yGrid
    # All others are defined already.
    # location = (gridCentX + (gridX * xLoc) - (lesScoreText.get_width() / 2), gridCentY + (gridY * yLoc) - (lesScoreText.get_height() / 2))


# List of nessecary pins
# 
# centerStack 4x out
# buttonsField 2x in
# buttonsAlooksis 5x in
# lightControllers
#   -field lights 1x out
#   -el strips 2x out
#   -button lights ~x out

# Variables you might want to change.
init = True
sleepInterval = 1.0/60.0
dFontSize = 100

centerStackRed = 2
centerStackYellow = 3
centerStackGreen = 4
centerStackBuzzer = 14

state = 1

# End of variables you might want to change.

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(centerStackRed, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(centerStackYellow, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(centerStackGreen, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(centerStackBuzzer, GPIO.OUT, initial=GPIO.LOW)

pygame.init()
pygame.camera.init()
importantThings = pygame.display.Info()

size = (importantThings.current_w, importantThings.current_h)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
dFont = pygame.font.SysFont("monospace", dFontSize)
WHITE = (0,0,0)

gridX = importantThings.current_w / 4
gridY = importantThings.current_h / 3
gridCentX = gridX / 2
gridCentY = gridY / 2

lesScoreImg = pygame.image.load(os.path.join('data', 'lesScoreImg.fw.png'))
aurScoreImg = pygame.image.load(os.path.join('data', 'aurScoreImg.fw.png'))

lesScoreImg = pygame.transform.scale(lesScoreImg, ((gridX, gridY)))
aurScoreImg = pygame.transform.scale(aurScoreImg, ((gridX, gridY)))

# Alexis' best advice
# Well there's one thing to know about this earth: We were put here just to make more dirt, and that's okay.
# We treat mishaps like sinking ships and I know that I don't want to be out to drift.
# The past is gone. Stop dwelling on what you could have done.
# No rest for the weary.
#
# Alexis' worst advice
# Quit your job.
# Do it, you'll be just fine.

leasathScore = 0
aureliaScore = 0

# Sourcetree whyyyyyyyyyyyyyyyyyyyyyyyyyyy

def getMatchStartButton():
    return 0
def getMatchResetSwitch():
    return 0
def getLesFieldButton():
    return 0
def getAurFieldButton():
    return 0
def updateLesFieldButton():
    return 0
def updateAurFieldButton():
    return 0
def getLesPosButton():
    return 0
def getLesNegButton():
    return 0
def getAurPosButton():
    return 0
def getAurNegButton():
    return 0
    
    
 # Begin Center Stack Method Defs
def special():
	return 0
def red():
	GPIO.output(centerStackRed, GPIO.HIGH)
def yellow():
	GPIO.output(centerStackYellow, GPIO.HIGH)
def green():
	GPIO.output(centerStackGreen, GPIO.HIGH)
def buzzerDef():
	GPIO.output(centerStackBuzzer, GPIO.HIGH)
def redOsc():
	GPIO.output(centerStackRed, GPIO.HIGH)
def yellowOsc():
	GPIO.output(centerStackYellow, GPIO.HIGH)
def greenOsc():
	GPIO.output(centerStackGreen, GPIO.HIGH)
def preGame():
	yellowOsc()
    green()
def lowTide():
	yellowOsc()
    green()
def gameOver():
	red()
    greenOsc()
def gameProg():
    green()
    
updateCenterStack = {0 : special,
					1 : red,
					2 : yellow,
					3 : green,
					4 : buzzerDef,
					5 : redOsc,
					6 : yellowOsc,
					7 : greenOsc,
					8 : preGame,
					9 : lowTide,
					10: gameOver,
                    11: gameProg,
}
	

def updateScore():
    # This outputs the scoreTextCentered and displays it.
    lesScoreText = dFont.render(str(leasathScore), 1, (0,0,0))
    lesTloc = (gridCentX + (gridX * 0) - (lesScoreText.get_width() / 2), gridCentY  + (gridY * 2) - (lesScoreText.get_height() / 2))
    aurScoreText = dFont.render(str(aureliaScore), 1, (0,0,0))
    aurTloc = (gridCentX + (gridX * 3) - (aurScoreText.get_width() / 2), gridCentY + (gridY * 2) - (aurScoreText.get_height() / 2))
    screen.blit(lesScoreImg, (0, gridY * 2))
    screen.blit(aurScoreImg, (gridX * 3, gridY * 2))
    screen.blit(lesScoreText, lesTloc)
    screen.blit(aurScoreText, aurTloc)

# GPIO.add_event_detect(23, GPIO.RISING, callback = getMatchStartButton, bouncetime = 300)

while init:
    #This is the setup call for the game. Called once.
     cam_list = pygame.camera.list_cameras()
     print "Using camera %s ..." % cam_list[0]
     webcam = pygame.camera.Camera(cam_list[0], (640, 480))
     webcam.start()
     init = False

while True:
    # This is the periodic call for the game. Called many times.
    for event in pygame.event.get():
        if event.type == QUIT:
			PIO.output(25, GPIO.LOW)
			GPIO.output(23, GPIO.LOW)
			GPIO.output(24, GPIO.LOW)
			webcam.stop()
			pygame.quit()
			GPIO.cleanup()
			sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
				GPIO.output(25, GPIO.LOW)
				GPIO.output(23, GPIO.LOW)
				GPIO.output(24, GPIO.LOW)
				webcam.stop()
				pygame.quit()
				GPIO.cleanup()
				sys.exit()
                
    screen.fill(WHITE)
    imagen = webcam.get_image()
    imagen = pygame.transform.scale(imagen,(importantThings.current_w,importantThings.current_h))
    screen.blit(imagen,(0,0))

    updateCenterStack[state]()

    updateScore()

    leasathScore += 1
    aureliaScore += 2

    pygame.display.flip()
    time.sleep(sleepInterval)
