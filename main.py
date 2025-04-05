import os

# glowna petla

# sprawdzenie czy foldery istnieja
if os.path.exists("./przygotowane") != True:
    os.makedirs("./przygotowane")
if os.path.exists("./odebrane") != True:
    os.makedirs("./odebrane")

while True:
    print("--------------\nMenu Główne:\n"
          "1. Przygotuj tekst\n"
          "2. Wyślij tekst\n"
          "3. Odbierz tekst\n"
          "4. Zakończ program")
    wybor = input("Wybierz opcję: ").strip()
    if wybor == "1":
        print("Przygotuj tekst")
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