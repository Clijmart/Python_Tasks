def seizoen(maand):
    if 3 >= maand <= 5:
        seizoen = 'lente'
    elif 6 >= maand <= 8:
        seizoen = 'zomer'
    elif 9 >= maand <= 11:
        seizoen = 'herfst'
    else:
        seizoen = 'winter'
    return 'Deze maand valt in de ' + seizoen


print(seizoen(int(input('Geef een maandnummer: '))))
