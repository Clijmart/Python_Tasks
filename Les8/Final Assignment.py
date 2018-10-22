totaal_aantal_kluizen = 12
empty_lines = '\n\n\n\n\n'


def input_start():
    while True:
        print(empty_lines)
        print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
        print('2: Ik wil een nieuwe kluis')
        print('3: Ik wil even iets uit mijn kluis halen')
        print('4: Ik geef mijn kluis terug')
        print('5: Ik wil stoppen')
        optie = input('Bepaal je keuze (1-5) en druk op enter: ')
        if optie == '1':
            toon_aantal_kluizen_vrij()
        elif optie == '2':
            nieuwe_kluis()
        elif optie == '3':
            kluis_openen()
        elif optie == '4':
            kluis_teruggeven()
        elif optie == '5':
            exit('Bedankt en tot ziens!')


def toon_aantal_kluizen_vrij():
    kluizen_file = open('kluizen.txt')
    kluizen_bezet = kluizen_file.readlines()
    kluizen_file.close()
    if len(kluizen_bezet) == 0:
        kluizen_vrij = totaal_aantal_kluizen
    else:
        kluizen_vrij = totaal_aantal_kluizen - len(kluizen_bezet)
    print(empty_lines)
    if kluizen_vrij == 1:
        print('Er is nog 1 kluis vrij')
    elif kluizen_vrij == 0:
        print('Er zijn geen kluizen meer vrij')
    else:
        print('Er zijn nog ' + str(kluizen_vrij) + ' kluizen vrij')
    input('\nKlik op Enter om terug naar het menu te gaan')


def nieuwe_kluis():
    kluizen_list = []
    for kluis_nummer in range(1, totaal_aantal_kluizen + 1):
        kluizen_list.append(kluis_nummer)
    kluizen_file = open('kluizen.txt')
    kluizen_bezet = kluizen_file.readlines()
    kluizen_file.close()
    for file_line in kluizen_bezet:
        kluis_nummer = int(file_line[:(file_line.index(';'))])
        kluizen_list.pop(kluizen_list.index(kluis_nummer))
    print(empty_lines)
    if len(kluizen_list) > 0:
        kluis_code = input('Voer een kluiscode in: ')
        kluis_select = kluizen_list[0]
        kluizen_file = open('kluizen.txt', 'a')
        kluizen_file.write(str(kluis_select) + ';' + str(kluis_code) + '\n')
        kluizen_file.close()
        print('Je hebt kluis ' + str(kluis_select))
    else:
        print('Sorry, er zijn geen kluizen meer vrij')
    input('\nKlik op Enter om terug naar het menu te gaan')


def kluis_openen():
    print(empty_lines)
    kluis_nummer = input('Jouw kluisnummer: ')
    kluis_code = input('Jouw kluiscode: ')
    kluizen_file = open('kluizen.txt')
    kluizen_bezet = kluizen_file.readlines()
    kluizen_file.close()
    print(empty_lines)
    codeCorrect = False
    for file_line in kluizen_bezet:
        if file_line == str(kluis_nummer) + ';' + str(kluis_code) + '\n':
            print('Code correct, kluis geopend')
            codeCorrect = True
    if not(codeCorrect):
        print('Code incorrect!')
    input('\nKlik op Enter om terug naar het menu te gaan')


def kluis_teruggeven():
    print(empty_lines)
    kluis_nummer = input('Jouw kluisnummer: ')
    kluis_code = input('Jouw kluiscode: ')
    kluizen_file = open('kluizen.txt')
    kluizen_bezet = kluizen_file.readlines()
    kluizen_file.close()
    print(empty_lines)
    codeCorrect = False
    for file_line in kluizen_bezet:
        if file_line == str(kluis_nummer) + ';' + str(kluis_code) + '\n':
            kluizen_bezet.pop(kluizen_bezet.index(file_line))
            kluizen_file = open('kluizen.txt', 'w')
            for line in kluizen_bezet:
                kluizen_file.write(line)
            kluizen_file.close()
            print('Kluis verwijderd')
            codeCorrect = True
    if not(codeCorrect):
        print('Code incorrect!')
    input('\nKlik op Enter om terug naar het menu te gaan')


def check_file():
    try:
        kluizen_file = open('kluizen.txt')
    except:
        kluizen_file = open('kluizen.txt', 'w+')
    kluizen_file.close()


check_file()
input_start()
