import pygame
import sys
import time


pygame.init()

# okno z wyświetlaczem
szerokosc = 750
wysokosc = 500
okno = pygame.display.set_mode([szerokosc,wysokosc])
pygame.display.set_caption("Wyświetlacz")
clock = pygame.time.Clock()

# kolory
czarny = (0, 0, 0)
bialy = (255, 255, 255)

alfabet = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
czcionka = pygame.font.SysFont("Times New Roman", 150)

def wyswieltanie_liter():
    for litera in alfabet:
        tekst = czcionka.render(litera, True, bialy)
        tekst_rect = tekst.get_rect()
        tekst_rect_center = ((szerokosc/2)-50,(wysokosc/2)-90)
        tekst_tlo = pygame.draw.rect(okno, czarny, (0, 0, 750, 500))
        okno.blit(tekst, tekst_rect_center)
        with open("zapisane_litery.txt", "a") as myfile:
            myfile.write(litera + ', ' + str(time.time()) + '\n')
        time.sleep(1)
        pygame.display.flip()

wyswietlanie = True
while wyswietlanie:

    pygame.display.update()

    okno.fill(czarny)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wyswietlanie = False

    wyswieltanie_liter()


pygame.quit()
            





