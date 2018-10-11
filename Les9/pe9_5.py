def namen():
    namen = {}
    while True:
        naam = input('Volgende naam: ')
        if naam == '':
            break
        if naam in namen:
            namen[naam] += 1
        else:
            namen[naam] = 1
    return namen


def output(namen):
    for naam in namen:
        if namen[naam] == 1:
            print('Er is 1 student met de naam {}'.format(naam))
        else:
            print('Er zijn {} studenten met de naam {}'.format(namen[naam], naam))


output(namen())