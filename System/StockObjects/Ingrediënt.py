from System.UserObjects.hulpFunctie import *


class Ingredient:
    def __init__(self, type, vervaldatum, searchkey):
        self.vervaldatum = int(vervaldatum)
        self.type = type
        self.searchkey = int(searchkey)
        if type == "chili":
            self.prijs = 0.25
        elif type == "honing":
            self.prijs = 0.5
        elif type == "marshmallow":
            self.prijs = 0.75

    def getKey(self):
        if type(self.searchkey) is str:
            return stringToIntVal(self.searchkey)
        return self.searchkey