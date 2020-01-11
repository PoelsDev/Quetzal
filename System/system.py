
from System.StockObjects.Stock import *
from ADTs.Table_wrapper import *
from System.Gebruiker import *
from System.Werknemer import *
from System.Bestelling import *


class System:
    def __init__(self):
        self.stock = Stock()
        self.werkNemers = Table("h_lin")         # adt hier aanpassen
        self.gebruikers = Table("h_lin")         # adt hier aanpassen

        self.bestellingen = Table("queue")       # adt hier aanpassen
        self.actieveWerknemers = Table("stack")
        self.time = 0

        self.lastSave = None        # last system save, voor eventuele undo

    def generateHTML(self):
        """
        Dit maakt een html-file aan voor de gegevens.
        """


    def __stringToIntVal(self, s):
        """
        zet elke char in een string om naar zijn intval en plakt deze aan elkaar om zo een key te bekomen
        :param s:
        :return:
        """
        intValString = ""

        for char in s:
            intval = ord(char)

            intValString += str(intval)

        return int(intValString)


    def __parseInitStock(self, line):
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

    def __parseInitUser(self, line):
        voornaam = ""
        achternaam = ""
        email = ""


        command = self.__splitCommand(line)
        wordCount = len(command)


        for i in range(wordCount):
            if i == 1:
                voornaam += command[i]
            elif i == 2:
                achternaam += command[i]
            elif i == wordCount - 1:
                email = command[i]

        id = self.__stringToIntVal(voornaam+achternaam)
        gebruiker = Gebruiker(id, voornaam, achternaam, email)


        key = self.__stringToIntVal(email)
        self.gebruikers.insert(gebruiker, int(key))



    def __parseInitEmployee(self, line):
        voornaam = ""
        achternaam = ""
        workload = 0

        command = self.__splitCommand(line)
        wordCount = len(command)

        for i in range(wordCount):
            if i == 1:
                voornaam += command[i]
            elif i == 2:
                achternaam += command[i]
            elif i == wordCount - 1:
                workload = int(command[i])

        id = self.__stringToIntVal(voornaam+achternaam)
        werknemer = Werknemer(id, voornaam, achternaam, workload)

        self.werkNemers.insert(werknemer, id)


    def __splitCommand(self, command):
        """
        Splitst een string op in aparte strings in een vector
        :param command: de op te splitsen string
        :return: een vector met het opgesplitste command
        """
        splittedCommand = []
        currentWord = ""
        for char in range(len(command)):
            if command[char] != ' ':
                currentWord += command[char]
            else:
                splittedCommand.append(currentWord)
                currentWord = ""

        splittedCommand.append(currentWord)

        return splittedCommand


    def __commandHandler(self, line):
        """
        Behandelt de commands na dat het systeem gestart is (stock, log, bestel)
        :param line: de command die behandelt moet worden
        :return: 0 als ongeldige input, 1 als command correct uitgevoerd is
        """

        command = self.__splitCommand(line)
        wordCount = len(command)

        if command[1] == "bestel":
            ingredients = []
            date = ""
            time = int(command[0])
            user = command[2]

            for i in range(3, wordCount):
                if 2 < i < wordCount - 5:
                    ingredients.append(command[i])
                elif i >= wordCount - 5:
                    date += command[i]

            order = Bestelling(user, date, ingredients)
            self.bestellingen.insert(order, self.__stringToIntVal(order.ID))
            return 1

        elif command[1] == "stock":
            if command[2] == "shot":
                subType = command[3]
                amount = int(command[4])
                date = ""

                for i in range(5, wordCount):
                    date += command[i]

                for i in range(amount):
                    shot = Cshot(subType, date)
                    self.stock.shots.insert(shot, int(date))
                return 1
            elif command[2] == "honing" or command[2] == "chili" or command[2] == "marshmallow":
                subtype = command[2]
                amount = int(command[3])
                date = ""

                for i in range(4, wordCount):
                    date += command[i]

                for i in range(amount):
                    topping = Ingredient(subtype, date)
                    self.stock.toppings.insert(topping, int(date))

                return 1

        elif command[1] == "log":
            self.generateHTML()
            print("Log generated")
            return 1

        else:
            print("Unknown command")
            return 0

    def systemRun(self, inputFile):
        """
        parsed een input file, en voert de commands uit
        """

        f = open(inputFile, 'r')
        initialising = False

        lines = f.readlines()

        commands = []

        for line in range(len(lines)):

            if not (lines[line][0] == "#"):

                for word in lines[line].split():
                    if initialising and word == "gebruiker":
                        self.__parseInitUser(lines[line])
                        break

                    elif initialising and word == "werknemer":
                        self.__parseInitEmployee(lines[line])
                        break

                    elif initialising and word != "start":  # als in init false, elke lijn in __parseInit steken
                        self.__parseInitStock(lines[line])
                        break


                    if word == "init":
                        initialising = True
                    elif word == "start":
                        initialising = False

                    else:
                        commands.append(lines[line])
                        break

        # vanaf hier worden de commands uitgevoerd
        for line in commands:
            self.__commandHandler(line)



s = System()

s.systemRun("inputFiles/testFile")





