def convert(gradenCelcius):
    gradenFahrenheit = gradenCelcius * 1.8 + 32
    return gradenFahrenheit


def table():
    for gradenCelcius in range(-30, 41, 10):
        outputFahrenheit = '     ' + str(float(convert(gradenCelcius)))
        outputCelcius = '     ' + str(float(gradenCelcius))

        print(outputFahrenheit[-5:] + outputCelcius[-8:])


print('  F       C')
table()
