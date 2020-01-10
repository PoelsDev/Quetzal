
from System.StockObjects.Stock import *
from ADTs.Table_wrapper import *


class System:
    def __init__(self):
        self.stock = Stock()
        self.werkNemers = Table("binTree")         # adt hier aanpassen
        self.gebruikers = Table("hashmap")         # adt hier aanpassen

        self.bestellingen = Table("queue")       # adt hier aanpassen
        self.actieveWerknemers = Table("stack")
        self.time = 0

        self.lastSave = None        # last system save, voor eventuele undo


    def generateRapport(self):
        """
        maakt een html file aan met gegevens
        """


    def __parseInit(self, line):
        itemType = None
        itemSubType = None
        itemCount = 0
        itemDate = ""

        i = 0
        for word in line.split():

            if i >= 3 and itemType == "shot":
                itemDate += word

            elif i == 2 and itemType == "shot":
                itemCount = int(word)

            elif i >= 2:
                itemDate += word

            elif i == 1 and itemType == "shot":
                itemSubType = word
            elif i == 1:
                itemCount = int(word)

            elif i == 0:
                itemType = word

            i += 1

        # effectief toevoegen van items aan de stock
        self.stock.addToStock(itemType, itemSubType, itemDate, itemCount)




    def systemRun(self, inputFile):


        """
        parsed een input file, en voert de commands uit
        """

        f = open(inputFile, 'r')
        adt = None
        typename = None
        adt_count = 0
        initialising = False

        lines = f.readlines()

        commands = []

        for line in range(len(lines)):

            if not (lines[line][0] == "#"):

                for word in lines[line].split():
                    if initialising and word != "start":  # als in init false, elke lijn in __parseInit steken
                        self.__parseInit(lines[line])
                        break

                    if word == "init":
                        initialising = True
                    elif word == "start":
                        initialising = False
                    else:
                        commands.append(lines[line])
                        break

        print("her")









        self.time += 1



s = System()

s.systemRun("inputFiles/testFile")
