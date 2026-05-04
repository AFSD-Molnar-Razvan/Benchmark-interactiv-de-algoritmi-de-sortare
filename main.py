import pygame
import random
import math
import time

pygame.init()


class InfoDesenare:
    # culori rgb
    NEGRU = 0, 0, 0
    ALB = 255, 255, 255
    VERDE = 0, 255, 0
    ROSU = 255, 0, 0
    CULOARE_FUNDAL = ALB

    GRI_URI = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT_MIC = pygame.font.SysFont('comicsans', 20)
    FONT_MARE = pygame.font.SysFont('comicsans', 30)

    # spatiere interfata
    PADDING_LATERAL = 100
    PADDING_SUS = 150

    def __init__(self, latime, inaltime, lista_numere):
        self.latime = latime
        self.inaltime = inaltime
        self.fereastra = pygame.display.set_mode((latime, inaltime))
        pygame.display.set_caption("Benchmark Sortare - Molnar si Roman")
        self.setare_lista(lista_numere)

        # init stats
        self.comparatii = 0
        self.interschimbari = 0
        self.timp_start = 0
        self.timp_scurs = 0

    def setare_lista(self, lista_numere):
        self.lista = lista_numere
        self.val_min = min(lista_numere)
        self.val_max = max(lista_numere)

        # calculam latimea si inaltimea dinamica in functie de cate elemente avem
        self.latime_bloc = round((self.latime - self.PADDING_LATERAL) / len(lista_numere))
        self.inaltime_bloc = math.floor((self.inaltime - self.PADDING_SUS) / (self.val_max - self.val_min))
        self.start_x = self.PADDING_LATERAL // 2

        # resetam statisticile pt lista noua
        self.comparatii = 0
        self.interschimbari = 0
        self.timp_scurs = 0


def desenare_interfata(info, nume_algoritm, crescator):
    info.fereastra.fill(info.CULOARE_FUNDAL)

    sens = "Crescator" if crescator else "Descrescator"
    titlu = info.FONT_MARE.render(f"{nume_algoritm} - {sens}", 1, info.VERDE)
    info.fereastra.blit(titlu, (info.latime / 2 - titlu.get_width() / 2, 5))

    controale = info.FONT_MIC.render("R - Reset | SPACE - Start | A - Crescator | D - Descrescator", 1, info.NEGRU)
    info.fereastra.blit(controale, (info.latime / 2 - controale.get_width() / 2, 45))

    sortari = info.FONT_MIC.render("B - Bubble Sort | I - Insertion Sort", 1, info.NEGRU)
    info.fereastra.blit(sortari, (info.latime / 2 - sortari.get_width() / 2, 75))

    # randare stats
    text_stats = f"Timp: {info.timp_scurs:.2f}s | Comparatii: {info.comparatii} | Interschimbari: {info.interschimbari}"
    stats = info.FONT_MIC.render(text_stats, 1, info.ROSU)
    info.fereastra.blit(stats, (info.latime / 2 - stats.get_width() / 2, 110))

    desenare_bare(info)
    pygame.display.update()


def desenare_bare(info, pozitii_colorate={}, curata_fundal=False):
    lista = info.lista

    # daca facem update in timpul sortarii, stergem doar zona cu bare ca sa nu avem flicker la text
    if curata_fundal:
        zona_curatare = (info.PADDING_LATERAL // 2, info.PADDING_SUS,
                         info.latime - info.PADDING_LATERAL, info.inaltime - info.PADDING_SUS)
        pygame.draw.rect(info.fereastra, info.CULOARE_FUNDAL, zona_curatare)

        # update separat pt stats
        zona_stats = (0, 110, info.latime, 35)
        pygame.draw.rect(info.fereastra, info.CULOARE_FUNDAL, zona_stats)
        text_stats = f"Timp: {info.timp_scurs:.2f}s | Comparatii: {info.comparatii} | Interschimbari: {info.interschimbari}"
        stats = info.FONT_MIC.render(text_stats, 1, info.ROSU)
        info.fereastra.blit(stats, (info.latime / 2 - stats.get_width() / 2, 110))

    for i, valoare in enumerate(lista):
        x = info.start_x + i * info.latime_bloc
        y = info.inaltime - (valoare - info.val_min) * info.inaltime_bloc
        culoare = info.GRI_URI[i % 3]

        if i in pozitii_colorate:
            culoare = pozitii_colorate[i]

        pygame.draw.rect(info.fereastra, culoare, (x, y, info.latime_bloc, info.inaltime))

    if curata_fundal:
        pygame.display.update()


