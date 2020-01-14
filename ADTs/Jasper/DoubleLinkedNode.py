class DoubleLinkedNode:
    def __init__(self, searchKey, next=None, previous=None):
        """
        The object is a node which will be used for a double linked chain (can be circular)
        :param searchKey: the search key of the node
        :param next: the reference to the next node in the chain
        :param previous: the reference to the previous node in the chain
        """
        self.searchKey = searchKey
        self.next = next
        self.previous = previous

    def toDotFile(self, file, head):
        if not self.searchKey.getKey() == head:
            file.write("node" + str(self.searchKey.getKey()) + ' [label="' + str(self.searchKey.getKey()) + '"]\n')
            file.write("node" + str(self.previous.searchKey.getKey()) + " -> node" + str(self.searchKey.getKey()) + "\n")
            file.write("node" + str(self.searchKey.getKey()) + " -> node" + str(self.previous.searchKey.getKey()) + "\n")
            self.next.toDotFile(file, head)
