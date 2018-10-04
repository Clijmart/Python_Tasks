while True:
    woord = input('Geef een string van 4 letters: ')
    if len(woord) == 4:
        print(woord + ' is geslaagd, het heeft 4 letters!')
        break
    else:
        print(woord + ' heeft ' + str(len(woord)) + ' letters')
