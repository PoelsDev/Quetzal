
from System.StockObjects.Ingrediënt import Ingredient
from System.StockObjects.Chocolade_Shot import Cshot


from ADTs.Table_wrapper import *

class Stock:
    def __init__(self):
        self.wit = Table("stack")           # adt hier aanpassen
        self.zwart = Table("stack")
        self.melk = Table("stack")
        self.bruin = Table("stack")
        self.honing = Table("stack")
        self.chili = Table("stack")
        self.marshmallow = Table("stack")
        self.cwit = 0
        self.czwart = 0
        self.cmelk = 0
        self.cbruin = 0
        self.choning = 0
        self.cchili = 0
        self.cmarshmallow = 0
        self.shot = {"wit": self.wit, "zwart": self.zwart, "melk": self.melk, "bruin": self.bruin}
        self.ingredient = {"honing": self.honing, "chili": self.chili, "marshmallow": self.marshmallow}
        self.cshot = {"wit": self.cwit, "zwart": self.czwart, "melk": self.cmelk, "bruin": self.cbruin}
        self.cingredient = {"honing": self.choning, "chili": self.cchili, "marshmallow": self.cmarshmallow}

    def count(self, type, subtype=None):
        """
        Bepaalt het aantal aanwezige items in de stock

        type: type ingrediënt (shot, honing, chili, marshmallow)
        subtype: welk soort shot
        """
        count = 0
        if type == "shot":
            count = len(self.shot[subtype].traverse())
        elif type == "marshmallow" or type == "chili" or type == "honing":
            count = len(self.ingredient[type].traverse())
        else:
            print("Unknown Type")
            return

        return count


    def addToStock(self, itemType, itemSubType, itemDate, count):
        if itemType == "shot":
            while count > 0:
                searchkey = int(itemDate + str(self.cshot[itemSubType]))
                shot = Cshot(itemSubType, itemDate, searchkey)
                self.shot[itemSubType].insert(shot)
                self.cshot[itemSubType] += 1
                count -= 1

        else:
            while count > 0:
                searchkey = int(itemDate + str(self.cingredient[itemType]))
                item = Ingredient(itemType, itemDate, searchkey)
                self.ingredient[itemType].insert(item)
                self.cingredient[itemType] += 1
                count -= 1
