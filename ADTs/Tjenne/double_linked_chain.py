import os

class Node:
    def __init__(self, content, key, prev=None, next=None):
        """

        :param content: de op te slagen item/waarde
        :param key: de searchkey
        :param prev: pointer naar vorige node in chain
        :param next: pointer naar volgende node in chain
        """
        self.content = content
        self.key = key
        self.next = next
        self.prev = prev


class DLC:
    def __init__(self):
        self.chain = Node(None, None, None, None)  # dummy
        self.size = 0

    def isEmpty(self):
        """
        Verteld of de chain leeg is of niet
        :return: True als leeg, anders false
        pre: chain moet bestaan
        post: /
        """
        if self.size == 0:
            return True
        return False

    def add(self, content, key):
        """
        Voegt item toe aan chain
        :param content: key van het toe te voegen item
        :return: True als toegevoegd
        pre: chain moet bestaan, key is een integer
        post: node met item zit in de chain
        """

        node = Node(content, key)

        if self.size == 0:
            self.chain = node
            node.prev = node
            node.next = node
            self.size += 1
            return True


        else:
            current = self.chain
            while current.next != self.chain:
                current = current.next

            current.next = node
            node.prev = current
            node.next = self.chain
            self.chain.prev = node
            self.size += 1
            return True



    def pop(self, key):
        """
        Verwijdert item uit de chain
        :param key: waarde van het te verwijderen item
        :return: True als toegevoegd, False als niet toegevoegd
        pre: chain moet bestaan, key is een integer
        post: Node met zelfde key is verwijdert uit de chain
       """
        current = self.chain
        prev = None

        if current.key == key:
            prev = current.prev
            current.prev.next = current.next
            current.next.prev = prev
            self.chain = current.next
            del current
            self.size -= 1
            return True

        while current.next != self.chain:
            prev = current
            current = current.next
            if current.key == key:
                prev.next = current.next
                current.next.prev = prev
                del current
                self.size -= 1
                return True
        return False

    def bubbleSort(self):
        """
        Sorteerd de chain op basis van de bubblesort. Van klein naar groot...
        :return: None
        pre: chain moet bestaan
        post: chain is gesorteerd van klein naar groot
        """

        sorted = False
        while not sorted:
            i = 0
            current = self.chain
            while i < self.size:
                start = self.chain
                while current.next != start:
                    if current.key > current.next.key:
                        temp_key = current.key
                        temp_content = current.content
                        current.key = current.next.key
                        current.content = current.next.content
                        current.next.content = temp_content
                        current.next.key = temp_key
                        current = current.next
                    else:
                        break

                i+=1
                current = self.chain
                for j in range(i):
                    current = current.next

            current = self.chain
            start = self.chain
            sorted = True
            while current.next != start:
                if current.next.key < current.key:
                    sorted = False
                current = current.next

    def traverse(self):
        """
        traversed de chain en returned een lijst met de waarden
        :return: een lijst met alle waarden
        pre: chain moet bestaan
        post: None
        """
        current = self.chain
        allItems = []

        while current.next != self.chain:
            allItems.append(current.content)
            current = current.next

        allItems.append(current.content)
        return allItems

    def retrieve(self, key):
        """
        zoekt in de chain naar item met zelfde key en returned deze
        :param key: de searchkey van het gezochte item
        :return: None als er geen key match gevonden is, anders het opgelagen item
        pre: chain moet bestaan, key is integer
        post: None
        """
        current = self.chain

        if current.key == key:
            return current.content

        while current.next != self.chain:
            current = current.next
            if current.key == key:
                return current.content
        return None

    def destroy(self):
        """
        Maakt de chain helemaal leeg, en verwijdert deze
        :return: True als correct verwijdert
        pre: chain moet bestaan
        post: chain bestaat niet meer
        """
        current = self.chain
        current.prev.next = None
        current.prev = None

        while current.next is not None:
            current.content = None
            current.key = None
            current.prev = None
            next = current.next
            current.next = None
            del current
            current = next
        del self.chain
        del self.size
        del self
        return True

    def print(self, forHashmap=False):  # werkt niet correct als er meerdere items zijn met zelfde key
        """
        maakt een dot file en png aan van de chain
        :return: None
        pre: chain moet bestaan
        post: /
        """
        dot = ""
        if not forHashmap:

            dot = "digraph G {\nrankdir = UD\n"
            dot += "rankdir = LR\n"
            dot += "front [style=invis]\n"
            dot += "front -> node_0 [label = \"front\"]\n"

        current = self.chain.next
        name = "node_"
        count = 0
        while count < self.size-1:
            dot += str(current.content) + " -> " + str(current.next.content) + "\n"
            dot += str(current.next.content) + " -> " + str(current.content) + "\n"
            count += 1
            current = current.next
        dot += str(current.content) + " -> " + str(self.chain.next.content) + "\n"
        dot += str(self.chain.next.content) + " -> " + str(current.content) + "\n"

        if forHashmap:
            return dot
        dot += "}"


        file = open("outputfiles/Dlc.dot", "w")
        file.write(dot)
        file.close()

        os.system("dot outputfiles/Dlc.dot -Tpng -o outputfiles/Dlc.png")










# d = DLC()
# d.add(6, 6)
# d.add(2, 2)
# d.add(4,4)
# d.add(1, 1)
# d.add(3, 3)
# d.destroy()
# d.bubbleSort()
# print("o")
#
# d.pop(1)
#
# print("o")




