# Telekomunikacja Zadanie 3
### Algorytm Huffmanna i transmisja wiadomości
### Opis projektu
[PL] Repozytorium zawiera algorytm implementujący kod Huffmanna do zmniejszania rozmiaru wysyłanej wiadomości. Rozwiązanie zawiera zarówno kodowanie, odkodowanie komunikatów, jak i wysyłanie oraz odbieranie wiadomości wewnątrz sieci lokalnej. Zadanie realizowane jest w ramach przedmiotu "*Telekomunikacja i przetwarzanie sygnałów*" na Politechnice Łódzkiej - 4 semestr na kierunku Informatyka Stosowana.

[EN[ This repository contains an algorithm that implements Huffman coding to reduce the size of transmitted messages. The solution includes both encoding and decoding of messages, as well as sending and receiving messages within a local network. The assignment is carried out as part of the "*Telecommunications and Signal Processing*" course at Lodz University of Technology – 4th semester in Computer Science.

## Opis zadania
Dla podanego tekstu należy opracować słownik kodowy, umieć uzasadnić jego zawartość. Kolejnym zadaniem jest zbudowanie programów, które kodują plik tekstowy i przesyła go za pomocą metody gniazd sieciowych (socked) na inny komputer, na którym jest zaimplementowany drugi progam, którego zadaniem jest odebranie, odkodowanie i zapisanie go na dysku

# Instrukcja
1. Uruchom main.py w dwóch osobnych terminalach (może być powershell i pycharm)
2. Wybierz opcję **"Przygotuj tekst"** z menu głównego i wprowadź komunikat. Podaj nazwę pliku, pod którą komunikat ma zostać zakodowany i zapisany. Zweryfikuj poprawność zapisania komunikatu do folderu "*.\przygotowane\nazwa_pliku.txt*".
3. Uruchom terminal swojego wyboru (PS, CMD, bash) i sprawdź **lokalne IP** maszyny komendą *ipconfig* w Windowsie lub *ifconfig -a* dla linuxa (przykład: *192.168.100.2*)
4. Wybierz opcję **"Odbierz tekst"** w pierwszym terminalu. 
5. Podaj port, na który zostanie wysłany plik (np. *4444*).
6. Wybierz opcję **"Wyślij tekst"** w drugim terminalu.
7. Wprowadź numer pliku, który chcesz nadać.
8. Podaj adres **IP odbiorcy** (w naszym przykładzie: *192.168.100.2*).
9. Podaj **port odbiorcy**, czyli ten, który został podany w kroku 5.
10. Wiadomość powinna zostać nadana pomyślnie. Jeśli się nie udało, otwórz nowe issue w repozytorium i opisz problem.
11. W terminalu pierwszym powinna wyświetlić się informacja o odebranym pliku. Wprowadź nazwę dla nowego pliku, aby go zapisać.

## Zasada działania algorytmu Huffmanna
W naszym programie wiadomość jest konwertowana algorytmem Huffmanna do postaci **skompresowanej**. Obywa się to przez zliczenie wszystkich znaków w komunikacie. Jest to najprostszy algorytm kompresji.
1. Utwórz słownik wystąpień (struktura w pythonie). Zapisuje ona każdą znalezioną literę w tekście i liczy ilość jej wystąpień.
2. Budowane jest drzewo Huffmanna. Zaczynamy od umieszczenia wszystkich znaków z ilością występowania w kopcu priorytetowym, który szybko wybiera elementy o najmniejszej ilości wystąpień.
3. W pętli pobierane są dwa elementy o najniższej ilości występowania i łączene są w nowy węzeł (częstotliwość występowania tych elementów wynosi sumę obu poszczególnych częstotliwości). Wynik wstawiany jest znowu do kopca. Proces powtarzany jest dopóki w kopcu zostanie jeden element. Ten element zostaje korzeniem drzewa.
4. Wyznaczanie unikalnych kodów dla każdego ze znaków. Rekurencyjnie przchodzimy przez drzewo i przy przechodzeniu w lewo dostawiamy "0" a w prawo "1".
5. Każdy liść drzewa odpowiada konkretnemu znakowi, więc dzięki ścieżce od korzenia dostajemy unikalny kod binarny.
6. Ten kod binarny wstawiany jest do zakodowanego pliku. Plik ma formę:<br />{<br />"słownik": {"a":"0", "b":"10", "c":"11"},<br />"zakodowany": 10110<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br /> Daje to nam komunikat "abc".
7. Plik w tej postaci wysyłany jest do odbiorcy.

## Przykład dla zobrazowania
1. Dla komunikatu "*abc*" każdy znak występuje raz. a=1, b=1, c=1.
2. Dla każdego znaku **tworzymy krotkę**: (częstotliwość występowania, licznik, znak):<br />- (1, 0, "a")<br />- (1, 1, "b")<br />- (1, 2, "c")<br />Warto zwrócić uwagę, że zmienna "*licznik*" zapobiega występowaniu remisów.
3. **Tworzymy węzeł** = ("a", "b").<br />Częstotliwość wynosi 2, bo czA=1 oraz czB=1.
4. **Do kopca wstawiamy krotkę** (2, 3, ("a", "b")).<br />Kopiec teraz zawiera:<br />- (1, 2, "c")<br />- (2, 3, ("a", "b"))
5. **Łączymy kolejne dwa węzły** i otrzymujemy: ("c", ("a", "b")). Jego częstotliwość wynosi 3.
6. **Wstawiamy go do kopca.** Obecnie w kopcu mamy tylko jeden węzeł i jest to: (3, 4, ("c", ("a", "b"))),<br />- częstotliwość: 3<br />- licznik: 4<br />- znak: ("c", ("a", "b"))
7. **Generujemy kod** idąc od lewej: c="0", a="10", b="11"
8. Otrzymujemy kod: "10110", czyli znaki 10 11 0.
9. W tej formie **wstawiamy kod** do pliku przygotowanego do wysłania.

### Drzewo z przykładu
            (*,3)
            /     \
         "c"     (*,2)
                /     \
              "a"      "b"

**Korzeń drzewa**: Łączna częstotliwość 3, struktura: ("c", ("a", "b"))<br />**Lewe dziecko:** Liść "c"<br />**Prawe dziecko:** Węzeł wewnętrzny, którego lewe dziecko to "a", a prawe to "b"
