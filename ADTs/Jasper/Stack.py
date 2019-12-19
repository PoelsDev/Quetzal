from StackNode import StackNode

class Stack:
    def __init__(self):
        self.listHead = None

    def isEmpty(self):
        """
        +isEmpty(): boolean
        Checks if stack is empty
        :return: Returns boolean, if the stack is empty returns True otherwise it will return False
        """
        if self.listHead == None:
            return True
        return False

    def push(self, newItem):
        """
        +push(in newItem: StackItemType, out success: boolean)
        Adds an item to the top of the stack
        :param newItem: the item that will be added to the stack
        :return: True if function was completed successful, otherwise returns False
        """
        if self.isEmpty():
            self.listHead = StackNode(newItem)
            return True
        else:
            temp = StackNode(newItem, self.listHead)
            self.listHead = temp
            return True
        return False

    def pop(self):
        """
        +pop(out success: boolean, out stackTop: StackItemType)
        Deletes the top of the stack (last added item) and saves it
        :return:True or False whether function was completed successful and if True it will also return the deleted item
        """
        if self.isEmpty():
            return False
        else:
            stackTop = self.listHead
            self.listHead = self.listHead.next
            return True, stackTop

    def getTop(self):
        """
        +getTop(out success: boolean, out stackTop: StackItemType)
        Function will return the top of the stack under "stackTop"
        :return: Returns True or False whether function was successful, if True it will also return the top under "stackTop"
        """
        if self.isEmpty():
            return False
        else:
            stackTop = self.listHead
            return True, stackTop

    def toDot(self, filename):
        open(filename, "w+")
        with open(filename, 'w') as file:
            file.write("graph G {\n")
            file.write("bottom [shape=record]\n")
            self.listHead.toDotFile(file)
            file.write("rankdir=LR")
            file.write("}")
