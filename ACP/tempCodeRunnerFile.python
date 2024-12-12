import pygame

pygame.init()

white = (255, 255, 255)

clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Display Text in Pygame")

display_surface.fill(white)

font = pygame.font.Font(None, 36) 
text = font.render("Hello, Pygame", True, (0, 0, 0))  
text_rect = text.get_rect(center=(500 // 2, 30)) 

rect_width, rect_height = 60, 60
rect_x = (500 - rect_width) // 2  
rect_y = (500 - rect_height) // 2  

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display_surface.fill(white)

    display_surface.blit(text, text_rect)

    pygame.draw.rect(display_surface, (0, 125, 255), pygame.Rect(rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
