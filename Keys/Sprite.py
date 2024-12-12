import pygame

pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill((255,255,255))

colors={'Blue': pygame.Color('Blue'),'Red': pygame.Color('Red'), 'Yellow': pygame.Color('Yellow') }
done=False
color_key= 'Blue'

x, y = 60, 60
sprite_width, sprite_height = 60, 60
screen_width, screen_height = 500, 500

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN or event.type==pygame.K_SPACE:
            if event.key == pygame.K_SPACE:  
                if color_key == 'Blue':
                    color_key = 'Red'
                elif color_key == 'Red':
                    color_key = 'Yellow'
                else:
                    color_key = 'Blue'

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:y-=3
    if pressed[pygame.K_DOWN]:y+=3
    if pressed[pygame.K_LEFT]:x-=3
    if pressed[pygame.K_RIGHT]:x+=3

    x= min(max(0,x), screen_width-sprite_width)
    y= min(max(0,y), screen_height-sprite_height)
    
    
    screen.fill((255, 255, 255))

    
    color = colors[color_key]

    
    pygame.draw.rect(screen, color, pygame.Rect(x, y, sprite_width, sprite_height))

  
    pygame.display.flip()


