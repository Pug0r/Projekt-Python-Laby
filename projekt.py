import pygame
import sys

#potrzebne zmienne, ktore beda potem uzywane:
X = 1200
Y = 1000 # wymiary wyswietlanego okna
niebieski = (140, 219, 237)
fioletowy = (172, 105, 179)
rozowy = (240, 93, 176)
zielony = (160, 247, 148)
black = (0,0,0)
white = (255,255,255) # kolory w rgb

colors = [niebieski, fioletowy, rozowy, zielony]

class Text:
    def font(self, font, size):
        self.font = pygame.font.SysFont(f'{font}.ttf', size)

    def draw_text(self, text, color, place1, place2): # place2 = window, place1 = (,)
        tekst = self.font.render(text, True, color)
        place2.blit(tekst, place1)


class Button:
    def __init__(self, a, b, x1, y1, color, place): #place = window 
        self.rect = pygame.Rect(a,b,x1,y1)
        pygame.draw.rect(place, color, self.rect)

    def buttontext(self, text): #niegotowe
        pass

def main():
    running = True
    pygame.display.set_caption("gierka")
    window = pygame.display.set_mode((X, Y))

    def colorchange():
        window.fill(colors[0])
        button1 = Button(10, 20, 30, 30, colors[1], window)
        button2 = Button(10, 60, 30, 30, colors[2], window)
        button3 = Button(10, 100, 30, 30, colors[3], window)
        pygame.display.update()


    colorchange()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: #niegotowe
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #niegotowe
                    pass

if __name__=="__main__":
    main()
    pygame.quit()