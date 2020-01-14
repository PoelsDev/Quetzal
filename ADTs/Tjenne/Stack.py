import os

class Node:
    def __init__(self, content):
        self.content = content
        self.next = None


class Stack:
    def __init__(self):
        self.dummy = Node(None)   # dummynode aan de bodem van de stack
        self.topNode = None       # pointer naar bovenste node van de stack
        self.size = 0

    def isEmpty(self):
        """
        Verteld of de queue leeg is of niet
        :return: True als leeg, anders false
         pre: stack moet bestaan
        post: /
        """
        if self.size ==0:
            return True
        return False

    def push(self, content):
        """
        Voegt item toe aan de stack
        :param content: Het item dat moet worden toegevoegd aan de stack
        :return: True als toegevoegd, anders false
        pre: stack moet bestaan
        post: item zit bovenaan op de stack
        """

        current = self.dummy
        while current.next is not None:
            current = current.next

        node = Node(content)
        current.next = node
        self.topNode = node
        self.size += 1
        return True

    def pop(self):
        """
        Popped het bovenste item van de stack en returned deze
        :return: top item
        pre: stack moet bestaan
        post: Bovenste item van stack is gepopped
        """
        current = self.dummy
        prev = None
        while current.next is not None:
            prev = current
            current = current.next

        prev.next = None
        self.topNode = prev
        to_pop = current.content
        del current
        self.size -= 1
        return to_pop

    def top(self):
        """"
        :return geeft de top van de stack
        pre: stack moet bestaan
        post: /
        """
        return self.topNode.content

    def destroy(self):
        """
        Verwijdert de hele stack
        :return: True als correct verwijdert
        pre: stack moet bestaan
        post: stack bestaat niet meer
        """
        i=0
        for i in range(self.size):
            self.pop()
        del self.topNode
        del self.size
        del self.dummy
        del self
        return True

    def traverse(self):
        """
        print alle waarden in de stack uit
        :return: None
        pre: stack moet bestaan
        post: None
        """
        current = self.dummy
        while current.next is not None:
            print(current.content)
            current = current.next
        print(current.content)


    def print(self):
        """
        maakt een dot file en een png van de stack
        :return: None
        pre: stack moet bestaan
        post: None
        """
        dot = "digraph G {\nrankdir = UD\n"
        dot += "top [style=invis]\n"
        dot += "top -> node_0 [label = top]\n"
        dot += "rankdir = LR\n"

        current = self.dummy.next
        name = "node_"
        count = 0
        while current.next is not None:
            dot += name + str(count) + " -> " + name + str(count+1) + "\n"
            count += 1
            current = current.next

        dot += "}"

        file = open("outputfiles/Stack.dot", "w")
        file.write(dot)
        file.close()

        os.system("dot outputfiles/Stack.dot -Tpng -o outputfiles/Stack.png")




# s = Stack()
#
# s.push(3)
# s.push(6)
# s.push(8)
# s.print()
#
# s.top()
# s.pop()
# s.top()
# print("o")
