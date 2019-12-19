class Queue:
    def __init__(self, size):
        self.front = None
        self.back = None
        self.items = [None] * size
        self.size = size

    def getFront(self):
        """
        +getFront(): queueItemType, boolean
        Geeft het eerste item van de queue terug + een boolean die succes aanduidt.
        Pre-condities: geen
        Post-condities: Geeft een tuple met daarin als eerste item de queueFront en als tweede
        item een boolean die aanduidt of de front gevonden is of niet.
        """
        if self.isEmpty():
            return None, False
        return self.items[self.front]

    def isEmpty(self):
        """
        +isEmpty(): boolean
        Deze functie checkt of de queue leeg is of niet.
        :return: True of False
        Pre-condities: geen
        Post-condities: Geeft met een boolean weer of de queue leeg is of niet.
        """
        if self.front is None and self.back is None:
            return True
        return False

    def dequeue(self):
        """
        +dequeue(): boolean
        Verwijdert eerste item uit de queue.
        :return: True of False
        Pre-condities: geen
        Post-condities: De queueFront wordt verwijderd.
        """
        if self.isEmpty():
            return False
        else:
            self.items[self.front] = None
            self.front += 1
            return True

    def enqueue(self, newItem):
        """
        +enqueue(in newItem:QueueItemType): boolean
        Voegt een item toe aan de queue (achteraan).
        :param newItem: Nieuw toe te voegen item.
        :return: True of False
        Pre-condities: geen
        Post-condities: De parameter newItem zal toegevoegd worden aan de queue.
        """
        if self.isEmpty():
            self.front = 0
            self.back = 0
            self.items[0] = newItem
            return True
        else:
            if self.back+1 == self.size:
                return False
            else:
                self.back += 1
                self.items[self.back] = newItem
                return True

    def traverse(self):
        """
        +traverse()
        Doorloopt de queue.
        """
        for item in self.items:
            if item is not None:
                print(item)

    def generateDot(self):
        """
        +generateDot()
        Genereert .dot code
        """
        dot = ""
        dot +="front [style=invis]\n"
        for item in self.items:
            if item is not None:
                dot+=str(item.getKey()) + " " + "[shape=record]\n"
        dot+="back [style=invis]\n"
        dot+="front ->"
        for item in self.items:
            if item is not None:
                dot+=f" {item.getKey()} ->"
        dot+=" back\n"
        dot+="rankdir=LR\n"

        return dot

    def toDot(self, filename):
        """
        +toDot() creeërt een .dot-file aan de hand van de gegenereerde dot-code uit +generateDot().
        """
        with open(filename, "w+") as f:
            dot = ""
            dot+="digraph g {\n"
            dot+=self.generateDot()
            dot+="}"
            f.write(dot)
