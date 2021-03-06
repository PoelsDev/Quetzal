
from System.StockObjects.Stock import *
from ADTs.Table_wrapper import *
from System.UserObjects.Gebruiker import *
from System.UserObjects.Werknemer import *
from System.UserObjects.Bestelling import *


class System:
    def __init__(self):
        self.stock = Stock()
        self.werkNemers = Table("h_lin")         # adt hier aanpassen
        self.gebruikers = Table("h_lin")         # adt hier aanpassen

        self.bestellingen = Table("queue")       # adt hier aanpassen
        self.vrije_Werknemers = Table("stack")
        self.bestellingendone = Table("234")

        self.actieve_Werknemers = []
        self.nieuweBestellingen = []

        # HTML Member Variables #
        self.html_string = ""
        self.html_count = 0

        self.time = 0

        self.lastSave = None        # last system save, voor eventuele undo

    def updateHTML(self):
        """
        +updateHTML() update de html string op basis van de voorbije gebeurtenissen (dit elke nieuwe tijdseenheid)
        """
        newline = "\n"
        # TABLE HEADER
        if self.time == 0:
            self.html_string += "<tr>"
            self.html_string += "<th> tijdstip </th>" + newline
            self.html_string += "<th> Stack </th>" + newline
            for werknemer in self.werkNemers.traverse():
                self.html_string += f"<th> {werknemer.voornaam} {werknemer.achternaam} </th>" + newline
            self.html_string += "<th>Nieuwe Bestellingen</th>" + newline
            self.html_string += "<th>Wachtende Bestellingen</th>" + newline
            self.html_string += "<th>Wit</th>" + newline
            self.html_string += "<th>Melk</th>" + newline
            self.html_string += "<th>Bruin</th>" + newline
            self.html_string += "<th>Zwart</th>" + newline
            self.html_string += "<th>Honing</th>" + newline
            self.html_string += "<th>Marshmallow</th>" + newline
            self.html_string += "<th>Chili</th>" + newline

        # TABLE DATA
        self.html_string += "<tr>" + newline
        # Tijdstip
        self.html_string += "<td>" + str(self.time) + "</td>" + newline
        self.html_string += "<td>|"
        # Werknemer Stack
        for item in reversed(self.vrije_Werknemers.traverse()):
            self.html_string += str(item.getKey()) + " "
        self.html_string += "</td>" + newline
        lst2 = self.werkNemers.traverse()
        # Workorders
        for werknemer in lst2:
            if werknemer.currentOrder != None:
                self.html_string += "<td>" + str(werknemer.load) + "</td>" + newline
            else:
                self.html_string += "<td></td>" + newline
                
        # Nieuwe bestellingen
        if len(self.nieuweBestellingen) != 0:
            self.html_string += "<td>"
            for bestelling in self.nieuweBestellingen:
                if self.nieuweBestellingen[len(self.nieuweBestellingen)-1] != bestelling:
                    self.html_string += str(bestelling.credits) + ", "
                else:
                    self.html_string += str(bestelling.credits)
            self.html_string += "</td>" + newline
        else:
            self.html_string += "<td></td>" + newline

        # Wachtende bestellingen
        if len(self.bestellingen.traverse()) != 0:
            self.html_string += "<td>"
            for bestelling in self.bestellingen.traverse():
                if self.bestellingen.traverse()[len(self.bestellingen.traverse())-1] != bestelling:
                    self.html_string += str(bestelling.credits) + ", "
                else:
                    self.html_string += str(bestelling.credits)
            self.html_string += "</td>" + newline
        else:
            self.html_string += "<td></td>" + newline

        # Wit
        self.html_string += "<td>" + str(self.stock.count("shot", "wit")) + "</td>" + newline
        # Melk
        self.html_string += "<td>" + str(self.stock.count("shot", "melk")) + "</td>" + newline
        # Bruin
        self.html_string += "<td>" + str(self.stock.count("shot", "bruin")) + "</td>" + newline
        # Zwart
        self.html_string += "<td>" + str(self.stock.count("shot", "zwart")) + "</td>" + newline
        # Honing
        self.html_string += "<td>" + str(self.stock.count("honing")) + "</td>" + newline
        # Marshmallow
        self.html_string += "<td>" + str(self.stock.count("marshmallow")) + "</td>" + newline
        # Chili
        self.html_string += "<td>" + str(self.stock.count("chili")) + "</td>" + newline
        self.html_string += "</tr>" + newline


    def generateHTML(self):
        """
        +generateHTML() maakt een html-file aan voor de gegevens
        """
        newline = "\n"
        output = ""
        output += "<html>" + newline
        output += "<style> table, td, th, tr {border-collapse: collapse; border: 1px solid black; empty-cells: show} </style>" + newline
        output += "<body>" + newline
        output += "<table>" + newline
        output += self.html_string
        output += "</table>" + newline
        output += "</body>" + newline
        output += "</html>" + newline
        with open(str(f"Log{self.time}.html"), "w+") as f:
            f.write(output)
        self.html_count += 1

    def __parseInitStock(self, line):
        """
        +__parseInitStock(in line: command line)
        parses command and adds items to the stock
        :param line: command line
        """
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
        """
        +__parseInitUser(in line: command line)
        parses command and adds user (gebruiker)
        :param line: command line
        """
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

        id = stringToIntVal(voornaam+achternaam)
        gebruiker = Gebruiker(id, voornaam, achternaam, email)


        key = stringToIntVal(email)
        self.gebruikers.insert(gebruiker, int(key))



    def __parseInitEmployee(self, line):
        """
        +__parseInitEmployee(in line: command line)
        parses command and adds employee (werknemer)
        :param line: command line
        """
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

        id = stringToIntVal(voornaam+achternaam)
        werknemer = Werknemer(id, voornaam, achternaam, workload)

        self.werkNemers.insert(werknemer, id)
        self.vrije_Werknemers.insert(werknemer)


    def __splitCommand(self, command):
        """
        +__splitCommand(in command: string, out splittedCommand: vector)
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
        +__commandHandler(in line: command, out: 0 or 1)
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

            order = Bestelling(user, date, ingredients, self.stock)
            if order.enoughstock:
                self.bestellingen.insert(order, stringToIntVal(order.getKey()))
                self.nieuweBestellingen.append(order)
                self.bestellingendone.insert(order, stringToIntVal(order.getKey()))
            else:
                print("Not enough stock")
            return 1

        elif command[1] == "stock":
            if command[2] == "shot":
                subType = command[3]
                amount = int(command[4])
                date = ""

                for i in range(5, wordCount):
                    date += command[i]

                self.stock.addToStock("shot", subType, date[:-1], amount)

                return 1
            elif command[2] == "honing" or command[2] == "chili" or command[2] == "marshmallow":
                subtype = command[2]
                amount = int(command[3])
                date = ""

                for i in range(4, wordCount):
                    date += command[i]

                self.stock.addToStock(subtype, None, date, amount)

                return 1

        elif command[1] == "log" or command[1] == "log\n":
            self.updateHTML()
            self.generateHTML()
            print("Log generated")
            return 1

        else:
            print("Unknown command")
            return 0


    def update(self, updateTime):
        """
        +update(in updateTime: boolean)
        wordt elke nieuwe time unit opgeroepen. Updated de progress
        :param updateTime: boolean query
        """
        if updateTime:

            # update de html string
            self.updateHTML()

            amountFreed = 0
            for w in range(len(self.actieve_Werknemers)):
                werker = self.actieve_Werknemers[w-amountFreed]
                if werker.workOrder():
                    self.vrije_Werknemers.insert(werker, werker.id)
                    self.actieve_Werknemers.pop(w-amountFreed)
                    amountFreed += 1

            # maakt de lijst met nieuwe bestellingen leeg
            while not len(self.nieuweBestellingen) == 0:
                self.nieuweBestellingen.pop()


        while not self.bestellingen.isEmpty() and not self.vrije_Werknemers.isEmpty():
            werker = self.vrije_Werknemers.delete()
            bestelling = self.bestellingen.delete()
            werker.giveOrder(bestelling)
            self.actieve_Werknemers.append(werker)






    def systemRun(self, inputFile):
        """
        +systemRun(in inputeFile: input text file)
        parsed een input file, en voert de commands uit
        :param inputFile: text file
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

            if int(line[0]) > self.time:
                for i in range(self.time, int(line[0])):
                    self.update(True)
                self.time = int(line[0])

            self.__commandHandler(line)
            self.update(False)


        # het verder afwerken eens dat alle commands gebeurt zijn
        while not (len(self.actieve_Werknemers) == 0 and self.bestellingen.isEmpty()):
            self.update(True)
            self.time += 1

s = System()

s.systemRun("inputFiles/system.txt")





