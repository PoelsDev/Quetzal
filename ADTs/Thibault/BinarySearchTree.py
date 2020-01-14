from TreeNode import TreeNode
from random import randint
from DummyObject import DummyObject
import os

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.parent = None
        self.leftTree = None
        self.rightTree = None

    def searchTreeInsert(self, newItem):
        """
        +searchTreeInsert(in NewItem: TreeItemType): boolean
        Deze functie insert een newItem in de binaire boom.
        :param newItem: NewItem dat moet worden toegevoegd.
        :return: True of False (success Boolean)
        Pre-condities: De parameter newItem moet een object met de getKey()-functie bevatten.
        Post-condities: Het object zal aan de binaire zoekboom worden toegevoegd. (Tenzij dezelfde key als een ander object)
        """
        if self.isEmpty():
            self.root = TreeNode(newItem)
        else:
            if newItem.getKey() == self.root.key.getKey():
                # self.root.newItem.add_Next(newItem)              Als de key zich al bevindt in de boom TODO: Gelinkte ketting
                return False
            elif newItem.getKey() < self.root.key.getKey():  # Als de key van het nieuwe item kleiner is dan de waarde van de key van de root
                if self.leftTree is None:  # Als er geen LeftTree is: maak een nieuwe BinarySearchTree en maak een leftTree
                    self.leftTree = BinarySearchTree()
                    self.leftTree.parent = self
                    self.leftTree.root = TreeNode(newItem)
                    return True
                else:
                    self.leftTree.searchTreeInsert(newItem)
            elif newItem.getKey() > self.root.key.getKey():  # Als de key van het nieuwe item groter is dan de waarde van de key van de root
                if self.rightTree is None:  # Als er geen rightTree is: maak een nieuwe BinarySearchTree en maak een rightTree
                    self.rightTree = BinarySearchTree()
                    self.rightTree.parent = self
                    self.rightTree.root = TreeNode(newItem)
                    return True
                else:
                    self.rightTree.searchTreeInsert(newItem)

    def searchTreeRetrieve(self, searchKey):
        """
        +searchTreeRetrieve(in searchKey: KeyType,out treeItem: TreeItemType)
        Deze functie zoekt een bepaalde key in de binaire zoekboom op basis van een gegeven searchKey en geeft het daarbij horende object terug.
        :param searchKey: Te zoeken key
        :return: None als er geen gevonden is, een object (treeItem) als er wel 1 gevonden is.
        Pre-condities: De parameter searchKey moet een object met de getKey()-functie bevatten.
        Post-condities: Er zal een object zijn teruggegeven met de overeenkomstige sleutel.
        """
        if not self.isEmpty(): # de functie doorzoekt recursief de boom
            if searchKey.getKey() == self.root.key.getKey():
                return self.root
            elif searchKey.getKey() < self.root.key.getKey():
                return self.leftTree.searchTreeRetrieve(searchKey)
            elif searchKey.getKey() > self.root.key.getKey():
                return self.rightTree.searchTreeRetrieve(searchKey)
        else:
            return None

    def getSubTreeIndex(self, searchKey):
        """
        *** ENKEL VOOR INTERN GEBRUIK ***
        +getSubTreeIndex(in searchKey: int): int
        Vergelijkt de parameter searchKey met de key in de root van de BST en geeft dan een index voor de juiste subtree.
        """
        if self.root.key.getKey() < searchKey:
            return 1
        else:
            return 0

    def searchTreeRetrieveSubTree(self, searchKey):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +searchTreeRetrieveSubTree(in searchKey: KeyType, out: BST)
        Deze functie is analoog aan de searchTreeRetrieve()-functie. Alleen returnt deze functie een SubTree i.p.v. een object.
        :param searchKey: De key waarvan de SubTree moet gezocht worden.
        :return: None als er geen gevonden is, een SubTree als de key gevonden is.
        Pre-condities: De parameter searchKey moet een getKey()-functie hebben om te werken.
        Post-condities: De functie geeft een subtree terug waarvan het object in de root de overkomstige key heeft.
        """
        if not self.isEmpty():
            if searchKey.getKey() == self.root.key.getKey():
                return self
            elif searchKey.getKey() < self.root.key.getKey():
                return self.leftTree.searchTreeRetrieveSubTree(searchKey)
            elif searchKey.getKey() > self.root.key.getKey():
                return self.rightTree.searchTreeRetrieveSubTree(searchKey)
        else:
            return None

    def searchTreeDelete(self, searchKey):
        """
        +searchTreeDelete(in searchKey: KeyType): boolean
        Deze functie delete met een gegeven key, een object uit de boom.
        :param searchKey: De key waarvoor een te verwijderen object moet gevonden worden.
        :return: False als het mislukt is, True als het gelukt is.
        Pre-condities: De parameter searchKey moet een getKey() functie hebben om te werken.
        Post-condities: Het object met de overeenkomstige sleutel zal verwijdert zijn.
        """
        if self.isEmpty():
            return False
        elif self.searchTreeRetrieve(searchKey) is None:
            return False
        else:
            temp_toDelete = self.searchTreeRetrieveSubTree(searchKey)
            # if temp_toDelete.root.key.next is None:
            if temp_toDelete.rightTree is None and temp_toDelete.leftTree is None:  # Het te verwijderen item is een leaf.
                subtreeIndex = temp_toDelete.parent.getSubTreeIndex(searchKey.getKey())
                if subtreeIndex == 0:
                    temp_toDelete.parent.leftTree = None
                else:
                    temp_toDelete.parent.rightTree = None
                temp_toDelete.parent = None
                temp_toDelete.root = None
                return True
            elif temp_toDelete.rightTree is not None and temp_toDelete.leftTree is None:  # Het te verwijderen item heeft een rechter deelboom.
                self.deleteWithRightTree(temp_toDelete)
                return True
            elif temp_toDelete.leftTree is not None and temp_toDelete.rightTree is None:  # Het te verwijderen item heeft een linker deelboom.
                self.deleteWithLeftTree(temp_toDelete)
                return True
            elif temp_toDelete.leftTree is not None and temp_toDelete.rightTree is not None:  # Het te verwijderen item heeft twee kinderen.
                self.deleteWithBothChildren(temp_toDelete)
                return True
            else:
                return False
        # else:
        #     temp_next = temp_toDelete.root.key.next.next
        #     temp_toDelete.root.key = temp_toDelete.root.key.next
        #     temp_toDelete.root.key.next = temp_next
        #     return True

    def deleteWithRightTree(self, deleteItem):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +deleteWithRightTree(in deleteItem: TreeItemType)
        Deze functie wordt gebruikt in de searchTreeDelete()-functie in het geval dat het te verwijderen object enkel een rechter deelboom heeft.
        Het zal voor deze omstandigheid een specifieke verwijdering uitvoeren.
        :param deleteItem: Het te verwijderen item.
        Pre-condities & post-condities n.v.t. wegens intern gebruik.
        """
        deleteItem = self.searchTreeRetrieveSubTree(deleteItem.root.key)

        if deleteItem.parent is None:
            new_tree = deleteItem.rightTree
            deleteItem.root = new_tree.root
            deleteItem.rightTree = new_tree.rightTree
            deleteItem.leftTree = new_tree.leftTree
            if deleteItem.rightTree is not None:
                deleteItem.rightTree.parent = deleteItem
            if deleteItem.leftTree is not None:
                deleteItem.leftTree.parent = deleteItem
        else:
            deleteItem.rightTree.parent = deleteItem.parent
            if deleteItem.rightTree.root.key.getKey() < deleteItem.parent.root.key.getKey():
                deleteItem.parent.leftTree = deleteItem.rightTree
            else:
                deleteItem.parent.rightTree = deleteItem.rightTree

    def deleteWithBothChildren(self, deleteItem):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +deleteWithBothChildren(in deleteItem: TreeItemType)
        Deze functie wordt gebruikt in de searchTreeDelete()-functie in het geval dat het te verwijderen object twee deelbomen heeft.
        Het zal voor deze omstandigheid (m.b.v. de searchTreeLeftSuccessor()-functie) een specifieke verwijdering uitvoeren.
        :param deleteItem: Het te verwijderen object.
        Pre-condities & post-condities n.v.t. wegens intern gebruik.
        """
        deleteItem = self.searchTreeRetrieveSubTree(deleteItem.root.key)

        if deleteItem.rightTree.rightTree is None and deleteItem.rightTree.leftTree is None:
            temp = deleteItem.rightTree.root.key
            deleteItem.root = deleteItem.rightTree.root
            self.searchTreeRetrieveSubTree(temp).rightTree = None
        elif deleteItem.rightTree.rightTree is not None and deleteItem.rightTree.leftTree is None:
            temp = deleteItem.rightTree.root
            deleteItem.rightTree.rightTree.parent = deleteItem
            deleteItem.rightTree = deleteItem.rightTree.rightTree
            deleteItem.root = temp
        elif deleteItem.rightTree.rightTree is None and deleteItem.rightTree.leftTree is not None:
            temp = deleteItem.rightTree.searchTreeLeftSuccessor()
            if temp.rightTree is not None:
                deleteItem.rightTree.rightTree = temp.rightTree
                deleteItem.rightTree.searchTreeLeftSuccessor().parent = deleteItem.rightTree
                deleteItem.root = deleteItem.rightTree.searchTreeLeftSuccessor().root
            else:
                deleteItem.root = deleteItem.rightTree.searchTreeLeftSuccessor().root
                self.searchTreeRetrieveSubTree(temp.root.key).rightTree.searchTreeLeftSuccessor().parent = None
                self.searchTreeRetrieveSubTree(temp.root.key).rightTree.searchTreeLeftSuccessor().root = None
        elif deleteItem.rightTree.rightTree is not None and deleteItem.rightTree.leftTree is not None:
            temp = deleteItem.rightTree.searchTreeLeftSuccessor()
            if temp.rightTree is not None:
                deleteItem.rightTree.searchTreeLeftSuccessor().rightTree.parent = deleteItem.rightTree
                deleteItem.rightTree.leftTree = deleteItem.rightTree.searchTreeLeftSuccessor().rightTree
                deleteItem.root = temp.root
            else:
                deleteItem.rightTree.leftTree = None
                deleteItem.root = temp.root

    def deleteWithLeftTree(self, deleteItem):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +deleteWithLeftTree(in deleteItem: TreeItemType)
        Deze functie wordt gebruikt in de searchTreeDelete()-functie in het geval dat het te verwijderen object enkel een linker deelboom heeft.
        Het zal voor deze omstandigheid een specifieke verwijdering uitvoeren.
        :param deleteItem: Het te verwijderen item.
        Pre-condities & post-condities n.v.t. wegens intern gebruik.
        """
        deleteItem = self.searchTreeRetrieveSubTree(deleteItem.root.key)

        if deleteItem.parent is None:
            new_tree = deleteItem.leftTree
            deleteItem.root = new_tree.root
            deleteItem.rightTree = new_tree.rightTree
            deleteItem.leftTree = new_tree.leftTree
            if deleteItem.rightTree is not None:
                deleteItem.rightTree.parent = deleteItem
            if deleteItem.leftTree is not None:
                deleteItem.leftTree.parent = deleteItem
        else:
            deleteItem.leftTree.parent = deleteItem.parent
            if deleteItem.leftTree.root.key.getKey() < deleteItem.parent.root.key.getKey():
                deleteItem.parent.leftTree = deleteItem.leftTree
            else:
                deleteItem.parent.rightTree = deleteItem.rightTree

    def searchTreeLeftSuccessor(self):
        """
        ** ENKEL VOOR INTERN GEBRUIK **

        +searchTreeLeftSuccessor(): BST
        Zoekt de inorder successor(-subTree) nadat er al 1 maal naar rechts gegaan is.
        :return: Boom waarin de successor zich in de root bevindt.
        Pre-condities & post-condities n.v.t. wegens intern gebruik.
        """
        if self.leftTree is None:
            return self
        else:
            return self.leftTree.searchTreeLeftSuccessor()

    def isEmpty(self):
        """
        +isEmpty(): boolean
        Deze functie checkt of de binaire boom leeg is of niet.
        :return: True als de boom leeg is, anders False.
        Pre-condities: geen.
        Post-condities: Geeft een boolean terug die weergeeft of de BST leeg is of niet.
        """
        if self.root is None and self.parent is None:
            return True
        return False

    def getRootData(self):
        """
        +getRootData(): TreeItemType, boolean
        Deze functie returnt het object van de root van de binaire boom waarin het wordt aangeroepen.
        :return: None als de boom leeg is, de rootdata als de boom niet leeg is. Daarnaast ook nog een succes boolean.
        Pre-condities: geen.
        Post-condities: Als de BST niet leeg is zal de data van het item in de root weergegeven worden (__str__-method)
        """
        if self.isEmpty():
            return None, False
        return self.root.key, True

    def setRootData(self, newItem):
        """
        +setRootData(in newItem: TreeItemType): boolean
        Dit is dezelfde als de getRootData()-functie, alleen verandert dit de rootdata. Creëert een nieuwe node met daarin newItem als de boom
        leeg is.
        :param newItem: Nieuwe rootobject
        :return: een succes Boolean
        Pre-condities: De parameter newItem moet een getKey()-functie hebben.
        Post-condities: De inhoud van de root waarvan deze functie is aangeroepen zal veranderd zijn.
        """
        if self.isEmpty():
            self.searchTreeInsert(newItem)
            return True
        if self.root.key.getKey() == newItem.getKey():
            self.root.key = newItem
            return True
        else:
            return False

    def getLeftSubtree(self):
        """
        +getLeftSubtree(): BST
        Geeft de linkse subTree.
        :return: Een lege binaire boom als de boom leeg is, anders de linkse Subtree.
        Pre-condities: geen.
        Post-condities: Als de BST niet leeg is zal de leftTree gereturnd worden. Anders zal er een lege boom teruggegeven worden.
        """
        if self.isEmpty() or self.leftTree is None:
            return BinarySearchTree()
        return self.leftTree

    def getRightSubtree(self):
        """
        +getRightSubtree(): BST
        Geeft de rechtse subTree.
        :return: Een lege binaire boom als de boom leeg is, anders de rechtse Subtree.
        Pre-condities: geen.
        Post-condities: Als de BST niet leeg is zal de rightTree gereturnd worden. Anders zal er een lege boom teruggegeven worden.
        """
        if self.isEmpty() or self.leftTree is None:
            return BinarySearchTree()
        return self.rightTree

    def inorderTraverse(self):
        """
        +inorderTraverse()
        Doorloopt de boom in inorder traverse en print de __str__ method van de objecten af (TreeItemType).
        Pre-condities: geen.
        Post-condities: De boom zal (als niet leeg) in inorder traverse doorlopen worden.
        """
        if not self.isEmpty():
            if self.leftTree is not None:
                self.leftTree.inorderTraverse()
            print(self.root.key)
            if self.rightTree is not None:
                self.rightTree.inorderTraverse()

    def printsearchTree(self):
        """
        +printsearchTree()
        Geeft .dot code voor de structuur van de tree.
        """
        pass

    def __str__(self):
        lines = printTree(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    def generateDot(self):
        """
        *** ENKEL VOOR INTERN GEBRUIK ***
        +generateDot()
        Deze functie genereert een string met daarin de inhoud van een .dot file. De functie voegt in preorder traversal de
        juiste nodes en links toe aan de string. De functie gaat recursief over zijn deelbomen om zo de dot-string te creëren.
        De string wordt vervolgens gereturned.
        """
        dot = ""
        link = "--"

        if not self.isEmpty():

            dot+="\n"

            # Basisgeval
            if self.leftTree is None:
                dot+=f"\n\"node{self.root.key.getKey()}-left\" [label=\"\", style=invis]\n"
                dot+=str(self.root.key.getKey())
                dot+= f" {link} \"node{self.root.key.getKey()}-left\" [style=invis]"
            else:
                dot+=str(self.root.key.getKey())
                dot+=f" {link} {str(self.leftTree.root.key.getKey())}"

            dot += "\n"
            if self.rightTree is None:
                dot+=f"\"node{self.root.key.getKey()}-right\" [label=\"\", style=invis]\n"
                dot+=str(self.root.key.getKey())
                dot+= f" {link} \"node{self.root.key.getKey()}-right\" [style=invis]"
            else:
                dot+=str(self.root.key.getKey())
                dot+=f" {link} {str(self.rightTree.root.key.getKey())}"

            dot+="\n"

            # recursieve stap
            if self.leftTree is not None:
              dot += self.leftTree.generateDot()
            if self.rightTree is not None:
                dot += self.rightTree.generateDot()

            return dot

    def toDot(self, filename):
        """
        +toDot()
        Deze functie genereert een volwaardige dot-file aan de hand van de generateDot() functie.
        """
        with open(filename, "w+") as f:
            f.write("graph G {\n")
            f.write(self.generateDot())
            f.write("\n}")


def printTree(tree, curr_index, index=False, delimiter='-'):
    if tree is None or tree.isEmpty():
        return [], 0, 0, 0

    line1 = []
    line2 = []
    node_repr = str(tree.root.key.getKey())

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        printTree(tree.leftTree, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        printTree(tree.rightTree, 2 * curr_index + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end

# bt = BinarySearchTree()
# # bt.searchTreeInsert(DummyObject(8))
# # bt.searchTreeInsert(DummyObject(4))
# # bt.searchTreeInsert(DummyObject(2))
# # bt.searchTreeInsert(DummyObject(6))
# # bt.searchTreeInsert(DummyObject(1))
# # bt.searchTreeInsert(DummyObject(3))
# # bt.searchTreeInsert(DummyObject(5))
# # bt.searchTreeInsert(DummyObject(7))
# # bt.searchTreeInsert(DummyObject(12))
# # bt.searchTreeInsert(DummyObject(10))
# # bt.searchTreeInsert(DummyObject(14))
# # bt.searchTreeInsert(DummyObject(9))
# # bt.searchTreeInsert(DummyObject(11))
# # bt.searchTreeInsert(DummyObject(13))
# # bt.searchTreeInsert(DummyObject(15))
#
# bt.searchTreeInsert(DummyObject(10))
# bt.searchTreeInsert(DummyObject(5))
# bt.searchTreeInsert(DummyObject(9))
# print(bt)
# bt.inorderTraverse()
# bt.toDot("output.dot")
# os.system("dot -Tps output.dot -o dotOutput.ps")
# bt.searchTreeInsert(DummyObject(12))
# bt.searchTreeDelete(DummyObject(10))
# print(bt)
# bt.inorderTraverse()
# bt.toDot("output1.dot")
# os.system("dot -Tps output1.dot -o dotOutput1.ps")
#
# # bt.toDot("output.dot")
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# #
# # bt.searchTreeDelete(DummyObject(1))
# # bt.toDot("output.dot")
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # bt.searchTreeDelete(DummyObject(2))
# # bt.toDot("output.dot")
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # bt.searchTreeDelete(DummyObject(3))
# # bt.toDot("output.dot")
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # bt.searchTreeDelete(DummyObject(4))
# # bt.searchTreeDelete(DummyObject(5))
# # bt.searchTreeDelete(DummyObject(6))
# # bt.searchTreeDelete(DummyObject(7))
# # bt.searchTreeDelete(DummyObject(8))
# # bt.searchTreeDelete(DummyObject(9))
# # bt.toDot("output.dot")
# # os.system("dot -Tps output.dot -o dotOutput.ps")
# # bt.searchTreeDelete(DummyObject(10))
# # bt.toDot("output.dot")
# # os.system("dot -Tps output.dot -o dotOutput.ps")
