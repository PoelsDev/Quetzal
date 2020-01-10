from ADTs.Tjenne.double_linked_chain import DLC

import os

class Node:
    def __init__(self, content, key):
        self.key = key
        self.content = content


class Hashmap:
    """
    retrieve ook nog niet gemaakt
    """

    def __init__(self, mapsize, type):
        """
        maakt een lege hashmap aan
        :param mapsize: de grootte van de map
        :param type: het type hashmap "lin, quad of sep"
        pre: type is in ["lin",quad,"sep"], mapsize > 0
        """
        self.size = mapsize
        self.type = type
        self.itemCount = 0
        self.map = []
        for i in range(mapsize):
            self.map.append(None)

    def isEmpty(self):
        """
        kijkt of de hashmap leeg is of niet
        :return: true als leeg, anders false
        pre: hashmap moet bestaan
        post: None
        """
        if self.itemCount == 0:
            return True
        return False

    def hashkey(self, key):
        """
        bepaalt de positie van een key in de hashmap
        :param key: de te convergeren key
        :return: de berekende hashkey
        pre: de hashmap moet bestaan, key is een integer
        post: returnwaarde is een integer
        """
        return int(key) % self.size

    def insert(self, content, key):
        """
        insert een item met key in de hashmap
        :param content: het toe te voegen item
        :param key: de searchkey van het item
        :return: True als correct toegevoegd, anders false
        pre: hashmap moet bestaan, key is een integer
        post: itemcount is met één vergroot, node met key en item toegevoegd aan map
        """
        hashkey = self.hashkey(key)
        originalItemCount = self.itemCount
        if self.type == "lin":
            self.__lininsert(content, key, hashkey)
            if self.itemCount > originalItemCount:
                return True
            return False

        if self.type == "quad":

            self.__quadinsert(content, key, hashkey)
            if self.itemCount > originalItemCount:
                return True
            return False

        if self.type == "sep":
            self.__sepinsert(content, key, hashkey)
            if self.itemCount > originalItemCount:
                return True
            return False

        return False

    def __lininsert(self, content, key, hashkey):
        """
        voegt item met key toe aan map volgens lin probing
        :param content: toe te voegen item
        :param key: de key bij het item
        :param hashkey: de (begin-)locatie van de nieuwe node in de map
        :return: None
        pre: hashmap moet bestaan, key is integer, hashkey is integer
        post: itemcount is met één verhoogt, node met item een key is toegevoegd aan map
        """

        if self.map[hashkey] is None:
            self.map[hashkey] = Node(content, key)
            self.itemCount += 1
            return
        nextposcount = 1
        current = self.map[hashkey + 1]
        while current is not None:
            nextposcount += 1
            if nextposcount >= self.size:
                nextposcount -= self.size
            current = self.map[hashkey + nextposcount]

        self.map[hashkey + nextposcount] = Node(content, key)
        self.itemCount += 1
        return

    def __quadinsert(self, content, key, hashkey):
        """
        voegt item met key toe aan map volgens quad probing
        :param content: toe te voegen item
        :param key: de key bij het item
        :param hashkey: de (begin-)locatie van de nieuwe node in de map
        :return: None
        pre: hashmap moet bestaan, key is integer, hashkey is integer
        post: itemcount is met één verhoogt, node met item een key is toegevoegd aan map
        """

        if self.map[hashkey] is None:
            self.map[hashkey] = Node(content, key)
            self.itemCount += 1
            return

        nextposcount = 1

        current = self.map[hashkey + pow(nextposcount, 2)]

        while current is not None:
            nextposcount += 1
            if hashkey + nextposcount >= self.size:
                nextposcount -= self.size
            current = self.map[hashkey + pow(nextposcount, 2)]

        self.map[hashkey + pow(nextposcount, 2)] = Node(content, key)
        self.itemCount += 1
        return

    def __sepinsert(self, content, key, hashkey):
        """
        voegt item met key toe aan map volgens sep probing
        :param content: toe te voegen item
        :param key: de key bij het item
        :param hashkey: de (begin-)locatie van de nieuwe node in de map
        :return: None
        pre: hashmap moet bestaan, key is integer, hashkey is integer
        post: itemcount is met één verhoogt, node met item een key is toegevoegd aan de chain in de map
        """
        if self.map[hashkey] is None:
            self.map[hashkey] = DLC()

        originalsize = self.map[hashkey].size
        self.map[hashkey].add(content, key)
        if self.map[hashkey].size > originalsize:
            self.itemCount += 1
        return


    def delete(self, key):
        """
        bepaald welke deletefunctie er moet worden uitgevoerd
        :param key: de key van het te deleten item
        :return: True als correct gedeleted, anders false
        pre: hashmap moet bestaan, key is een integer
        post: itemcount is met één gedaald, item dat bij key hoort is verwijdert

        """
        hashkey = self.hashkey(key)
        originalItemCount = self.itemCount

        if self.type == "lin":
            self.__lindelete(key, hashkey)
            if self.itemCount < originalItemCount:
                return True
            print("Item with key '" + str(key) + "' not found")
            return False
        if self.type == "quad":
            self.__quaddelete(key, hashkey)
            if self.itemCount < originalItemCount:
                return True
            print("Item with key '" + str(key) + "' not found")
            return False
        if self.type == "sep":
            self.__sepdelete(key, hashkey)
            if self.itemCount < originalItemCount:
                return True
            print("Item with key '" + str(key) + "' not found")
            return False

    def __lindelete(self, key, hashkey):
        """
        delete een item uit de hashmap via linair probing
        :param key: de originele key van het item
        :param hashkey: de searchkey van het item in de hashmap
        :return: True als item is verwijdert, false als item niet gevonden is
        pre: hashkey is een integer, key is een integer, hashmap moet bestaan
        post: itemcount is met één gedaald, item dat bij key hoort is verwijdert
        """
        node = self.map[hashkey]
        if node is not None:
            if node.key == key:
                self.map[hashkey] = None
                self.itemCount -= 1
                return True

        nextposcount = 0
        restart = False

        while True:
            nextposcount += 1
            if nextposcount + hashkey >= self.size:
                nextposcount -= self.size
                restart = True
            if nextposcount + hashkey >= hashkey and restart is True:
                return False
            current = self.map[hashkey + nextposcount]
            if current is not None:
                if current.key == key:
                    self.map[hashkey + nextposcount] = None
                    self.itemCount -= 1
                    return True

    def __quaddelete(self, key, hashkey):
        """
        delete een item uit de hashmap via quad probing
        :param key: de originele key van het item
        :param hashkey: de searchkey van het item in de hashmap
        :return: None
        pre: hashkey is een integer, key is een integer, hashmap moet bestaan
        post: itemcount is met één gedaald, item dat bij key hoort is verwijdert
        """
        node = self.map[hashkey]
        if node is not None:
            if node.key == key:
                self.map[hashkey] = None
                self.itemCount -= 1
                return

        nextposcount = 0
        restart = False
        while True:
            nextposcount += 1
            powerednextPos = pow(nextposcount, 2)
            if powerednextPos + hashkey >= self.size:
                powerednextPos -= self.size
                restart = True
            if powerednextPos + hashkey >= hashkey and restart is True:
                return False
            current = self.map[hashkey + powerednextPos]
            if current is not None:
                if current.key == key:
                    self.map[hashkey + powerednextPos] = None
                    self.itemCount -= 1
                    return

    def __sepdelete(self, key, hashkey):
        """
        delete een item uit de hashmap via seperate chaining
        :param key: de originele key van het item
        :param hashkey: de searchkey van het item in de hashmap
        :return: None
        pre: hashkey is een integer, key is een integer, hashmap moet bestaan
        post: itemcount is met één gedaald, item dat bij key hoort is verwijdert
        """
        if self.map[hashkey] is not None:
            originalsize = self.map[hashkey].size
            self.map[hashkey].pop(key)
            if self.map[hashkey].size < originalsize:
                self.itemCount -= 1
            if self.map[hashkey].isEmpty():
                self.map[hashkey] = None


    def print(self):
        """
        zet hashmap om naar dot en png
        :return: None
        """
        dot = "digraph G {\nrankdir = UD\n"

        noneCount = 0
        for i in range(len(self.map)):
            if self.map[i] is not None:
                if self.type == "sep":
                    dot += self.map[i].print(True)
                else:
                    dot += str(self.map[i].content) + "\n"
            else:
                dot += "None" + str(noneCount) + "\n"
                noneCount += 1

        dot += "}"

        file = open("outputfiles/Hashmap.dot", "w")
        file.write(dot)
        file.close()

        os.system("dot outputfiles/Hashmap.dot -Tpng -o outputfiles/Hashmap.png")



    def traverse(self):
        """
        traversed de map en returned een lijst met alle items
        :return:
        """

        allContent = []
        if self.type != "h_sep":
            for i in range(len(self.map)):
                if self.map[i] is not None:
                    allContent.append(self.map[i].conent)




# h = Hashmap(11, "lin")
# h.insert(2, 11)
# h.insert(13, 22)
# h.insert(35, 33)
# h.print()
#
# h.print()
# print("fin")
