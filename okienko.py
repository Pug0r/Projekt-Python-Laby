import pygame
import sys

def main():
    pygame.init()
    # logo = pygame.image.load("")
    # pygame. display.set_icon(logo) # to gdybysmy mieli jakies logo to mozna je tak dodac chyba
    pygame.display.set_caption("podpis") # nazwa aplikaci jaka sie wyswietla


    window = pygame.display.set_mode((1200,1000))
    
    niebieski = (37, 247, 247) # definicja koloru (rgb)
    fioletowy = (172, 105, 179)

    window.fill(fioletowy) 
    pygame.display.flip() # te dwie linijki zmieniaja kolor
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
if __name__=="__main__":
    main()
    pygame.quit()
    