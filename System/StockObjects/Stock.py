

from System.StockObjects.Ingrediënt import Ingredient
from System.StockObjects.Chocolade_Shot import Cshot
from System.StockObjects.Chocolade_Melk import Cmelk



from ADTs.Table_wrapper import *

class Stock:
    def __init__(self):
        self.toppings = Table("dlc")  # honing, chili en marshmallow
        self.melk = Table("dlc")           # adt hier aanpassen
        self.shot = Table("dlc")           # adt hier aanpassen



    def count(self, type):
        """
        Bepaald het aantal aanwezige items in de stock

        type: type ingrediënt
        """
        if type == "melk":
            # getsize
            return

        elif type == "shot":
            # traverse, return vector aan met maps voor elk type shot
            return

        else:
            # traverse, return vector met maps voor elk soort topping
            return



