from DoubleLinkNode import DoubleLinkNode


class DoubleLinkedCircularChain:
    def __init__(self):
        self.head = None
        self.count = 0

    def retrieve(self, index):
        """
        +retrieve(in index:integer): ListItemType, boolean
        Deze functie geeft de node van de gegeven index terug.
        :param index: Index van de node die je wilt vinden.
        :return: None als er niets is gevonden, anders de gevonden node. Daarnaast ook een succes boolean.
        Pre-condities: De parameter index moet van het type (positieve, kleiner dan self.count)integer zijn.
        Post-condities: Als er een corresponderende node gevonden is, zal deze teruggegeven worden.
        """
        if index < self.count:
            if self.count == 0:
                return None, False
            elif index == 0:
                return self.head, True
            elif index > 0:
                temp = self.head.next
                for i in range(0, (index-1)):
                    temp = temp.next
                return temp, True
        else:
            print("ERROR: index out of range.")

    def insert(self, index, newItem):
        """
        +insert(in index:integer, in newItem:ListItemType): boolean
        Insert een nieuw item op de plek "index" van de ketting.
        :param index: Plek waarop een nieuwe node moet toegevoegd worden.
        :param newItem: Waarde van de nieuwe node
        :return: succes Boolean
        Pre-condities: De parameter index moet van het type (positieve, kleiner dan self.count) integer zijn.
        Post-condities: Het object newItem zal op de plaats index ingevoegd worden.
        """
        if self.count >= index:
            if self.count == 0 and self.head is None:
                self.head = DoubleLinkNode(newItem)
                self.count += 1
                return True
            elif index == self.count:
                temp = DoubleLinkNode(newItem)
                temp.next = self.head
                temp.previous = self.retrieve(index-1)[0]
                temp.previous.next = temp
                self.head.previous = temp
                self.count += 1
                return True
            elif index == 0:
                temp = DoubleLinkNode(newItem)
                temp.next = self.head
                temp.previous = self.head.previous
                self.head.previous.next = temp
                self.head.previous = temp
                self.head = temp
                self.count += 1
                return True
            else:
                temp = DoubleLinkNode(newItem)
                temp.next = self.retrieve(index)[0]
                temp.previous = temp.next.previous
                temp.next.previous = temp
                temp.previous.next = temp
                self.count += 1
                return True
        else:
            return False

    def delete(self, index):
        """
        +delete(in index:integer): boolean
        Delete een node met gegeven index.
        :param index: De index van de te verwijderen node.
        :return: succes Boolean
        Pre-condities: De parameter index moet van het type (positieve, kleiner dan self.count) integer zijn.
        Post-condities: Als er op de plaats index een item zit, zal dit verwijdert worden.
        """
        if self.head is None and self.count == 0:
            return False
        else:
            if self.count >= index:
                temp = self.retrieve(index)[0]
                temp.previous.next = temp.next
                temp.next.previous = temp.previous
                self.count = self.count-1
                return True
            return False

    def sort(self):
        """
        +sort(): boolean
        Sorteert de ketting van klein naar groot (op basis van ID)
        Pre-condities: geen.
        Post-condities: Als de lijst niet leeg is zal ze gesorteerd worden op de key van het object.
        """
        if self.isEmpty():
            return False
        else:
            changed = True
            while changed:
                changed = False
                for i in range(0, self.count - 1):
                    temp_node = self.retrieve(i)[0]
                    if temp_node.value.getKey() > temp_node.next.value.getKey():
                        self.insert(i, temp_node.next.value)
                        self.delete(i + 2)
                        changed = True
            return True

    def isEmpty(self):
        """
        +isEmpty(): boolean
        :return: True als de lijst leeg is, anders False.
        Pre-condities: geen.
        Post-condities: Je krijgt een boolean(True/False) die aanwijst of de lijst leeg is of niet.
        """
        if self.head is None:
            return True
        return False

    def getLength(self):
        """
        +getLength(): integer
        :return:
        Pre-condities: geen.
        Post-condities: Je krijgt de lengte van de lijst (0 als de lijst leeg is).
        """
        return self.count

    def traverse(self):
        """
        +traverse()
        Doorloopt de ketting.
        """
        if self.getLength() > 0:
            startValue = self.head.value.getKey()
            temp = self.head.next
            print(self.head.value)
            while temp.value.getKey() != startValue:
                print(temp.value)
                temp = temp.next

    def getIndexForKey(self, key):
        """
        +getIndexForKey(in key: int): int
        Deze functie geeft de index terug voor een gegeven key.
        Pre-condities: de key moet zich in de lijst bevinden
        Post-condities: de index voor de key wordt gereturned
        """
        temp = self.head
        endValue = self.head.previous.value.getKey()
        index = 0
        while temp.value.getKey() != endValue:
            if temp.value.getKey() == key:
                return index
            temp = temp.next
            index+=1
        if endValue == key:
            return index

    def generateDot(self):
        """
        +generateDot() genereert een string met dot-inhoud van de gelinkte ketting.
        Het plaatst links tussen alle naburige nodes.
        """
        dot = ""
        temp = self.head
        endValue = self.head.previous.value.getKey()
        while temp.value.getKey() != endValue:
            dot+=f"{temp.value.getKey()} [shape=record]\n"
            dot+=f"{temp.next.value.getKey()} [shape=record]"
            dot+=f"{temp.value.getKey()} -> {temp.next.value.getKey()}\n"
            dot+=f"{temp.value.getKey()} -> {temp.previous.value.getKey()}\n"
            temp = temp.next

        dot+=f"{temp.value.getKey()} [shape=record]\n"
        dot+=f"{temp.next.value.getKey()} [shape=record]"
        dot+=f"{temp.value.getKey()} -> {temp.next.value.getKey()}\n"
        dot+=f"{temp.value.getKey()} -> {temp.previous.value.getKey()}\n"

        dot+="rankdir=LR\n"

        return dot

    def toDot(self, filename):
        """
        +toDot()
        Geeft .dot code voor de structuur van de tree.
        """
        with open(filename, "w+") as f:
            dot = ""
            dot+="digraph g {\n"
            dot+=self.generateDot()
            dot+="}"
            f.write(dot)
