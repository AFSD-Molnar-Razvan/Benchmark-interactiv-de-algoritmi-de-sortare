import pygame
import random
import math

# Initializam modulul pygame
pygame.init()


class InfoDesenare:
    # Definim culorile in RGB (Red, Green, Blue)
    NEGRU = 0, 0, 0
    ALB = 255, 255, 255
    VERDE = 0, 255, 0
    ROSU = 255, 0, 0
    CULOARE_FUNDAL = ALB

    # 3 nuante de gri ca sa diferentiem barele intre ele (arata mai bine vizual)
    GRI_URI = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    # Setam fonturile (folosim comicsans sau orice alt font default)
    FONT_MIC = pygame.font.SysFont('comicsans', 20)
    FONT_MARE = pygame.font.SysFont('comicsans', 30)

    # Spatii pe margini ca sa nu se lipeasca graficul de marginile ferestrei
    PADDING_LATERAL = 100
    PADDING_SUS = 150

    def __init__(self, latime, inaltime, lista_numere):
        self.latime = latime
        self.inaltime = inaltime

        # Setam fereastra
        self.fereastra = pygame.display.set_mode((latime, inaltime))
        pygame.display.set_caption("Benchmark Sortare - Molnar si Roman (Anul 2)")

        self.setare_lista(lista_numere)

    def setare_lista(self, lista_numere):
        self.lista = lista_numere
        self.val_min = min(lista_numere)
        self.val_max = max(lista_numere)

        # Calculam cat de lata sa fie o bara ca sa incapa toate pe ecran
        self.latime_bloc = round((self.latime - self.PADDING_LATERAL) / len(lista_numere))

        # Calculam inaltimea folosind math.floor ca sa evitam numerele cu virgula
        self.inaltime_bloc = math.floor((self.inaltime - self.PADDING_SUS) / (self.val_max - self.val_min))

        # De unde incepem sa desenam pe axa X
        self.start_x = self.PADDING_LATERAL // 2


def desenare_interfata(info):
    # Curatam ecranul la fiecare cadru
    info.fereastra.fill(info.CULOARE_FUNDAL)

    # Randam textul
    titlu = info.FONT_MARE.render("Proiect: Benchmark Interactiv de Sortare", 1, info.NEGRU)
    info.fereastra.blit(titlu, (info.latime / 2 - titlu.get_width() / 2, 10))

    controale = info.FONT_MIC.render("Apasa R pentru Reset | SPACE pentru Start", 1, info.NEGRU)
    info.fereastra.blit(controale, (info.latime / 2 - controale.get_width() / 2, 50))

    # Apelam functia care deseneaza barele
    desenare_bare(info)

    # Facem update la display
    pygame.display.update()


def desenare_bare(info):
    lista = info.lista

    # Trecem prin toata lista si desenam fiecare bara
    for i, valoare in enumerate(lista):
        # Calculam coordonatele x si y
        x = info.start_x + i * info.latime_bloc
        y = info.inaltime - (valoare - info.val_min) * info.inaltime_bloc

        # Alternam culorile folosind modulo 3
        culoare = info.GRI_URI[i % 3]

        # Desenam dreptunghiul (bara) pe ecran
        pygame.draw.rect(info.fereastra, culoare, (x, y, info.latime_bloc, info.inaltime))


def generare_lista_start(n, val_min, val_max):
    lista_noua = []
    for _ in range(n):
        valoare = random.randint(val_min, val_max)
        lista_noua.append(valoare)
    return lista_noua


def main():
    ruleaza = True
    ceas = pygame.time.Clock()

    # Parametrii pentru lista generata
    n = 50
    val_min = 0
    val_max = 100

    # Generam lista si instantiem clasa de desenare
    lista = generare_lista_start(n, val_min, val_max)
    info = InfoDesenare(800, 600, lista)

    # Bucla principala a programului
    while ruleaza:
        # Setam la maxim 60 FPS ca sa nu solicite procesorul degeaba
        ceas.tick(60)

        desenare_interfata(info)

        # Verificam actiunile utilizatorului
        for event in pygame.event.get():
            # Daca apasa pe X-ul ferestrei
            if event.type == pygame.QUIT:
                ruleaza = False

            # Daca apasa pe o tasta
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # R = Reset, generam o lista noua
                    lista = generare_lista_start(n, val_min, val_max)
                    info.setare_lista(lista)

    pygame.quit()


# Punctul de intrare in program
if __name__ == "__main__":
    main()