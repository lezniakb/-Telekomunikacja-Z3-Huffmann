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
