class NodeDLC:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def insert(self, value, index, idx, tree=None):
        if idx != index:
            idx += 1
            self.next.insert(value, index, idx)
        else:
            newNode = NodeDLC(value, self, self.prev)
            self.prev.next = newNode
            self.prev = newNode
            if index == 0:
                tree.head = newNode

    def find2(self, index, idx):
        if idx != index:
            idx += 1
            return self.next.find2(index, idx)
        else:
            return self

    def print(self):
        if self.next is None and self.prev is None:
            print(self.value.getKey())
        else:
            head = self
            nextKnop = self
            while nextKnop.next != head:
                print(nextKnop.value.getKey(), "->", nextKnop.next.value.getKey())
                print(nextKnop.next.value.getKey(), "->", nextKnop.value.getKey())
                nextKnop = nextKnop.next
            print(nextKnop.value.getKey(), "->", head.value.getKey())
            print(head.value.getKey(), "->", nextKnop.value.getKey())

    def createDot(self, f):
        if self.next is None and self.prev is None:
            f.write(str(self.value.getKey()) + "\n")
        else:
            f.write('"red=prev" [shape=record][color=red]\n')
            f.write('"blue=next" [shape=record][color=blue]\n')
            head = self
            nextKnop = self
            while nextKnop.next != head:
                f.write(str(nextKnop.value.getKey()) + " -> " + str(nextKnop.next.value.getKey()) + "[color=blue]\n")
                f.write(str(nextKnop.next.value.getKey()) + " -> " + str(nextKnop.value.getKey()) + "[color=red]\n")
                nextKnop = nextKnop.next
            f.write(str(nextKnop.value.getKey()) + " -> " + str(head.value.getKey()) + "[color=blue]\n")
            f.write(str(head.value.getKey()) + " -> " + str(nextKnop.value.getKey()) + "[color=red]\n")

    def find(self, searchkey):
        head = self
        nextKnop = self.next
        while nextKnop != head:
            if nextKnop.value.getKey() == searchkey:
                return True
            nextKnop = nextKnop.next
        return False

    def soort(self, head, size):
        for i in range(size - 1):
            if head.value.getKey() > head.next.value.getKey():
                vorigevalue = head.value
                head.value = head.next.value
                head.next.value = vorigevalue
            head = head.next

    def findindex(self, key):
        index = 1
        head = self.value
        next = self.next
        while True:
            if next.value.getKey() == key:
                return index
            elif next.value.getKey() == head.searchkey:
                return None
            else:
                next = next.next
                index += 1

    def traverse(self, L, head):
        L.append(self.value)
        if self.next is None or self.next == head:
            return L
        else:
            return self.next.traverse(L, head)

    def retrieve(self, head, key):
        if self.value.getKey() == key:
            return self.value
        elif self.next == head or self.next is None:
            return None
        else:
            return self.next.retrieve(head, key)

class DLC:
    def __init__(self):
        self.head = None
        self.size = 0
        self.dotindex = 1

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def findindex(self, key):
        if self.head.value.getKey() == key:
            return 0
        else:
            return self.head.findindex(key)

    def insert(self, value, index=None):
        if isinstance(value, int):
            value = Test(value)
        # if self.find(value.getKey()):
        #     return False
        if index is None:
            index = self.size
        if index > self.size or index < 0:
            return False
        elif self.head is None:
            self.head = NodeDLC(value)
            self.size += 1
            return True
        elif self.size == 1:
            newNode = NodeDLC(value, self.head, self.head)
            self.head.prev = newNode
            self.head.next = newNode
            if index == 0:
                self.head = newNode
            self.size += 1
            return True
        else:
            self.head.insert(value, index, 0, self)
            self.size += 1
            return True

    def find(self, searchkey):
        if self.head is None:
            return False
        elif self.head.value.getKey() == searchkey:
            return True
        elif self.size == 1:
            return False
        else:
            return self.head.find(searchkey)

    def delete(self, index=None):
        if index is None:
            index = 0
        if index > self.size-1 or index < 0:
            return False
        if index == 0 and self.size == 1:
            self.head = None
            self.size = 0
            return True
        elif self.size == 2:
            if index == 0:
                self.head = NodeDLC(self.head.next.value)
            elif index == 1:
                self.head = NodeDLC(self.head.value)
            self.size = 1
            return True
        else:
            delNode = self.head.find2(index, 0)
            delNode.prev.next = delNode.next
            delNode.next.prev = delNode.prev
            if index == 0:
                self.head = delNode.next
            self.size -= 1
            return True

    def retrieve(self, key):
        if self.head is None:
            return None
        else:
            return self.head.retrieve(self.head, key)

    def print(self):
        print("digraph K {")
        if self.head is not None:
            print("head [shape=square]")
            print("head ->", self.head.value.getKey())
            self.head.print()
        print("rankdir=LR")
        print("}")

    def createDot(self):
        f = open("dlc-" + str(self.dotindex) + ".dot", "w")
        f.write("digraph K {\n")
        if self.head is not None:
            f.write("head [shape=square]\n")
            f.write("head -> " + str(self.head.value.getKey()) + "\n")
            self.head.createDot(f)
        f.write("rankdir=LR\n")
        f.write("}\n")
        self.dotindex += 1

    def sort(self):
        if self.size > 1:
            for i in range(self.size):
                self.head.soort(self.head, self.size)
        return True

    def traverse(self):
        L = []
        if self.head is not None:
            return self.head.traverse(L, self.head)

class Test:
    def __init__(self, key):
        self.key = key
    def getKey(self):
        return self.key