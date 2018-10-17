from random import randint


def monopolyworp():
    for worp in range(1, 4):
        dobbelsteen1 = randint(1, 6)
        dobbelsteen2 = randint(1, 6)
        totaal = dobbelsteen1 + dobbelsteen2

        if dobbelsteen1 == dobbelsteen2:
            if worp == 3:
                print('{} + {} = (direct naar gevangenis)'.format(dobbelsteen1, dobbelsteen2))
                break
            else:
                print('{} + {} = {} (dubbel)'.format(dobbelsteen1, dobbelsteen2, totaal))
        else:
            print('{} + {} = {}'.format(dobbelsteen1, dobbelsteen2, totaal))
            break


monopolyworp()
