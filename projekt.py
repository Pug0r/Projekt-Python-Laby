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
    def __init__(self):
        pass

    def font(self, font, size):
        self.font = pygame.font.SysFont(font, size)

    def draw_text(self, text, color, place1, place2): # place2 = window, place1 = (,)
        tekst = self.font.render(text, True, color)
        place2.blit(tekst, place1)
        self.tekst = tekst


class Button:
    def __init__(self, a, b, x1, y1): #place = window 
        self.rect = pygame.Rect(a,b,x1,y1)
        self.x = x1 # przydatne potem do umieszczania tekstu
        self.y = y1
        self.a = a
        self.b = b

    def draw(self, place, color):
        pygame.draw.rect(place, color, self.rect)

    def buttontext(self, text, font, fontsize, place2, x): #place 2 = window
        tekst = Text()
        tekst.font(font, fontsize)
        tekst.draw_text(text, black, (self.a + x, self.b + self.y/3), place2)

    def click(self, func):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    func()
        


def main():
    running = True
    pygame.font.init()
    pygame.display.set_caption("gierka")
    window = pygame.display.set_mode((X, Y))
    


    tekst_startowy = Text()
    tekst_startowy.font('tlwgtypo.ttf', 32)


#ZMIANA KOLORU W MENU STARTOWYM 

    button1 = Button(10, 20, 30, 30) # przyciski do zmiany koloru
    button2 = Button(10, 60, 30, 30)
    button3 = Button(10, 100, 30, 30)


    def colorsupdate(n):
        colors[0], colors[n] = colors[n], colors[0]
        window.fill(colors[0])
        button1.draw(window, colors[1])
        button2.draw(window, colors[2])
        button3.draw(window, colors[3])
        tekst_startowy.draw_text('wciśnij enter aby rozpocząć', black, (X/2 - 150, Y-50), window)
        pygame.display.update()

    colorsupdate(0)

    def wybor_koloru():
        if button1.rect.collidepoint(pygame.mouse.get_pos()):
            colorsupdate(1)
        if button2.rect.collidepoint(pygame.mouse.get_pos()):
            colorsupdate(2)
        if button3.rect.collidepoint(pygame.mouse.get_pos()):
            colorsupdate(3)

# WYBOR JEZYKA
    def wybor_jezyka():
        window.fill(colors[0])
        polski = Button(350, 400, 500, 100)
        angielski = Button(350, 550, 500, 100)
        polski.draw(window, white)
        angielski.draw(window, white)
        polski.buttontext('polski', 'tlwgtypo.ttf', 45, window, 200)
        angielski.buttontext('angielski', 'tlwgtypo.ttf', 45, window, 180)
        tekst_wyborjezyka = Text()
        tekst_wyborjezyka.font('tlwgtypo.ttf', 45)
        tekst_wyborjezyka.draw_text('wybierz język', black, (X/2-80, 350), window)
        pygame.display.update()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                wybor_koloru()
            if event.type == pygame.KEYDOWN: # przejscie do wyboru jezyka
                if event.key == pygame.K_RETURN:
                    wybor_jezyka()


if __name__=="__main__":
    main()
    pygame.quit()