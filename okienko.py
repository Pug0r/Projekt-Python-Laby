import pygame
import sys

niebieski = (140, 219, 237)
fioletowy = (172, 105, 179)
rozowy = (240, 93, 176)
zielony = (160, 247, 148)

black = (0, 0, 0)
white = (255, 255, 255)

colors = [niebieski, fioletowy, rozowy, zielony]

def main():
    pygame.init()
    # logo = pygame.image.load("")
    # pygame. display.set_icon(logo) # to gdybysmy mieli jakies logo to mozna je tak dodac chyba
    pygame.display.set_caption("gierka") # nazwa aplikacji jaka sie wyswietla

    #font = pygame.font.Font('freesansbold.ttf', 32)
    #textsurface = font.render('pls', False, (0, 0, 0))

    window = pygame.display.set_mode((1200,1000))
    
    rect1 = pygame.Rect(10, 20, 30, 30)
    rect2 = pygame.Rect(10, 60, 30, 30)
    rect3 = pygame.Rect(10, 100, 30, 30)

    #tekst = font.render('to jest gierka', True, black, white)
    #tekstRect=tekst.get_rect()
    #tekstRect.center = (600, 500) 
    #tekstRect.blit(tekst, black) # to nie dziala

    def colorchange():
    	window.fill(colors[0])
    	pygame.draw.rect(window, colors[1], rect1)
    	pygame.draw.rect(window, colors[2], rect2)
    	pygame.draw.rect(window, colors[3], rect3)

    colorchange() 
    pygame.display.update()
    running = True
    mouse_pressed = False # zmienna na nacisnieta myszke
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True
                if rect3.collidepoint(pygame.mouse.get_pos()):
                    colors[0], colors[3] = colors[3], colors[0]
                    colorchange()
                    pygame.display.flip()	
                if rect1.collidepoint(pygame.mouse.get_pos()):
                    colors[0], colors[1] = colors[1], colors[0]
                    colorchange()
                    pygame.display.flip()
                if rect2.collidepoint(pygame.mouse.get_pos()):
                    colors[0], colors[2] = colors[2], colors[0]
                    colorchange()
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: 
                    running = False # tu mozna zaprogramowac co sie odpala jak sie wcisnie enter
                
    

if __name__=="__main__":
    main()
    pygame.quit()



    
