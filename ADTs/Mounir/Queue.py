"""
    +isEmpty(): boolean
    Deze functie checkt of de queue leeg is of niet.
    :return: True of False
    Pre-condities: geen
    Post-condities: Geeft met een boolean weer of de queue leeg is of niet.

    +enqueue(in newItem:QueueItemType): boolean
    Voegt een item toe aan de queue (achteraan).
    :param newItem: Nieuw toe te voegen item.
    :return: True of False
    Pre-condities: geen
    Post-condities: De parameter newItem zal toegevoegd worden aan de queue.

    +dequeue(): boolean
    Verwijdert eerste item uit de queue.
    :return: QueueFront of false
    Pre-condities: geen
    Post-condities: De queueFront wordt verwijderdt en teruggegeven als return.

    +getFront(): queueItemType, boolean
    Geeft het eerste item van de queue terug.
    Pre-condities: geen
    Post-condities: De queueFront wordt teruggegeven of False als de queue leeg is

    +printQueue()
    // Geeft .dot code voor de queue

    +traverse()
    Doorloopt de queue.
"""


class Queue:
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

    def enqueue(self, item):
        if isinstance(item, int) or isinstance(item, float):
            item = Test(item)

        if self.nextindex == self.maxsize:
            return False
        else:
            self.items[self.nextindex] = item
            self.nextindex += 1
            return True

    def dequeue(self):
        if not self.isEmpty():
            front = self.items[0]
            self.items = self.items[1:] + [None]
            self.nextindex -= 1
            return front
        return False

    def getFront(self):
        return self.items[0]

    def printQueue(self):
        if not self.isEmpty():
            print("digraph Q {")
            print("Front [shape=record]")
            for item in self.items[0:self.nextindex]:
                print(item.getKey(), "[shape=record]")
            print("Back [shape=record]")
            print("Front -> ", end='')
            print(self.items[0].getKey(), end='')
            for item in self.items[1:self.nextindex]:
                print(" ->", item.getKey(), end='')
            print(" -> Back")
            print("rankdir=LR")
            print("}")
        else:
            print("Graph Q {")
            print('"Lege queue" [shape=record]')
            print("}")

    def createDot(self):
        f = open("queue-" + str(self.dotindex) + ".dot", "w")
        if not self.isEmpty():
            f.write("digraph Q {\n")
            f.write("Front [shape=record]\n")
            for item in self.items[0:self.nextindex]:
                f.write(str(item.getKey()) + " [shape=record]\n")
            f.write("Back [shape=record]\n")
            f.write("Front -> ")
            f.write(str(self.items[0].getKey()))
            for item in self.items[1:self.nextindex]:
                f.write(" -> " + str(item.getKey()))
            f.write(" -> Back\n")
            f.write("rankdir=LR\n")
            f.write("}\n")
        else:
            f.write("Graph Q {\n")
            f.write('"Lege queue" [shape=record]\n')
            f.write("}\n")
        f.close()
        self.dotindex += 1


class Test:
    def __init__(self, key):
        self.searchkey = key

    def getKey(self):
        return self.searchkey