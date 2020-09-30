from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class PlayerType(Enum):
    Goalie = 1
    Defence = 2
    Forward = 3


class Gender(Enum):
    Male = 1
    Female = 2


class House:
    #Vi tillverkar hus i GREEN, RED, BLUE så ange en av dessa
    def __init__(self, address, color):
        if len(address) <= 1:
            raise ValueError("Address kan inte vara tomt")
        self._address = address
        self._color = color

    def SetNewAddress(self, address):
        if len(address) <= 1:
            raise ValueError("Address kan inte vara tomt")
        self._address = address

    def GetColor(self):
        return self._color

    def GetAddress(self):
        return self._address

listOfHouses=[]
while True:
    try:
        w = 1/0
        ad = input("Ange address")
        col = Color.GREEN
        h1 = House(ad, col)
        listOfHouses.append(h1)
    except Exception as  ex:
        #
        print(f"{ex.args}")




h2 = House("Hejgatan 14",Color.GREEN)
h3 = House("Hejgatan 15",Color.BLUE)





for h in listOfHouses:
    if h.GetColor() == Color.GREEN:
        print(h.GetAddress())


#for h in listOfHouses:
#    if h.GetColor() == "GREEN":
#        print(h.GetAddress())