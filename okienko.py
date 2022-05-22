import pygame
import sys

niebieski = (140, 219, 237)
fioletowy = (172, 105, 179)
rozowy = (240, 93, 176)

colors = [niebieski, fioletowy, rozowy]

def main():
    pygame.init()
    # logo = pygame.image.load("")
    # pygame. display.set_icon(logo) # to gdybysmy mieli jakies logo to mozna je tak dodac chyba
    pygame.display.set_caption("podpis") # nazwa aplikacji jaka sie wyswietla


    window = pygame.display.set_mode((1200,1000))
    
    rect1 = pygame.Rect(10, 20, 30, 30)
    rect2 = pygame.Rect(10, 60, 30, 30)
        
    def colorchange():
    	window.fill(colors[0])
    	pygame.draw.rect(window, colors[1], rect1)
    	pygame.draw.rect(window, colors[2], rect2)

    colorchange() 
    pygame.display.flip()
    running = True
    mouse_pressed = False # zmienna na nacisnieta myszke
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True
                if rect1.collidepoint(pygame.mouse.get_pos()):
                    colors[0], colors[1] = colors[1], colors[0]
                    colorchange()
                    pygame.display.flip()
                if rect2.collidepoint(pygame.mouse.get_pos()):
                    colors[0], colors[2] = colors[2], colors[0]
                    colorchange()
                    pygame.display.flip()


if __name__=="__main__":
    main()
    pygame.quit()



    
