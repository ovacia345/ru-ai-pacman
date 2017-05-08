# a built-in library containing some mathematical operations like square root
import math


class AlbertHeijn():
    '''
    A class to represent an Albert Heijn with a 'name' and 'x', 'y' coordinates
    '''
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    'Returns the position as an (x,y) tuple'
    def getPosition(self):
        return (self.x, self.y)


class TerminalKamer():
    '''
    A class to represent a Terminal Kamer
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        return (self.x, self.y)


def distance(xy1, xy2):
    '''
    Returns the distance between points 'xy1' and 'xy2'
    '''
    return math.sqrt(pow(xy1[0] - xy2[0], 2) + pow(xy1[1] - xy2[1], 2))


def closestAHDistance(tk, ahs):
    '''
    Returns the distance to the Albert Heijn in 'ahs' that is closest to 'tk'
    '''
    tkpos = tk.getPosition()
    ahPositions = [ah.getPosition() for ah in ahs]
    ahDistances = [distance(tkpos, ahpos) for ahpos in ahPositions]
    closestAHDistance = min(ahDistances)
    return closestAHDistance

'some Albert Heijns in Nijmegen'
albertheijns = [
    AlbertHeijn('Daalseweg', 85, 77),
    AlbertHeijn('Groenestraat', 68, 69),
    AlbertHeijn('van Schevichavenstraat', 79, 83),
    AlbertHeijn('St. Jacobslaan', 70, 58),
    AlbertHeijn('Stationsplein', 70, 82)
    ]
'the TK'
tk = TerminalKamer(75, 56)

'print the closest distance to an Albert Heijn from the TK'
print(closestAHDistance(tk, albertheijns))
