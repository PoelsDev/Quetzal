class PrototypeQueue:
    def __init__(self, size):
        self.front = None
        self.back = None
        self.items = [None] * size
        self.size = size

    def enqueue(self, newItem):
        """
        +enqueue(in newItem: QueueItemType, out success: boolean)
        Adds a new item to the end of the Queue
        :param newItem: The new item that will be added Queue
        :return: Boolean query, True or False whether the function was successful
        """
        if self.isEmpty():
            self.front = 0
            self.back = 0
            self.items[self.back] = newItem
            return True
        elif self.size == (self.back)+1:
            return False
        else:
            self.back += 1
            self.items[self.back] = newItem
            return True

    def isEmpty(self):
        """
        +isEmpty(): boolean
        Checks if the queue is empty
        :return:True if queue is empty, False if not
        """

        if self.front == None:
            return True
        else:
            return False

    def dequeue(self):
        """
        +dequeue(out success:boolean, out queueFront: QueueItemType)
        Deletes the front of the queue, the first item that was added to the queue
        :return:Boolean query whether function was successful, if function was successful it will also return the deleted item
        under "queueFront"
        """
        if self.isEmpty():
            return False
        else:
            queueFront = self.items[self.front]
            self.items[self.front] = None
            self.front += 1
            return True, queueFront

    def getFront(self):
        """
        +getFront(out success: boolean, out queueFront: QueueItemType)
        Gives you the front of the queue
        :return: Returns True or False wheter the queue is empty or not, if true it will also return the front of the queue
        under "queueFront"
        """
        if self.isEmpty():
            return False
        else:
            queueFront = self.items[self.front]
            return True, queueFront

    def getItem(self, index):
        """
        +getItem(in index: integer, out success: boolean, out queueItem: QueueItemType)
        Gives the item that is located on the given index
        :param index: index number in queue
        :return: Boolean query whether the function is empty or not, if not it will return the item that is placed on the given index
        under "queueItem"
        """
        if self.isEmpty():
            return False
        else:
            queueItem = self.items[index]
            return True, queueItem

    def toDot(self, filename):
        open(filename, "w+")
        with open(filename, 'w') as file:
            file.write("digraph G {\n")
            file.write("front [style=invis]\n")
            file.write("back [style=invis]\n")
            for i in range(0,self.size):
                if not self.items[i] == None:
                    file.write("node" + str(self.items[i].getKey()) + ' [label="' + str(self.items[i].getKey()) + '",shape=record]\n')
            file.write("front -> ")
            for i in range(0,self.size):
                if not self.items[i] == None:
                    file.write("node" + str(self.items[i].getKey()) + "-> ")
            file.write("back\n")
            file.write("rankdir=LR")
            file.write("}")
