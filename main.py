import os
import heapq
import json
import math
import socket

def zakodujHuff(tekst):
    drzewo = zbudujDrzewo(tekst)
    kody = utworzKody(drzewo)
    zakodowany = ""
    # dla kazdego znaku w tekscie zastap go jego kodem huffmanna
    for znak in tekst:
        zakodowany += kody[znak]
    return kody, zakodowany

def odkodujHuff(zakodowanyTekst, kody):
    # budujemy odwrocony slownik: kod -> znak
    odwrKody = {}
    for klucz, wartosc in kody.items():
        odwrKody[wartosc] = klucz
    odkodowany = ""
    nowy = ""
    # odczytujemy kolejne bity i sprawdzamy czy pasuja do kodu
    for bit in zakodowanyTekst:
        nowy += bit
        if nowy in odwrKody:
            odkodowany += odwrKody[nowy]
            nowy = ""
    return odkodowany

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

def nadajWiadomosc():
    folder = ".\\przygotowane"
    przygotowanePliki = os.listdir(folder)
    if not przygotowanePliki:
        print("Brak plików w folderze .\\przygotowane ")
        return False

    print("\nPrzygotowane pliki:")
    for i, plik in enumerate(przygotowanePliki):
        print(f"{i+1}. {plik}")

    wybor = input("Podaj numer pliku do wysłania: ")
    indeksPliku = int(wybor) - 1
    if indeksPliku < 0 or indeksPliku >= len(przygotowanePliki):
        print("Niewłaściwy wybór")
        return False

    file_path = os.path.join(folder, przygotowanePliki[indeksPliku])

    # odczytujemy zawartosc wybranego pliku
    with open(file_path, "r", encoding="utf-8") as f:
        file_data = f.read()

    # IP odbiorcy (jesli robi sie test na jednej maszynie mozna wpisac 127.0.0.1)
    ip = input("Podaj adres IP odbiorcy: ")

    # port odbiorcy - może być np. 4444 albo 12345
    port = int(input("Podaj port odbiorcy: "))

    try:
        # utworzenie gniazda TCP klienta
        socketKlient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketKlient.connect((ip, port))
        # wysylamy dane - konwersja do bajtow z uzyciem utf-8
        socketKlient.sendall(file_data.encode("utf-8"))
        print("Plik został pomyślnie wysłany!")
        socketKlient.close()
    except Exception as e:
        print("Wystąpił błąd podczas wysyłania: ", e)


def odbierzWiadomosc():
    # port odbiorcy - może być np. 4444 albo 12345, nie musi być taki sam co nadawcy
    # jesli tekst odbierany jest na tej samej maszynie to port nie może być taki sam!
    port = int(input("Podaj port na którym otworzy się połączenie: "))
    # utworzenie gniazda serwera TCP
    socketSerwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketSerwer.bind(("", port))
    socketSerwer.listen(1)
    print("Oczekiwanie na połączenie na porcie {port}...")

    polaczenie, ip = socketSerwer.accept()
    print(f"Nawiązano połączenie z IP: {ip}")
    chunkiDanych = []

    # odbieramy dane w petli, az nie przestanie przychodzic
    while True:
        data = polaczenie.recv(4096)
        if not data:
            break
        chunkiDanych.append(data)

    calosc = b"".join(chunkiDanych).decode("utf-8")
    polaczenie.close()
    socketSerwer.close()

    try:
        # probujemy zdekodowac odebrane dane jako format JSON
        dane = json.loads(calosc)
        slownikLiter = dane["slownik"]
        zakodowanyTekst = dane["zakodowany"]
        # dekodowanie tekstu przy uzyciu otrzymanego slownika kodowego
        odkodowanyTekst = odkodujHuff(zakodowanyTekst, slownikLiter)
    except Exception as e:
        print("Wystąpił błąd podczas dekodowania danych: ", e)
        return False

    # pobierz nazwe pliku do zapisu odszyfrowanego tekstu
    nazwaPliku = input("Podaj nazwe pliku do zapisania odebranego tekstu (bez rozszerzenia): ")
    folder = ".\\odebrane"
    sciezka = os.path.join(folder, nazwaPliku + ".txt")

    with open(sciezka, "w", encoding="utf-8") as f:
        f.write(odkodowanyTekst)
    print("Zapisano do: " + sciezka)
    print(f"Odebrany tekst: {odkodowanyTekst}")
    obliczRozmiary()


def obliczRozmiary(oryginalnyTekst, zakodowanyTekst):
    # obliczanie rozmiarow oryginalnego i zakod. tekstu (w bajtach)
    oryRozm = len(oryginalnyTekst.encode("utf-8"))
    nowyRozm = math.ceil(len(zakodowanyTekst) / 8.0)

    print(f"Rozmiar oryginalnego tekstu: {oryRozm} B")
    print(f"Rozmiar zakodowanego tekstu: {nowyRozm} B")

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
        nadajWiadomosc()
    elif wybor == "3":
        odbierzWiadomosc()
    elif wybor == "4":
        print("Zakończ program")
        break
    else:
        print("Wybrano niewłaściwą opcję!")
    input("Wciśnij enter aby kontynuować...")

print("\nProgram zakończony pomyślnie")