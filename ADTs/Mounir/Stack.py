"""
    +isEmpty(): boolean
    Deze functie checkt of de Stack leeg is of niet.
    :return: True of False
    Pre-condities: geen
    Post-condities: Geeft weer of de stack leeg is of niet.

    +push(in newItem:StackItemType): boolean
    Voegt een item toe bovenop de stack.
    :param newItem: Nieuw toe te voegen item.
    :return: True of False: succes Boolean
    Pre-condities: De parameter newItem moet een object van een class met een variabel "searchkey".
    Post-condities: newItem wordt toegevoegd

    +pop(): stackItemType, boolean
    Haalt het laatste item vanop de stack eraf en geeft die weer.
    :return: Het gepopte item (None als de stack leeg is) en een succes Boolean.
    Pre-condities: geen
    Post-condities: Het bovenste item van de stack is er af gehaald en wordt teruggegeven.

    +getTop(): stackItemType, boolean
    Geeft het bovenste item van de stack.
    :return: Returnt het item (None als de stack leeg is) en een succes Boolean
    Pre-condities: geen
    Post-condities: Als de stack niet leeg is zal het bovenste item teruggegeven worden

    +printStack()
    Print .dot code voor de queue

    +createDot()
    Maakt een .dot file met code van de structuur van de queue.

"""


class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.items = [None]*maxsize
        self.nextindex = 0
        self.dotindex = 1

    def isEmpty(self):
        Check = True
        for item in self.items:
            if item is not None:
                Check = False
                break
        if Check:
            return True
        return False

    def push(self, item):
        if isinstance(item, int) or isinstance(item, float):
            item = Test(item)
        if self.nextindex == self.maxsize:
            return False
        else:
            self.items[self.nextindex] = item
            self.nextindex += 1
            return True

    def pop(self):
        if not self.isEmpty():
            front = self.items[self.nextindex-1]
            self.items[self.nextindex-1] = None
            self.nextindex -= 1
            return front
        return False

    def getTop(self):
        return self.items[self.nextindex-1]

    def printStack(self):
        print("Graph S {")
        print("Bottom [shape=record]")
        for item in self.items[:self.nextindex]:
            print(item.getKey(), "[shape=record]")
        print("rankdir = LR")
        print("}")

    def createDot(self):
        f = open("stack-" + str(self.dotindex) + ".dot", "w")
        f.write("Graph S {\n")
        f.write("Bottom [shape=record]\n")
        for item in self.items[:self.nextindex]:
            f.write(str(item.getKey()) + " [shape=record]\n")
        f.write("rankdir = LR\n")
        f.write("}\n")
        f.close()
        self.dotindex += 1

class Test:
    def __init__(self, key):
        self.searchkey = key
    def getKey(self):
        return self.searchkey