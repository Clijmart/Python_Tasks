def convert(gradenCelcius):
    gradenFahrenheit = gradenCelcius * 1.8 + 32
    return gradenFahrenheit


def table():
    print('  F       C')
    for gradenCelcius in range(-30, 41, 10):
        print('{:5}   {:5}'.format(convert(gradenCelcius), float(gradenCelcius)))


table()
