

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
        elif type == "mashmallow":
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
                searchkey = itemDate + str(count)
                shot = Cshot(itemSubType, itemDate, searchkey)
                if itemType == "wit":
                    self.wit.insert(shot)
                elif itemType == "zwart":
                    self.zwart.insert(shot)
                elif itemType == "bruin":
                    self.bruin.insert(shot)
                count -= 1
        else:
            while count > 0:
                searchkey = itemDate + str(count)
                item = Ingredient(itemType, itemDate, searchkey)
                if itemType == "honing":
                    self.honing.insert(item)
                elif itemType == "marshmallow":
                    self.marshmallow.insert(item)
                elif itemType == "chili":
                    self.chili.insert(item)
                count -= 1
