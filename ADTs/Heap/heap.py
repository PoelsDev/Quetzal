import os

class Node:
    def __init__(self, key, content, pos):
        self.key = key
        self.content = content
        self.left = None
        self.right = None
        self.pos = pos

class Heap:


    def __init__(self):
        """
        maakt een Heap aan (ketting implementatie)
        """
        self.size = 0
        self.root = None
        self.last = None
        self.allNodes = []
        self.printCount = 0

    def isEmpty(self):
        """
        kijkt of de heap items bevat
        :return: True als leeg, anders false
        pre: heap moet bestaan
        post: returned een bool
        """
        if self.size == 0:
            return True
        return False

    def __removenode(self, key):
        """
        verwijdert een node uit al nodes
        :param key: te key van het te verwijderen item
        :return: True als verwijdert, anders false
        pre: bst moet bestaan, key is integer
        post: self.allnodes is met één gedaald
        """
        for i in range(len(self.allNodes)):
            if self.allNodes[i].key == key:
                self.allNodes.pop(i)
                return True
        return False

    def printSorted(self):
        dot = "digraph G {\nrankdir = UD\n"

        while self.size > 2:
            dot += str(self.root.content)
            self.delete()
        last = str(self.root.content)
        self.delete()
        dot += str(self.root.content)
        dot += last

        dot += "}"

        file = open("outputfiles/Heapsorted.dot", "w")
        file.write(dot)
        file.close()
        os.system("dot outputfiles/Heapsorted.dot -Tpng -o outputfiles/Heapsorted.png")


    def __trickle_up(self, current):
        """
        zet een item op de juiste plaats in de heap na een insert
        :param current: de node waarin het geadde item zit
        :return: /
        pre: heap moet bestaan
        post: heaptop heeft de grootste waarde in de heap
        """

        possible = True

        while possible and current is not None:
            possible = False
            parent = self.__searchNode(int((current.pos-1)/2))
            if parent.key < current.key:
                temp_key = parent.key
                temp_content = parent.content
                parent.content = current.content
                parent.key = current.key
                current.key = temp_key
                current.content = temp_content
                current = parent
                possible = True

        return

    def top(self):
        """
        geeft de root van de heap (grootste waarde)
        :return: de root van de tree, als tree leeg is dan None
        pre: heap moet bestaan
        post : None
        """
        return self.root

    def __trickle_down(self):
        """
        zet de nieuwe root op de juiste plaats in de heap na een delete
        :return: /
        pre: heap moet bestaan
        post: heaptop heeft de grootste waarde in de heap
        """
        current = self.root
        possible = True

        while possible and current is not None:
            possible = False
            leftchild = self.__searchNode((current.pos*2) + 1)
            rightchild = self.__searchNode((current.pos*2) + 2)

            if leftchild is not None:
                if rightchild is not None:
                    if leftchild.key > rightchild.key and leftchild.key > current.key:
                        temp_key = current.key
                        temp_content = current.content
                        current.content = leftchild.content
                        current.key = leftchild.key
                        leftchild.key = temp_key
                        leftchild.content = temp_content
                        leftchild = current
                        possible = True
                else:
                    if leftchild.key > current.key:
                        temp_key = current.key
                        temp_content = current.content
                        current.content = leftchild.content
                        current.key = leftchild.key
                        leftchild.key = temp_key
                        leftchild.content = temp_content
                        leftchild = current
                        possible = True

            if rightchild is not None:
                if leftchild is not None:
                    if rightchild.key > leftchild.key and rightchild.key > current.key:
                        temp_key = current.key
                        temp_content = current.content
                        current.content = rightchild.content
                        current.key = rightchild.key
                        rightchild.key = temp_key
                        rightchild.content = temp_content
                        rightchild = current
                        possible = True

                else:
                    temp_key = current.key
                    temp_content = current.content
                    current.content = current.content
                    current.key = rightchild.key
                    rightchild.key = temp_key
                    rightchild.content = temp_content
                    rightchild = current
                    possible = True



    def __searchNode(self, position):
        """
        zoekt de node met een bepaalde positie in de ketting
        :param position: de positie van de gezochte node
        :return: de gevonden node
        pre: de heap moet bestaan
        post: returned altijd een node, nooit None
        """

        current = self.root
        i = 0
        for i in range(position):
            current = current.right
        return current


    def insert(self, key, content):
        """
        insert een node met key en content in de heap
        :param key: de zoeksleutel
        :param content: het op te slagen item
        :return:  True als correct geïnserted
        pre: heap moet bestaan, key is een integer
        post: node met key en item is correct toegevoegd
        """

        if self.isEmpty():
            self.root = Node(key, content, 0)
            self.last = self.root
            self.size += 1
            self.allNodes.append(Node(key, content, 0))
            return True

        if self.last is not None:
            self.last.right = Node(key, content, self.last.pos+1)
            self.last.right.left = self.last
            self.last = self.last.right
            self.allNodes.append(Node(key, content, self.last.pos+1))
        self.__trickle_up(self.last)
        self.size += 1
        return True

    def deleteHeap(self):
        while self.size != 0:
            self.delete()

    def delete(self):
        """
        delete de top van de heap en past deze correct aan
        :return: None
        pre: heap moet bestaan
        post: de heaptop is de tweede grootste waarde in de originele heap
        """

        if self.size > 2:
            new_last = None
            to_delete = self.root
            key = self.root.key
            if self.last is not None:
                new_last = self.last.left
            self.root.right.left = self.last
            if self.last is not None:
                if self.last.left is not None:
                    self.last.left.right = None
            self.root = self.last
            if self.root is not None:
                self.root.pos = 0
                self.root.right = to_delete.right
                self.root.left = None
            self.last = new_last

            self.size -= 1
            self.__removenode(key)
            del to_delete

            self.__trickle_down()
        elif self.size == 2:
            to_delete = self.root
            self.root = self.last
            self.__removenode(to_delete.key)
            del to_delete
            self.size -= 1
        else:
            to_delete = self.root
            self.root = None
            self.last = None
            self.__removenode(to_delete.key)
            del to_delete
            self.size -= 1

    def print(self):
        """
        :return: None
        zet tree om naar dot en png
        """
        dot = "digraph G {\nrankdir = LR\n"

        current = self.root
        if current is not None:
            while current.right is not None:
                dot += str(current.content) + "\n"
                dot += str(current.content) + "->" + str(current.right.content) + "\n"
                current = current.right

            dot += str(current.content)



        dot += "}"

        file = open("../../System/outputfiles/heap_" + str(self.printCount) + ".dot", "w")
        file.write(dot)
        file.close()

        os.system("dot ../../System/outputfiles/heap_" + str(self.printCount) + ".dot  -Tpng -o ../../System/outputfiles/heap_" + str(self.printCount) + ".png")
        self.printCount += 1


    def traverse(self):
        """
        traversed de ketting en returned alle content in een lijst
        :return: een lijst met alle content
        """
        allContent = []
        current = self.root

        while current.right is not None:
            allContent.append(current.content)
            current = current.right

        allContent.append(current.content)
        return allContent








# h = Heap()
# h.insert(3, 3)
# h.insert(4, 4)
# h.insert(1, 1)
# h.insert(5, 5)
# h.insert(2, 2)
# h.insert(7, 7)
# h.insert(8, 8)
#
# h.print()
#
# print("fin")



