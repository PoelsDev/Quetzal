

from System.StockObjects.Ingrediënt import Ingredient
from System.StockObjects.Chocolade_Shot import Cshot


from ADTs.Table_wrapper import *

class Stock:
    def __init__(self):
        self.toppings = Table("stack")  # honing, chili en marshmallow
        self.shots = Table("stack")           # adt hier aanpassen



    def count(self, type, subtype=None):
        """
        Bepaalt het aantal aanwezige items in de stock

        type: type ingrediënt (shot, topping)
        subtype: welk soort shot of topping
        """
        if type == "shot":
            #self.shots.traverse(subtype)
            return

        elif type == "topping":
            # self.toppings.traverse(subtype)
            return

        else:
            # traverse, return vector met maps voor elk soort topping
            return


    def addToStock(self, itemType, itemSubType, itemDate, count):
        if itemType == "honing" or itemType == "marshmallow" or itemType == "chili":
             while count > 0:
                 item = Ingredient(itemType, itemDate)
                 self.toppings.insert(item, itemDate)
                 count -= 1
             return

        elif itemType == "shot":
            while count > 0:
                shot = Cshot(itemSubType, itemDate)
                self.shots.insert(shot, itemDate)
                count -= 1
            return

