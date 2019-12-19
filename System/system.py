
from System.StockObjects.Stock import *
from ADTs.Table_wrapper import *


class System:
    def __init__(self):
        self.stock = Stock()
        self.werkNemers = Table("")         # adt hier aanpassen
        self.bestellingen = Table("")       # adt hier aanpassen

        self.time = 0


    def __update(self):
        return