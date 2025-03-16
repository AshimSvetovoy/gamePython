import pygame
pygame.init
#pygame.display.set_mode((800, 600))

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

rect_x = 350
rect_y = 250
rect_width = 100
rect_height = 100

red = (255, 0, 0)

pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

pygame.display.update()

pygame.time.Clock().tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
   
