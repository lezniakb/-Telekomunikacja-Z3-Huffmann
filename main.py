# glowna petla
while True:
    print("--------------\nMenu Główne:\n"
          "1. Skompresuj tekst\n"
          "2. Dekompresuj tekst\n"
          "3. Skompresuj plik\n"
          "4. Dekompresuj plik\n"
          "5. Pokaż statystyki\n"
          "6. Zakończ program")
    wybor = input("Wybierz opcję: ").strip()
    if wybor == "1":
        print("kompresuj tekst")
    elif wybor == "2":
        print("dekompresuj tekst")
    elif wybor == "3":
        print("kompresuj plik")
    elif wybor == "4":
        print("dekompresuj plik")
    elif wybor == "5":
        print("statystyki")
    elif wybor == "6":
        break
    else:
        print("Wybrano niewłaściwą opcję!")
    input("Wciśnij enter aby kontynuować...")

print("Program zakończony pomyślnie")