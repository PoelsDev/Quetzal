

from System.StockObjects.Ingrediënt import Ingredient
from System.StockObjects.Chocolade_Shot import Cshot


from ADTs.Table_wrapper import *

class Stock:
    def __init__(self):
        self.wit = Table("stack")           # adt hier aanpassen
        self.zwart = Table("stack")
        self.bruin = Table("stack")
        self.honing = Table("stack")
        self.chili = Table("stack")
        self.marshmallow = Table("stack")
        self.cwit = 0
        self.czwart = 0
        self.cbruin = 0
        self.choning = 0
        self.cchili = 0
        self.cmarshmallow = 0
    def count(self, type, subtype=None):
        """
        Bepaalt het aantal aanwezige items in de stock

        type: type ingrediënt (shot, honing, chili, marshmallow)
        subtype: welk soort shot
        """

        count = 0

        if type == "shot":
            if subtype == "wit":
                count = len(self.wit.traverse())
            elif subtype == "zwart":
                count = len(self.zwart.traverse())
            elif subtype == "bruin":
                count = len(self.bruin.traverse())
        elif type == "marshmallow":
            count = len(self.marshmallow.traverse())
        elif type == "chili":
            count = len(self.chili.traverse())
        elif type == "honing":
            count = len(self.honing.traverse())
        else:
            print("Unknown Type")
            return

        return count


    def addToStock(self, itemType, itemSubType, itemDate, count):
        if itemType == "shot":
            while count > 0:
                if itemType == "wit":
                    searchkey = itemDate + str(self.cwit)
                    shot = Cshot(itemSubType, itemDate, searchkey)
                    self.wit.insert(shot)
                    self.cwit += 1
                elif itemType == "zwart":
                    searchkey = itemDate + str(self.czwart)
                    shot = Cshot(itemSubType, itemDate, searchkey)
                    self.zwart.insert(shot)
                    self.czwart += 1
                elif itemType == "bruin":
                    searchkey = itemDate + str(self.cbruin)
                    shot = Cshot(itemSubType, itemDate, searchkey)
                    self.bruin.insert(shot)
                    self.cbruin += 1
                count -= 1
        else:
            while count > 0:
                if itemType == "honing":
                    searchkey = itemDate + str(self.choning)
                    item = Ingredient(itemType, itemDate, searchkey)
                    self.honing.insert(item)
                    self.choning += 1
                elif itemType == "marshmallow":
                    searchkey = itemDate + str(self.cmarshmallow)
                    item = Ingredient(itemType, itemDate, searchkey)
                    self.marshmallow.insert(item)
                    self.cmarshmallow += 1
                elif itemType == "chili":
                    searchkey = itemDate + str(self.cchili)
                    item = Ingredient(itemType, itemDate, searchkey)
                    self.chili.insert(item)
                    self.cchili += 1
                count -= 1
