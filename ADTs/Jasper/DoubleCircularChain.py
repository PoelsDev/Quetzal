from DoubleLinkedNode import DoubleLinkedNode


class DoubleCircularChain:
    def __init__(self):
        self.head = None
        self.nodeCount = 0

    def isEmpty(self):
        """
        +isEmpty(): boolean
        Checks if the double circular chain is empty
        :return:Boolean query whether the chain is empty or not
        """
        if self.head == None:
            return True
        else:
            return False

    def getLength(self):
        """
        +getLength(): integer
        Gives how many items(nodes) there are in the chain
        :return: the count of nodes (items)
        """
        if self.isEmpty() or self.nodeCount == 0:
            return 0
        else:
            return self.nodeCount

    def retrieve(self, index):
        """
        +retrieve(in index: integer, out dataItem: ListItemType, out success: boolean)
        Retrieves the item that is located in the chain on the given index
        :param index: index of item that will be retrieved
        :return:True or False whether chain is empty, if not empty it returns True and the item on given index under
        "dataItem"
        """
        if self.nodeCount == 0:
            return False
        elif index == 0:
            dataItem = self.head
            return True, dataItem
        elif index > 0:
            dataItem = self.head.next
            for i in range(0, index-1):
                dataItem = dataItem.next
            return True, dataItem

    def insert(self, index, newItem):
        """
        +insert(in index: integer, in newItem:ListItemType, out success: boolean)
        Adds a new item to the chain on the given index
        :param index: index where the new item will be added in the chain
        :param newItem: the item that will be inserted in the chain
        :return: Boolean query, True or False, whether the function was completed successfully
        """
        if index <= self.nodeCount:
            if self.nodeCount == 0 and self.head == None:
                self.head = DoubleLinkedNode(newItem)
                self.nodeCount += 1
                return True
            elif index == self.nodeCount:
                temp = DoubleLinkedNode(newItem)
                temp.next = self.head
                temp.previous = self.retrieve(index-1)[1]
                temp.previous.next = temp
                self.head.previous = temp
                self.nodeCount += 1
                return True
            elif index == 0:
                temp = DoubleLinkedNode(newItem)
                temp.next = self.head
                temp.previous = self.head.previous
                self.head.previous = temp
                self.head.previous.next = temp
                self.head = temp
                self.nodeCount += 1
                return True
            else:
                temp = DoubleLinkedNode(newItem)
                temp.next = self.retrieve(index)[1]
                temp.previous = temp.next.previous
                temp.next.previous = temp
                temp.previous.next = temp
                self.nodeCount += 1
                return True
        else:
            return False

    def delete(self, index):
        """
        +delete(in index: integer, out success: boolean)
        Deletes item on the position index in the chain
        :param index: index of item that will be deleted
        :return:True or False whether function was successful or not
        """
        if self.nodeCount == 0:
            return False
        else:
            temp = self.retrieve(index)[1]
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
            self.nodeCount -= 1
            return True

    def sort(self):
        """
        +sort(): boolean
        Sorts the items in the chain based on a value, from the smallest value to the largest value
        :return: Boolean query whether the function was successful or not
        """
        if self.isEmpty():
            return False
        else:
            changed = True
            while changed:
                changed = False
                for i in range(0, self.nodeCount-1):
                    temp = self.retrieve(i)[1]
                    if temp.searchKey.getKey() > temp.next.searchKey.getKey():
                        self.insert(i, temp.next.searchKey)
                        self.delete(i+2)
                        changed = True
            return True

    def toDot(self, filename):
        open(filename, "w+")
        with open(filename, 'w') as file:
            file.write("digraph G {\n")
            file.write("node" + str(self.head.searchKey.getKey()) + ' [label="' + str(self.head.searchKey.getKey()) + '"]\n')
            self.head.next.toDotFile(file, self.head.searchKey.getKey())
            file.write("rankdir=LR")
            file.write("}")
