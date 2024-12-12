import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))
screen.fill((255,255,255))

color1=(0,122,43)
color2=(0,180,11)

pygame.draw.circle(screen, color1, (250,250), 40)
pygame.draw.circle(screen, color2, (100, 100), 20, 3)

pygame.display.update()

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

pygame.quit()