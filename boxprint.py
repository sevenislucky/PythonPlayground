"""
************
*          *
*          *
*          *
************

"""

def boxprint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception('"symbol" need to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('"height" or "width" need to be greater then 1.')
    
    print(symbol * width)

    for i in range (height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxprint('$', 20,10)
#boxprint('TT', 40,5)
#boxprint('z', 1,10)
#boxprint('z', 10,1)
