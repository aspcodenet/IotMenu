class House:
    #Vi tillverkar hus i GREEN, RED, BLUE så ange en av dessa
    def __init__(self, address, color):
        self._address = address
        self._color = color

    def GetColor(self):
        return self._color

    def GetAddress(self):
        return self._address

h1 = House("Hejgatan 12", "Green")
h2 = House("Hejgatan 14","Green")
h3 = House("Hejgatan 15","Blue")
h1 = House("Hejgatan 12", "Green")

listOfHouses = [h1,h2,h3]



for h in listOfHouses:
    if h.GetColor() == "Green":
        print(h.GetAddress())


