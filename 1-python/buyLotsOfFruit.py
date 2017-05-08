fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}

def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order
    """

    counter = 0.0
    for fruit in orderList:
        if fruit[ 0 ] in fruitPrices.keys():
            counter = counter + fruit[ 1 ] * fruitPrices[ fruit[ 0 ] ]
        else:
            return None

    list = []
    print( enumerate( [1, 2, 3, 4, 5 ] ) )

    return counter





orderList = [('apples', 2), ('pears', 3), ('limes', 4)]
print('Cost of', orderList, 'is', buyLotsOfFruit(orderList))
