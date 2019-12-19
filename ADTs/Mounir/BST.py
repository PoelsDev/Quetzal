from random import randint, choice
from string import ascii_letters

"""
    +isEmpty(): boolean
    Deze functie checkt of de binaire boom leeg is of niet.
    :return: True als de boom leeg is, anders False.
    Pre-condities: geen.
    Post-condities: Geeft een boolean terug die weergeeft of de BST leeg is of niet.
    
    +searchTreeInsert(in NewItem: TreeItemType): boolean
    Deze functie insert een newItem in de binaire boom.
    :param newItem: NewItem dat moet worden toegevoegd.
    :return: True of False (success Boolean)
    Pre-condities: De parameter newItem moet een integer, een float of een object zijn van een class met een variabel searchkey, en er maag geen andere object zitten met hetzelfde searchkey.
    Post-condities: Het object zal aan de binaire zoekboom worden toegevoegd. (Tenzij dezelfde key als een ander object)
    
    +searchTreeRetrieve(in searchKey: KeyType,out treeItem: TreeItemType)
    Deze functie zoekt een bepaalde key in de binaire zoekboom op basis van een gegeven searchKey en geeft het daarbij horende object terug.
    :param searchKey: Te zoeken key
    :return: None als er geen gevonden is, een object (treeItem) als er wel 1 gevonden is.
    Pre-condities: De parameter searchKey moet gelijk zijn aan de value van de variabel searchkey van de object die we willen zoeken.
    Post-condities: Er zal een object zijn teruggegeven met de overeenkomstige sleutel.
    
    +searchTreeDelete(in searchKey: KeyType): boolean
    Deze functie delete met een gegeven key, een object uit de boom.
    :param searchKey: De key waarvoor een te verwijderen object moet gevonden worden.
    :return: False als het mislukt is, True als het gelukt is.
    Pre-condities: De parameter searchKey moet gelijk zijn aan de value van de variabel searchkey van de object die we willen verwijderen.
    Post-condities: Het object met de overeenkomstige sleutel zal verwijdert zijn.
    
    +inorderTraverse()
    Doorloopt de boom in inorder traverse en print de __str__ method van de objecten af (TreeItemType).
    Pre-condities: geen.
    Post-condities: De boom zal (als niet leeg) in inorder traverse doorlopen worden
    
    +printsearchTree()
    //Print .dot code voor de structuur van de tree.
    
    +createDot()
    //Maakt een .dot file met de structuur van de tree.
    
    +inorderDot()
    //Maakt een .dot file met de inorder traversal van de tree.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.leftTree = None
        self.rightTree = None

    def insert(self, value):
        if self.value.getKey() > value.getKey():        #Check voor de leftTree
            if self.leftTree is not None:                 #Als die bestaat recursie
                return self.leftTree.insert(value)
            else:                                         #Als die niet bestaat toevoegen op die plaats
                self.leftTree = Node(value)
                return True
        elif self.value.getKey() < value.getKey:      #Check voor de rightTree
            if self.rightTree is not None:                #Als die bestaat dan recursie
                return self.rightTree.insert(value)
            else:                                         #Als die niet bestaat toevoegen op die plaats
                self.rightTree = Node(value)
                return True

    def find(self, searchkey):
        if self.value.getKey() == searchkey:     # Als de value van de node gelijk is aan de value die we zoeken
            return self                                 # Return de node
        elif self.value.getKey > searchkey:    # Als de value van de node groter is dan de value die we zoeken
            if self.leftTree is not None:               # We gaan eerste checken als leftTree bestaat
                return self.leftTree.find(searchkey)        # Als die bestaat gaan we recursie doen met de leftTree
            else:
                return None                            # Als die niet bestaat gaan we False terug geven (value zit er niet in de boom)
        else:                                           # Als de value van de node kleiner is dan de value die we zoeken
            if self.rightTree is not None:              # We gaan eerst checks als de rightTree bestaat
                return self.rightTree.find(searchkey)       # Als die bestaat gaan we recursie doen met de rightTree
            else:
                return None                            # Als die niet bestaat gaan we False terug geven (value zit er niet in de boom)

    def findParent(self, searchkey):
        # Hulp method om de ouder van een node met een bepaalde value te vinden
        if self.leftTree is not None:
            if self.leftTree.value.getKey() == searchkey:
                return self
        if self.rightTree is not None:
            if self.rightTree.value.getKey() == searchkey:
                return self
        if self.value.getKey() > searchkey:
            return self.leftTree.findParent(searchkey)
        elif self.value.getKey() < searchkey:
            return self.rightTree.findParent(searchkey)

    def preorder(self):
        if self is not None:
            print(self.value.getKey(), end=' ')
            if self.leftTree is not None:
                self.leftTree.preorder()
            if self.rightTree is not None:
                self.rightTree.preorder()

    def inorder(self):
        if self is not None:
            if self.leftTree is not None:
                self.leftTree.inorder()
            print(self.value.getKey(), end = ' ')
            if self.rightTree is not None:
                self.rightTree.inorder()

    def postorder(self):
        if self is not None:
            if self.leftTree is not None:
                self.leftTree.postorder()
            if self.rightTree is not None:
                self.rightTree.postorder()
            print(self.value.getKey(), end = ' ')

    def delete(self, searchkey, tree):
        # Delete van een node die geen kindjes heeft
        if self.leftTree is None and self.rightTree is None:
            if tree.root.findParent(searchkey).leftTree == self:
                tree.root.findParent(searchkey).leftTree = None
            else:
                tree.root.findParent(searchkey).rightTree = None

        # Delete van een node die leftTree heeft en geen rightTree
        if self.leftTree is not None and self.rightTree is None:
            if tree.root.findParent(searchkey).leftTree == self:
                tree.root.findParent(searchkey).leftTree = self.leftTree
            else:
                tree.root.findParent(searchkey).rightTree = self.leftTree
        # Delete van een node die rightTree heeft en geen leftTree
        if self.leftTree is None and self.rightTree is not None:
            if tree.root.findParent(searchkey).leftTree == self:
                tree.root.findParent(searchkey).leftTree = self.rightTree
            else:
                tree.root.findParent(searchkey).rightTree = self.rightTree
        # Delete van een node die rightTree en leftTree heeft
        if self.leftTree is not None and self.rightTree is not None:
            # Geval de inorder successor is de rightTree van de node
            if self.rightTree.leftTree is None:
                self.value = self.rightTree.value
                self.rightTree = self.rightTree.rightTree
            # Geval de inorder successor van de node zit meer dan 1 niveau lager dan de node
            elif self.rightTree.leftTree is not None:
                parentInorder = self.rightTree
                while parentInorder.leftTree.leftTree is not None:
                    parentInorder = parentInorder.leftTree
                inorder = parentInorder.leftTree
                self.value = inorder.value
                parentInorder.leftTree = inorder.rightTree
        return True

    def print(self):
        if self.leftTree is not None and self.rightTree is None:
            invisible = choice(ascii_letters) + str(randint(0, 999))
            print(self.value.getKey(), "--", self.leftTree.value.getKey())
            print(invisible + "[style=invis]")
            print(self.value.getKey(), "--", invisible + "[style=invis]")
            self.leftTree.print()
        elif self.rightTree is not None and self.leftTree is None:
            invisible = choice(ascii_letters) + str(randint(0, 999))
            print(invisible + "[style=invis]")
            print(self.value.getKey(), "--", invisible + "[style=invis]")
            print(self.value.getKey(), "--", self.rightTree.value.getKey())
            self.rightTree.print()
        elif self.rightTree is not None and self.leftTree is not None:
            print(self.value.getKey(), "--", self.leftTree.value.getKey())
            print(self.value.getKey(), "--", self.rightTree.value.getKey())
            self.leftTree.print()
            self.rightTree.print()

    def createDot(self, file):
        if self.leftTree is not None and self.rightTree is None:
            invisible = choice(ascii_letters) + str(randint(0, 999))
            file.write(str(self.value.getKey())+ " -- " + str(self.leftTree.value.getKey()) + "\n")
            file.write(invisible + " [style=invis]\n")
            file.write(str(self.value.getKey()) + " -- " + invisible + " [style=invis]\n")
            self.leftTree.createDot(file)
        elif self.rightTree is not None and self.leftTree is None:
            invisible = choice(ascii_letters) + str(randint(0, 999))
            file.write(invisible + "[style=invis]\n")
            file.write(str(self.value.getKey()) + " -- " + invisible + "[style=invis]\n")
            file.write(str(self.value.getKey()) + " -- " + str(self.rightTree.value.getKey()) + "\n")
            self.rightTree.createDot(file)
        elif self.rightTree is not None and self.leftTree is not None:
            file.write(str(self.value.getKey()) + " -- " + str(self.leftTree.value.getKey()) + "\n")
            file.write(str(self.value.getKey()) + " -- " + str(self.rightTree.value.getKey()) + "\n")
            self.leftTree.createDot(file)
            self.rightTree.createDot(file)

    def dotInorder(self, f):
        if self is not None:
            if self.leftTree is not None:
                self.leftTree.dotInorder(f)
            f.write(" -> " + str(self.value.getKey()))
            if self.rightTree is not None:
                self.rightTree.dotInorder(f)


class BST:
    def __init__(self):
        self.root = None
        self.dotindex = 1
        self.dotindexinorder = 1

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def searchTreeInsert(self, value):
        if isinstance(value, int) or isinstance(value, float):
            value = Test(value)
        if self.root is not None:
            if self.searchTreeRetrieve(value.getKey()) is None:
                return self.root.insert(value)
            else:
                return False
        else:
            self.root = Node(value)

    def searchTreeRetrieve(self, searchkey):
        if self.root is not None:
            return self.root.find(searchkey)
        else:
            return None

    def preorderTraverse(self):
        print("Preorder: ", end = '')
        self.root.preorder()
        print('')

    def inorderTraverse(self):
        print("Inorder: ", end = '')
        self.root.inorder()
        print('')

    def postorderTraverse(self):
        print("Postorder: ", end = '')
        self.root.postorder()
        print('')

    def searchTreeDelete(self, searchkey):
        # Geval de boom is leeg
        if self.root is None:
            return False
        if self.searchTreeRetrieve(searchkey) is None:
            return False

        elif self.root.value.getKey() == searchkey:  # Value die we willen deleten is de root van de boom
            # Root heeft geen leftTree en geen rightTree
            if self.root.leftTree is None and self.root.rightTree is None:
                self.root = None
            # Root heeft leftTree maar geen rightTree
            elif self.root.leftTree is not None and self.root.rightTree is None:
                self.root = self.root.leftTree
            # Root heeft rightTree maar geen leftTree
            elif self.root.rightTree is not None and self.root.leftTree is None:
                self.root = self.root.rightTree
            # Root heeft rightTree en leftTree
            elif self.root.leftTree is not None and self.root.rightTree is not None:
                # Geval de inorder successor is de rightTree van de root
                if self.root.rightTree.leftTree is None:
                    self.root.value = self.root.rightTree.value
                    self.root.rightTree = self.root.rightTree.rightTree
                # Geval de inorder successor van de node zit meer dan 1 niveau lager dan de node
                elif self.root.rightTree.leftTree is not None:
                    parentInorder = self.root.rightTree
                    while parentInorder.leftTree.leftTree is not None:
                        parentInorder = parentInorder.leftTree
                    inorder = parentInorder.leftTree
                    self.root.value = inorder.value
                    parentInorder.leftTree = inorder.rightTree
            return True
        # Geval de node die we willen deleten zit niet in de root

        elif self.root.value.getKey() != searchkey:
            return self.searchTreeRetrieve(searchkey).delete(searchkey, self)

    def printsearchTree(self):
        print("Graph B {")
        if self.root is not None and self.root.leftTree is None and self.root.rightTree is None:
            print(self.root.value.getKey())
        elif self.root is not None:
            self.root.print()
        print("}")

    def createDot(self):
        f = open("bst-" + str(self.dotindex) + ".dot", "w")
        f.write("Graph B {\n")
        if self.root is not None and self.root.leftTree is None and self.root.rightTree is None:
            print(str(self.root.value.getKey()) + "\n")
        elif self.root is not None:
            self.root.createDot(f)
        f.write("}\n")
        f.close()
        self.dotindex += 1

    def dotInorder(self):
        f = open("bst-inorder-" + str(self.dotindexinorder) + ".dot", "w")
        f.write("digraph B {\n")
        f.write("Inorder")
        self.root.dotInorder(f)
        f.write("\nrankdir=LR\n")
        f.write("}\n")
        f.close()
        self.dotindexinorder += 1


class Test:
    def __init__(self, key):
        self.key = key
    def getKey(self):
        return self.key

