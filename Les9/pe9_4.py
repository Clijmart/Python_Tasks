def ticker(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()
    symbols = {}
    for bedrijf in lines:
        findSplit = bedrijf.index(':')
        name = bedrijf[:findSplit]
        symbol = bedrijf[findSplit+1:-1]
        symbols[name] = symbol
    return symbols


def nameToSymbol(symbols):
    name = input('Enter Company name: ')
    if name in symbols:
        print('Ticker symbol: {}'.format(symbols[name]))
    else:
        print('Invalid Company')


def symbolToName(symbols):
    symbol = input('Enter Ticker symbol: ')
    for bedrijf in symbols:
        if symbols[bedrijf] == symbol:
            name = bedrijf
            print('Company name: {}'.format(name))
            return
    print('Invalid Ticket')


symbols = ticker('tickersymbols.txt')
nameToSymbol(symbols)
symbolToName(symbols)
