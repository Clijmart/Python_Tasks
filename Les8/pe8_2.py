while True:
    lijst = eval(input("Geef lijst met minimaal 10 strings: "))
    if len(lijst) < 10:
        print('Geef minimaal 10 strings!\n')
    else:
        quadLijst = []
        for string in lijst:
            if len(string) == 4:
                quadLijst.append(string)
        print('De nieuw-gemaakte lijst met alle vier-letter strings is: ', quadLijst)
        exit()