import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

# I love testing things!
#
# rip alooksis

#create fullscreen display 640x480
importantThings = pygame.display.Info()

size = (importantThings.current_w, importantThings.current_h)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0])
webcam.start()

while True:
    #grab image, scale and blit to screen
    imagen = webcam.get_image(screen)

    #draw all updates to display
    pygame.display.update()

    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            webcam.stop()
            pygame.quit()
            sys.exit()