def bubble_sort(info, crescator=True):
    lista = info.lista
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            numar1 = lista[j]
            numar2 = lista[j + 1]

            info.comparatii += 1

            if (numar1 > numar2 and crescator) or (numar1 < numar2 and not crescator):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                info.interschimbari += 1

                # punem rosu si verde pe elementele curent selectate
                desenare_bare(info, {j: info.VERDE, j + 1: info.ROSU}, True)
                # pauza pt animatie
                yield True
    return lista


def insertion_sort(info, crescator=True):
    lista = info.lista
    for i in range(1, len(lista)):
        curent = lista[i]
        while True:
            info.comparatii += 1
            ascendent_ok = i > 0 and lista[i - 1] > curent and crescator
            descendent_ok = i > 0 and lista[i - 1] < curent and not crescator

            if not ascendent_ok and not descendent_ok:
                break

            lista[i] = lista[i - 1]
            i = i - 1
            lista[i] = curent
            info.interschimbari += 1

            desenare_bare(info, {i - 1: info.VERDE, i: info.ROSU}, True)
            yield True
    return lista


def generare_lista_start(n, val_min, val_max):
    lista_noua = []
    for _ in range(n):
        lista_noua.append(random.randint(val_min, val_max))
    return lista_noua


def main():
    ruleaza = True
    ceas = pygame.time.Clock()

    n = 50
    val_min = 0
    val_max = 100

    lista = generare_lista_start(n, val_min, val_max)
    info = InfoDesenare(800, 600, lista)

    sortare = False
    crescator = True
    algoritm_sortare = bubble_sort
    nume_algoritm = "Bubble Sort"
    generator_sortare = None

    # setup sunet
    pygame.mixer.init()
    try:
        sunet = pygame.mixer.Sound("click.wav")
        sunet.set_volume(0.3)
    except FileNotFoundError:
        print("Atentie: Fisierul click.wav lipseste!")

    while ruleaza:
        ceas.tick(60)

        if sortare:
            # actualizare cronometru daca ruleaza algoritmul
            info.timp_scurs = time.time() - info.timp_start
            try:
                next(generator_sortare)
            except StopIteration:
                sortare = False
        else:
            desenare_interfata(info, nume_algoritm, crescator)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ruleaza = False

            if event.type == pygame.KEYDOWN:
                taste_valide = [pygame.K_r, pygame.K_SPACE, pygame.K_a, pygame.K_d, pygame.K_b, pygame.K_i]
                if event.key in taste_valide:
                    try:
                        sunet.play()
                    except:
                        pass

                if event.key == pygame.K_r:
                    lista = generare_lista_start(n, val_min, val_max)
                    info.setare_lista(lista)
                    sortare = False

                elif event.key == pygame.K_SPACE and not sortare:
                    sortare = True
                    # resetare contoare cand incepem
                    info.comparatii = 0
                    info.interschimbari = 0
                    info.timp_start = time.time()

                    generator_sortare = algoritm_sortare(info, crescator)

                elif event.key == pygame.K_a and not sortare:
                    crescator = True
                elif event.key == pygame.K_d and not sortare:
                    crescator = False
                elif event.key == pygame.K_b and not sortare:
                    algoritm_sortare = bubble_sort
                    nume_algoritm = "Bubble Sort"
                elif event.key == pygame.K_i and not sortare:
                    algoritm_sortare = insertion_sort
                    nume_algoritm = "Insertion Sort"

    pygame.quit()


if __name__ == "__main__":
    main()