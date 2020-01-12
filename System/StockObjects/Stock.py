
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
        +count(in type: type ingrediënt string, in subtype: shot type string, out: count integer)
        Bepaalt het aantal aanwezige items in de stock

        :param type: type ingrediënt (shot, honing, chili, marshmallow)
        :param subtype: welk soort shot
        :return: count, amount of remaining items of a particular type in the stock
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
        """
        +addToStock(in itemType: item type string, in ItemSubType: item subtype string, in itemDate: date string,
        in count: amount of the item integer)

        adds an amount of items to the stock

        :param itemType: type of the item added to the stock
        :param itemSubType: potential subtype of the item added to the stock
        :param itemDate: expiration date of the item added to the stock
        :param count: the amount of the item added to the stock
        :return: None
        """

        if itemType == "shot":
            while count > 0:
                searchkey = int(str(int(itemDate)) + str(self.cshot[itemSubType]))
                shot = Cshot(itemSubType, itemDate, searchkey)
                self.shot[itemSubType].insert(shot)
                self.cshot[itemSubType] += 1
                count -= 1

        else:
            while count > 0:
                searchkey = int(str(int(itemDate)) + str(self.cingredient[itemType]))
                item = Ingredient(itemType, itemDate, searchkey)
                self.ingredient[itemType].insert(item)
                self.cingredient[itemType] += 1
                count -= 1
