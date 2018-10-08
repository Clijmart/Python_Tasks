def seizoen(maand):
    if maand in [3, 4, 5]:
        output = 'Deze maand valt in de lente'
    elif maand in [6, 7, 8]:
        output = 'Deze maand valt in de zomer'
    elif maand in [9, 10, 11]:
        output = 'Deze maand valt in de herfst'
    elif maand in [12, 1, 2]:
        output = 'Deze maand valt in de winter'
    else:
        output = 'Error. ' + str(maand) + ' is niet een maandnummer!'
    return output


print(seizoen(int(input('Geef een maandnummer: '))))
