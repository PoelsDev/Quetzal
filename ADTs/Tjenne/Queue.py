import os

class Node:
    def __init__(self, content):
        self.next = None
        self.content = content


class Queue:
    def __init__(self):
        self.head = None    # pointer naar de eerst volgende waarde in queue
        self.size = 0

    def isEmpty(self):
        """
        Verteld of de queue leeg is of niet
        :return: True als leeg, anders false
        pre: queue moet bestaan
        post: /
        """
        if self.size == 0:
            return True
        return False

    def enqueue(self, content):
        """
        voegt item toe aan queue
        :param content: toe te voegen waarde
        :return: True als toegevoegd
        pre: key is een integer, node met content is achteraan toegevoegd aan de queue
        """
        if self.head is None:
            self.head = Node(content)
            self.size += 1
            return True

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(content)
        self.size += 1
        return True

    def dequeue(self):
        """
        Verwijdert eerste item uit queue en returned dit
        :return: het verwijderde item
        pre: queue moet bestaan
        post: node vooraan in de queue is verwijdert
        """

        to_pop = self.head
        ret_val = self.head.content
        self.head = self.head.next
        del to_pop.content
        del to_pop
        self.size -= 1
        return ret_val


    def front(self):
        """
        returned de waarde van het eerste item in de queue
        :return: de self.head waarde
        pre: queue moet bestaan
        post: /
        """
        return self.head


    def traverse(self):
        """
        traversed de queue en print de waarden
        :return: een lijst met alle items
        pre: queue moet bestaan
        post: None
        """
        current = self.head
        allContent = []
        while current.next is not None:
            allContent.append(current.content)
            current = current.next
        allContent.append(current.content)
        return allContent


    def destroy(self):

        """
        Verwijdert de hele queue
        :return: None
        pre: queue moet bestaan
        post: queue is helemaal verwijdert
        """

        while self.head is not None:
            self.dequeue()

        del self

    def print(self):
        """
        zet queue om naar dot en png
        :return: None
        """
        dot = "digraph G {\nrankdir = UD\n"
        dot += "front [style=invis]\n"
        dot += "front -> node_0 [label = \"front\"]\n"
        dot += "rankdir = LR\n"

        current = self.head
        name = "node_"
        count = 0
        while current.next is not None:
            dot += name + str(count) + " -> " + name + str(count+1) + "\n"
            count += 1
            current = current.next

        dot += "}"

        file = open("outputfiles/Queue.dot", "w")
        file.write(dot)
        file.close()

        os.system("dot outputfiles/Queue.dot -Tpng -o outputfiles/Queue.png")









# q = Queue()
# q.enqueue(3, 3)
# q.enqueue(5, 5)
# q.enqueue(7, 7)
# q.print()
# print("o")
# #
# q.dequeue()
# print("e")
# #
# q.destroy()
# print("fin")
