import pygame
import sys

def main():
    pygame.init()
    # logo = pygame.image.load("")
    # pygame. display.set_icon(logo)
    pygame.display.set_caption("podpis")

    screen = pygame.display.set_mode((550,200))

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
if __name__=="__main__":
    main()
    pygame.quit()