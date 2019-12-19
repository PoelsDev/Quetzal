from ADTs.BinarySearchTree import BinarySearchTree
from ADTs.Tjenne.Queuez import Queue
from ADTs.Thibault.Stack import Stack
from ADTs.Tjenne.heap import Heap
from ADTs.Tjenne.hashmap import Hashmap
from ADTs.Mounir.DLC import DLC

class Table:

    def __init__(self, type):
        """
        constructor van de adt
        :param type: string die bepaald welk type de adt is: (stack,queue,heap,dlc,binTree,hlin,hquad,hsep)
        pre: type is een string die een adt beschrijft
        post: adt wordt correct aangemaakt
        """
        self.type = type
        self.data = None

        if type == "stack":
            self.data = Stack()         # kies hier welke adts
        elif type == "heap":
            self.data = Heap()
        elif type == "queue":
            self.data = Queue()
        elif type == "dlc":
            self.data = DLC()
        elif type == "binTree":
            self.data = BinarySearchTree()
        elif type == "hash_lin":
            self.data = Hashmap(51, "lin")
        elif type == "hash_quad":
            self.data = Hashmap(51, "quad")
        elif type == "hash_sep":
            self.data = Hashmap(51, "sep")
        else:
            print("Unknown type: " + type)

    def insert(self, content, key=None):
        """
        insert een item met een key in de adt
        :param content: het op te slagen item
        :param key: de eventuele zoekwaarde
        :return: True als correct geïnserted
        """

        if self.type == "stack":
            self.data.push(content)
        elif self.type == "heap":
            self.data.insert(key, content)
        elif self.type == "queue":
            self.data.enqueue(content, key)
        elif self.type == "dlc":
            self.data.add(content, key)
        elif self.type == "binTree":
            self.data.insert(key, content)

    def delete(self, key=None):
        """
        delete een item uit de adt, welke hangt af van het type natuurlijk
        :param key: eventuele key als nodig
        :return: True als correct verwijdert, anders false
        """
        if self.type == "stack":
            self.data.pop()
        elif self.type == "heap":
            self.data.delete()
        elif self.type == "queue":
            self.data.dequeue()
        elif self.type == "dlc":
            self.data.pop(key)
        elif self.type == "binTree":
            self.data.delete(key)

    def print(self):
        """
        maakt een dotfile en png aan van de adt
        :return: None
        pre: Adt moet correct aangemaakt zijn
        post: None
        """
        self.data.print()

    def isEmpty(self):
        """
        kijkt of er elementen in de adt zijn opgeslagen
        :return: True als empty, anders false
        pre: adt moet correct aangemaakt zijn
        post: returned een bool
        """
        return self.data.isEmpty()

    def retrieve(self, key=None):
        """
        zoekt in de adt naar een item met matchende key (als adt dit toestaat), voor stack en heap = top, queue = front
        :param key: de eventuele key van het gezochte item
        :return: het gevonden item, als er geen match is dan None
        pre: adt moet correct aangemaakt zijn, key is integer
        post: None
        """
        if self.type == "stack":
            self.data.top()
        elif self.type == "heap":
            self.data.top()
        elif self.type == "queue":
            self.data.front()
        elif self.type == "dlc":
            self.data.retrieve(key)
        elif self.type == "binTree":
            self.data.find(key)


    def traverse(self):
        """
        print een traverse van de adt
        :return: None
        pre: Adt moet correct aangemaakt zijn
        post: None
        """
        if self.type == "stack":
            self.data.traverse()
            return
        elif self.type == "heap":
            # nog niet geïmplementeerd
            return
        elif self.type == "queue":
            self.data.traverse()
            return
        elif self.type == "dlc":
            self.data.traverse()
            return
        elif self.type == "binTree":
            self.data.inorderTraverse()




# A = Table("queue")
# A.insert(1, 1)
# A.insert(5, 5)
# A.insert(3, 3)
# A.print()
# A.traverse()
# A.delete(1)
# A.print()
# print("fin")
