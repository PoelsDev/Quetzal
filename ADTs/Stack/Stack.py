from ADTs.Stack.Node import Node


class Stack:
    def __init__(self):
        self.listHead = None

    def isEmpty(self):
        """
        +isEmpty(): boolean
        Deze functie checkt of de Stack leeg is of niet.
        :return: True of False
        Pre-condities: geen
        Post-condities: Geeft weer of de stack leeg is of niet.
        """
        if self.listHead is None:
            return True
        return False

    def push(self, newItem):
        """
        +push(in newItem:StackItemType): boolean
        Voegt een item toe bovenop de stack.
        :param newItem: Nieuw toe te voegen item.
        :return: True of False: succes Boolean
        Pre-condities: De parameter newItem moet een object zijn met de getKey()-method.
        Post-condities:
        """
        if self.isEmpty():
            self.listHead = Node(newItem)
            return True
        else:
            temp = Node(newItem, self.listHead)
            self.listHead = temp
            return True

    def pop(self):
        """
        +pop(): stackItemType, boolean
        Haalt het laatste item vanop de stack eraf en geeft die weer.
        :return: Het gepopte item (None als de stack leeg is) en een succes Boolean.
        Pre-condities: geen
        Post-condities: Het bovenste item van de stack is er af gehaald en wordt teruggegeven.
        """
        if self.isEmpty():
            return None
        else:
            temp = self.listHead
            self.listHead = temp.next
            return temp.value

    def top(self):
        """
        +top(): stackItemType, boolean
        Geeft het bovenste item van de stack.
        :return: Returnt het item (None als de stack leeg is) en een succes Boolean
        Pre-condities: geen
        Post-condities: Als de stack niet leeg is zal het bovenste item teruggegeven worden.
        """
        if not self.isEmpty():
            return self.listHead, True
        return None, False

    def traverse(self):
        """
        +traverse()
        Doorloopt de Stack in volgorde van top tot bottom.
        """
        lst = []
        temp = self.listHead
        while temp != None:
            #print(temp.value)
            lst.append(temp.value)
            temp = temp.next

        return lst

    def generateDot(self):
        """
        *** ENKEL VOOR INTERN GEBRUIK ***
        +generateDot()
        Deze functie genereert .dot-code op basis van de item in de stack.
        """
        dot=""
        dot+="bottom [shape=record]\n"
        temp = self.listHead
        keyList = []
        while temp is not None:
            keyList.append(temp.value.getKey())
            temp = temp.next
        for key in reversed(keyList):
            dot+=f"{key} [shape=record]\n"

        dot+="rankdir=LR\n"

        return dot

    def print(self, filename):
        """
        +print()
        Geeft de .dot code van de stack.
        """
        with open(filename, "w+") as f:
            dot = ""
            dot+="graph g {\n"
            dot+=self.generateDot()
            dot+="}"
            f.write(dot)
