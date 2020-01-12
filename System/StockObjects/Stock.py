

from System.StockObjects.Ingrediënt import Ingredient
from System.StockObjects.Chocolade_Shot import Cshot


from ADTs.Table_wrapper import *

class Stock:
    def __init__(self):
        self.wit = Table("h_sep")           # adt hier aanpassen
        self.zwart = Table("h_sep")
        self.melk = Table("h_sep")
        self.bruin = Table("h_sep")
        self.honing = Table("h_sep")
        self.chili = Table("h_sep")
        self.marshmallow = Table("h_sep")
        self.cwit = 0
        self.czwart = 0
        self.cmelk = 0
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
            elif subtype == "melk":
                count = len(self.melk.traverse())
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
                if itemSubType == "wit":
                    searchkey = int(itemDate + str(self.cwit))
                    shot = Cshot(itemSubType, itemDate, searchkey)
                    self.wit.insert(shot)
                    self.cwit += 1
                elif itemSubType == "zwart":
                    searchkey = int(itemDate + str(self.czwart))
                    shot = Cshot(itemSubType, itemDate, searchkey)
                    self.zwart.insert(shot)
                    self.czwart += 1
                elif itemSubType == "bruin":
                    searchkey = int(itemDate + str(self.cbruin))
                    shot = Cshot(itemSubType, itemDate, searchkey)
                    self.bruin.insert(shot)
                    self.cbruin += 1

                elif itemSubType == "melk":
                    searchkey = int(str(int(itemDate)) + str(self.cmelk))
                    shot = Cshot(itemSubType, itemDate, searchkey)
                    self.melk.insert(shot)
                    self.cmelk += 1
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
