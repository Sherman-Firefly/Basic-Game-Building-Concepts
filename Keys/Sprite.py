import pygame

pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill((255,255,255))
colors={'Blue': pygame.color('Blue'),'Red': pygame.color('Red'), 'Yellow': pygame.color('Yellow') }
done=False
is_blue=True

x=60
y=60

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN or event.type==pygame.K_SPACE:
            is_blue= not is_blue

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:y+=3
    if pressed[pygame.K_DOWN]:y-=3
    if pressed[pygame.K_LEFT]:x-=3
    if pressed[pygame.K_RIGHT]:x-=3

    x= min(max(0,x), screen_width-sprite_width)
    y= min(max(0,y), screen_height-sprite_height)
    
    

    if is_blue:
        color=(0,128,225)
    else:
        color=(255,255,255)
    pygame.draw.rect(screen,color, pygame.Rect(x,y,60,60))
pygame.display.flip()



