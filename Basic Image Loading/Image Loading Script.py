import pygame
pygame.init()       #basic setup

myFont = pygame.font.SysFont('Comic Sans MS',30)
white = (255, 255, 255)
imgOfMe = pygame.image.load('loadedImage.jpg')
screen = pygame.display.set_mode((1600,900)) #defining variables

screen.fill((white))
screen.blit(imgOfMe,(0,0))
pygame.display.flip()

pygame.display.set_caption('me as beby')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #closing sequence
            running = False
