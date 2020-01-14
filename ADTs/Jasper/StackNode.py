class StackNode:
    def __init__(self, searchKey, next=None):
        """
        The object is a node that will be used in a stack
        :param searchKey: The value of the node
        """
        self.searchKey = searchKey
        self.next = next

    def toDotFile(self,file):
        if self != None:
            file.write("node" + str(self.searchKey.getKey()) + ' [label="' + str(self.searchKey.getKey()) + '",shape=record]\n')
        if self.next != None:
            self.next.toDotFile(file)
