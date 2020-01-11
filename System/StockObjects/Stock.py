

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

        count = 0

        if type == "shot":
            allShots = self.shots.traverse()
            for shot in allShots:
                if shot.soort == subtype:
                    count += 1
            return

        elif type == "topping":
            allToppings = self.toppings.traverse()
            for topping in allToppings:
                if topping.type == subtype:
                    count += 1
            return

        print("Unkknown type")
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

