from ADTs.BinarySearchTree import BinarySearchTree
from ADTs.Tjenne.Queue import Queue
from ADTs.Thibault.Stack import Stack
from ADTs.Thibault.TwoThreeFourTree import TwoThreeFourTree
from ADTs.Tjenne.heap import Heap
from ADTs.Tjenne.hashmap import Hashmap
from ADTs.Mounir.DLC import DLC
from ADTs.Mounir.TwoThreeTree import Tree



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
        elif type == "23":
            self.data = Tree()
        elif type == "binTree":
            self.data = BinarySearchTree()
        elif type == "h_lin":
            self.data = Hashmap(51, "lin")
        elif type == "h_quad":
            self.data = Hashmap(51, "quad")
        elif type == "h_sep":
            self.data = Hashmap(51, "sep")
        elif type == "234":
            self.data = TwoThreeFourTree()
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
            self.data.insert(content.getKey(), content)
        elif self.type == "queue":
            self.data.enqueue(content)
        elif self.type == "dlc":
            self.data.insert(content)
        elif self.type == "binTree":
            self.data.searchTreeInsert(content)
        elif self.type == "23":
            self.data.insertItem(content)
        elif self.type == "h_lin" or self.type == "h_quad" or self.type == "h_sep":
            self.data.insert(content, content.getKey())
        elif self.type == "234":
            self.data.insertItem(content)

    def delete(self, key=None):
        """
        delete een item uit de adt, welke hangt af van het type natuurlijk
        :param key: eventuele key als nodig
        :return: True als correct verwijdert, anders false
        """
        if self.type == "stack":
           return self.data.pop()
        elif self.type == "heap":
            self.data.delete()
        elif self.type == "queue":
            return self.data.dequeue()
        elif self.type == "dlc":
            self.data.delete(key)
        elif self.type == "binTree":
            if key == None:
                key = self.data.inorderTraverse()[0]
            self.data.searchTreeDelete(key)
        elif self.type == "23":
            self.data.deleteItem(key)
        elif self.type == "234":
            if key == None:
                key = self.data.inorder()[0].getKey()
            self.data.deleteItem(key)
        elif self.type == "h_lin" or self.type == "h_sep" or self.type == "h_quad":
            self.data.delete(key)

    def print(self):
        """
        maakt een dotfile en png aan van de adt
        :return: None
        pre: Adt moet correct aangemaakt zijn
        post: None
        """
        if self.type == "dlc" or self.type == "23":
            self.data.createDot()
        else:
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
            return self.data.searchTreeRetrieve(key)
        elif self.type == "23":
            self.data.retrieveItem(key)
        elif self.type == "234":
            return self.data.retrieveItem(key)


    def traverse(self):
        """
        print een traverse van de adt
        :return: None
        pre: Adt moet correct aangemaakt zijn
        post: None
        """
        if self.type == "stack":
            return self.data.traverse()
        elif self.type == "heap":
            return self.data.traverse()
        elif self.type == "queue":
            return self.data.traverse()
        elif self.type == "dlc":
            return self.data.traverse()
        elif self.type == "binTree":
            return self.data.inorderTraverse()
        elif self.type == "23":
            return self.data.traverse()
        elif self.type == "234":
            return self.data.inorder()
        elif self.type == "h_lin" or self.type == "h_quad" or self.type == "h_sep":
            return self.data.traverse()




# A = Table("queue")
# A.insert(1, 1)
# A.insert(5, 5)
# A.insert(3, 3)
# A.print()
# A.traverse()
# A.delete(1)
# A.print()
# print("fin")
