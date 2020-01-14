# Treenodes
class Node:
    def __init__(self, content, key):
        self.content = content
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

import os

class Tree:
    def __init__(self):

        self.size = 0
        self.allNodes = []  # voor de todot te versimpelen
        self.root = None    # pointer naar de root van de tree

    def isEmpty(self):
        """
        Verteld of de tree leeg is of niet
        :return: True als leeg, anders false
        pre: Tree moet bestaan
        post: /
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

    def insert(self, key, content, root=None):
        """
        Voegt item toe aan tree
        :param content: key van toe te voegen item
        :param root: huidige root, nodig voor recursie
        :return: True als toegevoegd, False als niet toegevoegd
        pre: Tree moet bestaan, key is een integer
        post: node met key en item is correct toegevoegd
        """

        if root is None:
            root = self.root

        if self.size == 0:
            self.root = Node(content, key)
            self.allNodes.append(self.root)
            self.size += 1
            return

        elif key >= root.key:
            if root.right is None:
                root.right = Node(content, key)
                root.right.parent = root
                self.allNodes.append(root.right)
                self.size += 1
                return
            else:
                self.insert(key, content, root.right)
                return

        else:
            if root.left is None:
                root.left = Node(content, key)
                root.left.parent = root
                self.allNodes.append(root.left)
                self.size += 1

                return

            else:
                self.insert(key, content, root.left)
                return

    def delete(self, key):
        """
        Verwijdert item uit tree
        :param key: key van het te verwijderen item
        :return: false if not found, True if found and deleted
        pre: Tree moet bestaan, key is een integer
        post: node met zelfde key is verwijdert uit tree
        """
        root = self.find(key, True)
        if root is False:
            return False

        parent = root.parent

        #  root deleten
        if self.root == root:
            found = False
            current = root
            if root.left is not None:
                current = root.left
                while not found:
                    if current.right is not None:
                        current = current.right
                    else:
                        found = True

                if root.left != current:
                    current.parent.right = None
                    current.left = root.left
                    current.left.parent = current

                current.parent = None
                if root.right is not None:
                    current.right = root.right
                    current.right.parent = current

                self.__removenode(self.root.key)
                self.root = current
                del root
                self.size -= 1

            elif root.right is not None:
                current = root.right
                while not found:
                    if current.left is not None:
                        current = current.left
                    else:
                        found = True

                if root.right != current:
                    current.parent.left = None
                    current.right = root.right
                    current.right.parent = current

                current.parent = None
                if root.left is not None:
                    current.left = root.left
                    current.left.parent = current
                self.__removenode(self.root.key)
                self.root = current
                del root
                self.size -= 1
                return True
            else:
                self.__removenode(self.root.key)
                self.root = None
                del root
                self.size -= 1
                return True




        # leaf zonder kinderen
        if root.left is None and root.right is None:
            if root == parent.left:
                parent.left = None
                self.__removenode(self.root.key)
                del root
                self.size -= 1
                return True
            else:
                parent.right = None
                self.__removenode(self.root.key)
                del root
                self.size -= 1
                return True

        # één kind
        if root.left is None:
            child = root.right
            parent.right = child
            child.parent = parent
            self.__removenode(self.root.key)
            self.size -= 1
            del root
            return True

        if root.right is None:
            child = root.left
            parent.left = child
            child.parent = parent
            self.__removenode(self.root.key)
            del root
            self.size -= 1
            return True

        # twee kinderen (inorder succesor)
        found = False
        current = root
        if root.left is not None:
            current = root.left
            while not found:
                if current.right is not None:
                    current = current.right
                else:
                    found = True

        if parent.right == root:
            parent.right = current
            if current == root.left:
                current.left = None
            else:
                current.parent.right = None
                current.left = root.left
                root.left.parent = current
            current.parent = parent

            if root.right is not None:
                root.right.parent = current
            current.right = root.right
            self.__removenode(self.root.key)
            del root
            self.size -= 1
            return True
        else:
            parent.left = current
            if current == root.left:
                current.left = None
            else:
                current.left = root.left
                root.left.parent = current
            current.parent = parent
            current.right = root.right
            if root.right is not None:
                root.right.parent = current
            self.__removenode(self.root.key)

            del root
            self.size -= 1
            return True

    def find(self, key, forDel=False):
        """
        Zoekt in de tree naar het item dat bij het gegeven key hoort
        :param key:de key die bij het gevraagde item hoort
        :param forDel: bool die bepaald of de node moet worden gereturned of de content van de node
        :return: False als key niet bestaat in tree, het item als deze is gevonden
        pre: Tree moet bestaan, key is een integer
        post: /
        """
        found = False
        root = self.root
        while not found:
            if key > root.key:
                if root.right is None:
                    print("Key not found")
                    return False
                root = root.right
            elif key < root.key:
                if root.left is None:
                    print("Key not found")
                    return False
                root = root.left

            elif root.key == key:
                found = True

        if forDel:
            return root
        return root.content


    def inorderTraverse(self, root=None, start=True):
        """
        print de inorderTraversal
        :param root: huidige root
        :param start: bool voor bepalen te bepalen of we root nog moeten gelijkstellen
        :return: None
        pre: Tree moet bestaan
        post: /
        """

        if start and root is None:
            root = self.root

        if root is not None:
            self.inorderTraverse(root.left, False)  # altijd eerst zo ver mogelijk naar links

            print(root.key)

            self.inorderTraverse(root.right, False)  # dan zo ver mogelijk naar rechts



    def print(self):
        """
        zet tree om naar dot en png
        :return: None
        """
        dot = "digraph G {\nrankdir = UD\n"

        for i in range(len(self.allNodes)):
            if self.allNodes[i].left is not None:
                dot += str(self.allNodes[i].key) + " -> " + str(self.allNodes[i].left.key) + "\n"
            if self.allNodes[i].right is not None:
                dot += str(self.allNodes[i].key) + " -> " + str(self.allNodes[i].right.key) + "\n"

        dot += "}"

        file = open("outputfiles/BinTree.dot", "w")
        file.write(dot)
        file.close()

        os.system("dot outputfiles/BinTree.dot -Tpng -o outputfiles/BinTree.png")





# t = Tree()
#
# t.insert(5, 5)
# t.insert(2, 2)
# t.insert(1, 1)
# t.insert(3, 3)
# t.insert(7, 7)
# t.insert(6, 6)
# t.insert(8, 8)
# t.print()
#
# p = t.find(8)
# print(p)
# #
# # t.inorderTraverse()
#
# t.insert(5, 5)
# t.insert(7, 7)
# t.insert(6, 6)
# t.insert(8, 8)
# t.insert(4, 4)
#
#
# print(t.delete(7))  # twee childs
# t.inorderTraverse()
# print(t.delete(6))  # root
# t.inorderTraverse()
# print(t.delete(1))  # 1 child
# t.inorderTraverse()




