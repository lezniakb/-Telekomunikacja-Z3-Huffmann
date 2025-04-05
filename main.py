import os
import heapq
import json
import math

def zakodujHuff(tekst):
    drzewo = zbudujDrzewo(tekst)
    kody = utworzKody(drzewo)
    zakodowany = ""
    # dla kazdego znaku w tekscie zastap go jego kodem huffmanna
    for znak in tekst:
        zakodowany += kody[znak]
    return kody, zakodowany

def iloscWystapien(tekst):
    # zapisujemy slownik zliczajacy ilosc liter
    iloscWystapien = {}
    for znak in tekst:
        # dla kazdego znaku w tekscie
        if znak in iloscWystapien:
            # jesli znak jest juz w slowniku, to dodaj kolejne wystapienie
            iloscWystapien[znak] += 1
        else:
            # jesli znaku nie ma w slowniku, to dodaj nowy element i przypisz mu =1
            iloscWystapien[znak] = 1
    # zwroc slownik czestotliwosci wystapien
    return iloscWystapien

def zbudujDrzewo(tekst):
    wystapienia = iloscWystapien(tekst)
    heap = []
    licznik = 0  # licznik unikalnych elementow do rozwiazywania remisu
    # dla kazdego znaku dajemy krotke (czestosc, licznik, znak)
    for znak, cz in wystapienia.items():
        heapq.heappush(heap, (cz, licznik, znak))
        licznik += 1
    # laczymy wezly drzewa az zostanie jeden element
    while len(heap) > 1:
        cz1, licznik1, lewy = heapq.heappop(heap)
        cz2, licznik2, prawy = heapq.heappop(heap)
        wezel = (lewy, prawy)  # nowy wezel laczacy dwa wezly
        heapq.heappush(heap, (cz1 + cz2, licznik, wezel))
        licznik += 1
    # ostatni element w kopcu to cale drzewo Huffmana
    drzewo = heap[0][2]
    return drzewo

def utworzKody(drzewo, prefix=""):
    # jesli jesteśmy na lisciu - znak jest pojedynczy
    if isinstance(drzewo, str):
        # jesli tekst sklada sie z jednego znaku, przypisz kod "0"
        if prefix == "":
            return {drzewo: "0"}
        return {drzewo: prefix}
    # rozdziel drzewo na lewy i prawy podwezel
    lewy, prawy = drzewo
    kody = {}
    # rekurencyjne wyznaczanie kodu dla lewego podwezla
    kody.update(utworzKody(lewy, prefix + "0"))
    # kod dla prawego podwezla
    kody.update(utworzKody(prawy, prefix + "1"))
    return kody

def przygotujTekst():
    # pobierz tekst od uzytkownika
    tekst = input("Podaj tekst do zakodowania: ")
    # pobierz nazwe pliku od uzytkownika
    nazwaPliku = input("Podaj nazwę pliku (bez rozszerzenia): ")

    # wykonaj kodowanie Huffmana
    kody, zakodowanyTekst = zakodujHuff(tekst)

    # obliczanie rozmiarow oryginalnego i zakod. tekstu (w bajtach)
    oryRozm = len(tekst.encode("utf-8"))
    nowyRozm = math.ceil(len(zakodowanyTekst) / 8.0)

    print(f"Rozmiar oryginalnego tekstu: {oryRozm} B")
    print(f"Rozmiar zakodowanego tekstu: {nowyRozm} B")

    # tworzymy strukture danych do zapisu (slownik kodowy oraz zakodowany tekst)
    data = {
        "slownik": kody,
        "zakodowany": zakodowanyTekst
    }

    sciezka = os.path.join(".\\przygotowane", nazwaPliku + ".txt")
    # zapisujemy dane w formacie JSON
    with open(sciezka, "w", encoding="utf-8") as plik:
        json.dump(data, plik)
    print("Plik został pomyślnie zapisany: " + sciezka)

# glowna petla
# sprawdzenie czy foldery istnieja
if os.path.exists(".\\przygotowane") != True:
    os.makedirs(".\\przygotowane")
if os.path.exists(".\\odebrane") != True:
    os.makedirs(".\\odebrane")

while True:
    print("--------------\nMenu Główne:\n"
          "1. Przygotuj tekst\n"
          "2. Wyślij tekst\n"
          "3. Odbierz tekst\n"
          "4. Zakończ program")
    wybor = input("Wybierz opcję: ").strip()
    if wybor == "1":
        przygotujTekst()
    elif wybor == "2":
        print("Wyślij tekst")
    elif wybor == "3":
        print("Odbierz tekst")
    elif wybor == "4":
        print("Zakończ program")
        break
    else:
        print("Wybrano niewłaściwą opcję!")
    input("Wciśnij enter aby kontynuować...")

print("\nProgram zakończony pomyślnie")