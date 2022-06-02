from pickletools import read_unicodestring1
import pygame
import pygame.freetype
import sys

niebieski = (140, 219, 237)
fioletowy = (172, 105, 179)
rozowy = (240, 93, 176)
zielony = (160, 247, 148)

black = (0, 0, 0)
white = (255, 255, 255)

colors = [niebieski, fioletowy, rozowy, zielony]

pygame.init()
font = pygame.font.SysFont('kalapi.ttf', 32, bold=False, italic=False) # font taki najzwyklejszy
font2 = pygame.font.SysFont('tlwgtypo.ttf', 45, bold=False, italic=False)
#font3 = pygame.freetype.SysFont(pygame.freetype.get_default_font(), 32, bold = True, italic = False)



def main():
    
    #logo = pygame.image.load("logo.jpg")
    #pygame. display.set_icon(logo) # to gdybysmy mieli jakies logo to mozna je tak dodac chyba
    pygame.display.set_caption("gierka") # nazwa aplikacji jaka sie wyswietla
    pygame.font.init()

    tekst = font.render('wciśnij enter aby rozpocząć', True, black) # tekst na poczatku

    window = pygame.display.set_mode((1200,1000))

    def draw_rect(miejsce, color):
        rect = pygame.Rect(miejsce)
        pygame.draw.rect(window, color, rect)

    rect1 = pygame.Rect(10, 20, 30, 30)
    #draw_rect((10, 20, 30, 30), colors[1])
    rect2 = pygame.Rect(10, 60, 30, 30)
    rect3 = pygame.Rect(10, 100, 30, 30)

    events = pygame.event.get()
   

    def colorchange():
        window.fill(colors[0])
        pygame.draw.rect(window, colors[1], rect1)
        pygame.draw.rect(window, colors[2], rect2)
        pygame.draw.rect(window, colors[3], rect3)
        window.blit(tekst, (470, 930))
    

    colorchange()
    pygame.display.update()
    running = True
    mouse_pressed = False # zmienna na nacisnieta myszke

    def jezyki():

        #def polski():
            #window.fill(colors[0]) # czemu to nie chceeee
            #pygame.display.update()

        #def angielski():
            #pass

        wybor_jezyka = True
        nonlocal window, running
        window.fill(colors[0])
        wybierz_jezyk = font2.render('wybierz język', True, black)
        jezyk_1 = pygame.Rect(350, 400, 500, 100)
        jezyk_2 = pygame.Rect(350, 550, 500, 100)
        polski_text = font2.render('polski', True, black)
        angielski_text = font2.render('angielski', True, black)
        
        start_t = font.render('start', True, black)
        pygame.draw.rect(window, white, jezyk_1)
        pygame.draw.rect(window, white, jezyk_2)
        window.blit(wybierz_jezyk, (500, 350))
        window.blit(polski_text, (550, 435))
        window.blit(angielski_text, (540, 585))
        pygame.display.update()
        
        while wybor_jezyka == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # to nie jest najlepsze rozwiazanie bo sie wylacza dlatego ze jest error xd
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jezyk_1.collidepoint(pygame.mouse.get_pos()):
                        jezyk = 'polski'
                        return jezyk
                        #window2 = pygame.display((500, 500)) # jakas funkcja tu sie powinna odpalic??
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jezyk_2.collidepoint(pygame.mouse.get_pos()):
                        jezyk = 'angielski'
                        return jezyk
                        


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
                    jezyki()
                    #if jezyk == polski:
                     #   pass
                    running = False # to co sie dzieje po wyborze jezyka

if __name__=="__main__":
    main()
    pygame.quit()



    
