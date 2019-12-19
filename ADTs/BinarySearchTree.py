from BinaryTreeNode import BinaryTreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.parent = None
        self.leftTree = None
        self.rightTree = None

    def __str__(self):
        lines = printTree(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    def isEmpty(self):
        """
        +isEmpty(): Boolean
        Checks if tree is empty
        :return:Boolean query whether the tree is empty or not
        """
        if self.root == None and self.parent == None:
            return True
        else:
            return False

    def searchTreeRetrieve(self, searchKey):
        """
        +searchTreeRetrieve(in searchKey: Keytype, out treeItem: TreeItemType, out success: boolean)
        Based on given searchKey it will give back the treenode of the binary search tree that contains this searchKey
        :param searchKey: searchKey of node you want to be returned
        :return: Treenode that contains this searchKey
        """
        if self.isEmpty():
            return False
        else:
            if searchKey.getKey() == self.root.searchKey.getKey():
                return self.root
            elif searchKey.getKey() < self.root.searchKey.getKey():
                return self.leftTree.searchTreeRetrieve(searchKey)
            else:
                return self.rightTree.searchTreeRetrieve(searchKey)

    def findTree(self, searchKey):
        """
        +findTree(in searchKey: Keytype, out treeItem: binary search tree)
        Based on given searchKey it will give back the subtree that contains the treenode that contains the given searchKey
        :param searchKey: searchKey of node of subtree you want to be returned
        :return:  SubTree that contains the treenode that contains the searchKey
        """
        if self.root != None and self.root.searchKey.getKey() == searchKey.getKey():
            return self
        elif self.leftTree != None and self.root.searchKey.getKey() > searchKey.getKey():
            return self.leftTree.findTree(searchKey)
        elif self.rightTree != None and self.root.searchKey.getKey() < searchKey.getKey():
            return self.rightTree.findTree(searchKey)
        else:
            return None

    def searchTreeInsert(self, newItem):
        """
        +searchTreeInsert(in newItem: TreeItemType, out success: boolean)
        Adds a new item (newItem) to the binary search tree and it will be added based on its searchKey
        :param newItem: An object that has a particular value which will serve as a searchKey
        :return: boolean query whether the searchTreeInsert was successful or not
        """
        if self.isEmpty():
            self.root = BinaryTreeNode(newItem)
            return True
        else:
            if newItem.getKey() == self.root.searchKey.getKey():
                print("<< Item met zelfde searchKey zit al in boom >>")
                return False
                # self.root.addNext(newItem) moet nog geimplementeerd worden
            elif newItem.getKey() < self.root.searchKey.getKey():
                if self.leftTree == None:
                    self.leftTree = BinarySearchTree()
                    self.leftTree.parent = self
                    self.leftTree.root = BinaryTreeNode(newItem)
                    return True
                else:
                    self.leftTree.searchTreeInsert(newItem)
            elif newItem.getKey() > self.root.searchKey.getKey():
                if self.rightTree == None:
                    self.rightTree = BinarySearchTree()
                    self.rightTree.parent = self
                    self.rightTree.root = BinaryTreeNode(newItem)
                    return True
                else:
                    self.rightTree.searchTreeInsert(newItem)

    def searchTreeDelete(self, searchKey):
        """
        +searchTreeDelete(in searchKey: KeyType, out success:boolean)
        Deletes treenode from binary search tree based on its given searchKey
        :param searchKey: searchKey of treenode you want to delete from the binary search tree
        :return: boolean query whether the delete was successful or not
        """
        deletedTree = self.findTree(searchKey)
        if deletedTree == None:
            return False

        # leaf
        elif deletedTree.leftTree == None and deletedTree.rightTree == None:
            if searchKey.getKey() < deletedTree.parent.root.searchKey.getKey():
                deletedTree.parent.leftTree = None
                deletedTree.parent = None
                return True
            elif searchKey.getKey() > deletedTree.parent.root.searchKey.getKey():
                deletedTree.parent.rightTree = None
                deletedTree.parent = None
                return True
        # has only a left child
        elif deletedTree.leftTree != None and deletedTree.rightTree == None:
            # is left of its parent
            if deletedTree.parent == None:
                new_tree = deletedTree.leftTree
                deletedTree.root = new_tree.root
                deletedTree.leftTree = new_tree.leftTree
                deletedTree.rightTree = new_tree.rightTree
                if deletedTree.leftTree != None:
                    deletedTree.leftTree.parent = deletedTree
                if deletedTree.rightTree != None:
                    deletedTree.rightTree.parent = deletedTree
            elif searchKey.getKey() < deletedTree.parent.root.searchKey.getKey():
                # link the leftTree of its parent to the left tree of itself
                deletedTree.parent.leftTree = deletedTree.leftTree
                # link the parent of its left child to its parent
                deletedTree.leftTree.parent = deletedTree.parent
                deletedTree.leftTree = None
                deletedTree.parent = None
                return True
            # right of is parent
            elif searchKey.getKey() > deletedTree.parent.root.searchKey.getKey():
                deletedTree.parent.rightTree = deletedTree.leftTree
                deletedTree.leftTree.parent = deletedTree.parent
                deletedTree.leftTree = None
                deletedTree.parent = None
                return True
        # has only a right child
        elif deletedTree.rightTree != None and deletedTree.leftTree == None:
            if deletedTree.parent == None:
                new_tree = deletedTree.rightTree
                deletedTree.root = new_tree.root
                deletedTree.leftTree = new_tree.leftTree
                deletedTree.rightTree = new_tree.rightTree
                if deletedTree.leftTree != None:
                    deletedTree.leftTree.parent = deletedTree
                if deletedTree.rightTree != None:
                    deletedTree.rightTree.parent = deletedTree
            elif searchKey.getKey() < deletedTree.parent.root.searchKey.getKey():
                deletedTree.parent.leftTree = deletedTree.rightTree
                deletedTree.rightTree.parent = deletedTree.parent
                deletedTree.rightTree = None
                deletedTree.parent = None
                return True
            elif searchKey.getKey() > deletedTree.parent.root.searchKey.getKey():
                deletedTree.parent.rightTree = deletedTree.rightTree
                deletedTree.rightTree.parent = deletedTree.parent
                deletedTree.rightTree = None
                deletedTree.parent = None
                return True
        # has a right and left child
        elif deletedTree.rightTree != None and deletedTree.leftTree != None:
            inorderSuccessor = deletedTree.rightTree.mostLeftChild()
            self.searchTreeDelete(inorderSuccessor.root.searchKey)
            deletedTree.root = inorderSuccessor.root
            return True

    def mostLeftChild(self):
        """
        :return: returns smallest child under a particular node of a binary search tree
        """
        tmp = self
        while tmp.leftTree != None:
            tmp = tmp.LeftTree
        return tmp

    def getRootData(self):
        """
        +getRootData(out success:boolean): TreeItemType
        This function can be used on a tree-node to get its searchKey
        :return: If tree is empty return will be False, otherwise it will return the searchKey of the treenode on which the function was called
        """
        if self.isEmpty():
            return False
        else:
            return self.root.searchKey

    def setRootData(self, newItem):
        """
        +setRootData(in newItem: TreeItemType, out success: boolean)
        Changes the searchKey of a treenode in a not empty binary search tree
        :param searchKey:
        :return:
        """
        if self.isEmpty():
            self.searchTreeInsert(newItem)
            return True
        elif self.root.searchKey.getKey() == newItem.getKey():
            self.root.searchKey = newItem
            return True
        else:
            return False

    def getLeftSubtree(self):
        """
        +getLeftSubtree(): BinaryTree
        Gives back leftTree of root of the tree on which this function was used
        :return: False if tree is empty, the leftTree of root of tree on which function was called
        """
        if self.isEmpty():
            return BinarySearchTree()
        else:
            return self.root.leftTree

    def getRightSubtree(self):
        """
        +getRightSubtree: BinaryTree
        Gives back rightTree of root of the tree on which this function was used
        :return: False if tree is empty, the rightTree of root of tree on which function was called
        """
        if self.isEmpty():
            return BinarySearchTree()
        else:
            return self.root.rightTree

    def inorderTraverse(self):
        """
        +inorderTraverse()
        Goes trough binary tree in inorder and for each node it will print out the searchkey
        :return: prints out searchKey of node
        """
        if not self.isEmpty():
            if self.leftTree != None:
                self.leftTree.inorderTraverse()
            print(self.root.searchKey.getKey())
            if self.rightTree != None:
                self.rightTree.inorderTraverse()

    def toDot(self, filename):
        open(filename, "w+")
        with open(filename, 'w') as file:
            self.toDotFile(file)
            file.write("}")

    def toDotFile(self, file):
        if self.parent == None:
            file.write("graph G {\n")
            file.write(
                "node" + str(self.root.searchKey.getKey()) + ' [label="' + str(self.root.searchKey.getKey()) + '"]\n')
            if self.leftTree != None:
                self.leftTree.toDotFile(file)
            elif self.leftTree == None:
                file.write("dummyleftnode" + str(self.root.searchKey.getKey()-1) + ' [label="' + str(self.root.searchKey.getKey()-1) + '", style=invis]\n')
                file.write(
                "node" + str(self.root.searchKey.getKey()) + " -- dummyleftnode" + str(self.root.searchKey.getKey()-1) + " [style=invis]" + "\n")
            if self.rightTree != None:
                self.rightTree.toDotFile(file)
            elif self.rightTree == None:
                file.write("dummyrightnode" + str(self.root.searchKey.getKey()+1) + ' [label="' + str(
                    self.root.searchKey.getKey()+1) + '", style=invis]\n')
                file.write(
                "node" + str(self.root.searchKey.getKey()) + " -- dummyrightnode" + str(self.root.searchKey.getKey()+1) + " [style=invis]" + "\n")
        else:
            file.write(
                "node" + str(self.root.searchKey.getKey()) + ' [label="' + str(self.root.searchKey.getKey()) + '"]\n')
            file.write(
                "node" + str(self.parent.root.searchKey.getKey()) + " -- node" + str(self.root.searchKey.getKey()) + "\n")
            if self.leftTree != None:
                self.leftTree.toDotFile(file)
            elif self.leftTree == None:
                file.write("dummyleftnode" + str(self.root.searchKey.getKey()-1) + ' [label="' + str(
                    self.root.searchKey.getKey()-1) + '", style=invis]\n')
                file.write(
                "node" + str(self.root.searchKey.getKey()) + " -- dummyleftnode" + str(self.root.searchKey.getKey()-1) + " [style=invis]" + "\n")
            if self.rightTree != None:
                self.rightTree.toDotFile(file)
            elif self.rightTree == None:
                file.write("dummyrightnode" + str(self.root.searchKey.getKey()+1) + ' [label="' + str(
                    self.root.searchKey.getKey()+1) + '", style=invis]\n')
                file.write(
                "node" + str(self.root.searchKey.getKey()) + " -- dummyrightnode" + str(self.root.searchKey.getKey()+1) + " [style=invis]" + "\n")

