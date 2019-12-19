
from System.StockObjects.Stock import *
from ADTs.Table_wrapper import *


class System:
    def __init__(self):
        self.stock = Stock()
        self.werkNemers = Table("bin")         # adt hier aanpassen
        self.gebruikers = Table("dlc")         # adt hier aanpassen

        self.bestellingen = Table("queue")       # adt hier aanpassen
        self.actieveWerknemers = Table("stack")
        self.time = 0


    def generateRapport(self):
        """
        maakt een html file aan met gegevens
        """

    def systemRun(self, inputFile):

        """
        parsed een input file, en voert de commands uit
        """





        self.time += 1