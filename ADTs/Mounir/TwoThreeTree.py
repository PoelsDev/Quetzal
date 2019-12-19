from copy import deepcopy

"""
    +isEmpty(): boolean
    Deze functie checkt of de 2-3 boom leeg is of niet.
    :return: True als de boom leeg is, anders False.
    Pre-condities: geen.
    Post-condities: Geeft een boolean terug die weergeeft of de 2-3 boom leeg is of niet.
    
    +insertItem(in NewItem: TreeItemType): boolean
    Deze functie insert een newItem in de 2-3 boom.
    :param newItem: NewItem dat moet worden toegevoegd.
    :return: True of False (success Boolean)
    Pre-condities: De parameter newItem moet een object van een class zijn met een variabel searchkey.
    Post-condities: Het object zal aan de 2-3 boom worden toegevoegd. (Tenzij dezelfde key als een ander object)

    +retrieveItem(in searchKey: KeyType, out treeItem: TreeItemType)
    Deze functie zoekt een bepaalde key in de 2-3 boom op basis van een gegeven searchKey en geeft het daarbij horende object terug.
    :param searchKey: Te zoeken key
    :return: None als er geen gevonden is, een object (treeItem) als er wel 1 gevonden is.
    Pre-condities: De parameter searchKey moet gelijk zijn aan de value van de variabel searchkey van de object die we willen zoeken.
    Post-condities: Er zal een object zijn teruggegeven met de overeenkomstige sleutel.
    
    +deleteItem(in searchKey: KeyType): boolean
    Deze functie delete met een gegeven key, een object uit de boom.
    :param searchKey: De key waarvoor een te verwijderen object moet gevonden worden.
    :return: False als het mislukt is, True als het gelukt is.
    Pre-condities: De parameter searchKey moet gelijk zijn aan de value van de variabel searchkey van de object die we willen verwijderen.
    Post-condities: Het object met de overeenkomstige sleutel zal verwijdert zijn.
    
    +printTree()
    Geeft .dot code voor de structuur van de 2-3 boom.
    
    +createDot()
    Creert een nieuwe .dot file met de structuur van de 2-3 boom
    
    +inorderDot()
    Creert een nieuwe .dot file met de inorder traversal de de 2-3 boom 
    
    +inorder()
    Doorloopt de boom in inorder traverse en print de __str__ method van de objecten af (TreeItemType).
    Pre-condities: geen.
    Post-condities: De boom zal (als niet leeg) in inorder traverse doorlopen worden.

"""


class Node:
    def __init__(self):
        self.root = []
        self.parent = None
        self.left = None
        self.left2 = None
        self.mid = None
        self.right2 = None
        self.right = None

    def find(self, key):
        if len(self.root) == 1:
            if self.root[0].searchkey == key:
                return self.root[0]
            if self.left is not None and self.right is not None:
                if self.root[0].searchkey > key:
                    return self.left.find(key)
                else:
                    return self.right.find(key)
            return None
        else:
            if self.root[0].searchkey == key:
                return self.root[0]
            elif self.root[1].searchkey == key:
                return self.root[1]
            if self.left is not None and self.right is not None and self.mid is not None:
                if self.root[0].searchkey > key:
                    return self.left.find(key)
                elif self.root[1].searchkey > key:
                    return self.mid.find(key)
                else:
                    return self.right.find(key)
            return None

    def insert(self, value, apartgeval=None):
        # Geval Blad of climb up
        if (self.left is None and self.right is None) or (apartgeval is True):
            # -- Lege node
            if len(self.root) == 0:
                self.root = [value]
            # -- Bijna vol
            if len(self.root) == 1:
                if self.root[0].searchkey < value.searchkey:
                    self.root = self.root + [value]
                else:
                    self.root = [value] + self.root
            # --  Vol
            else:  # (len = 2)
                if self.root[1].searchkey < value.searchkey:
                    self.root = self.root + [value]
                elif self.root[0].searchkey < value.searchkey:
                    self.root = [self.root[0]] + [value] + [self.root[1]]
                else:
                    self.root = [value] + self.root
            # We voegen toe en dan pas split
                if self.parent is None:
                    temp = deepcopy(self)
                    self.left = Node()
                    self.right = Node()
                    self.left.parent = self
                    self.right.parent = self
                    self.left.root = [self.root[0]]
                    self.right.root = [self.root[2]]

                    self.left.left = temp.left
                    self.left.right = temp.left2
                    self.right.left = temp.right2
                    self.right.right = temp.right
                    if temp.left is not None:
                        self.left.left.parent = self.left
                        self.left.right.parent = self.left
                        self.right.left.parent = self.right
                        self.right.right.parent = self.right
                    self.root = [self.root[1]]
                    self.left2 = None
                    self.right2 = None

                else:
                    if len(self.parent.root) == 1:
                        midden = self.root[1]

                        if self.parent.left == self:
                            self.parent.left = Node()
                            self.parent.left.parent = self.parent
                            self.parent.left.root = [self.root[0]]
                            self.parent.left.left = self.left
                            self.parent.left.right = self.left2
                            if self.parent.left.left is not None and self.parent.left.right is not None:
                                self.parent.left.left.parent = self.parent.left
                                self.parent.left.right.parent = self.parent.left

                            self.parent.mid = Node()
                            self.parent.mid.parent = self.parent
                            self.parent.mid.root = [self.root[2]]
                            self.parent.mid.left = self.right2
                            self.parent.mid.right = self.right
                            if self.parent.mid.left is not None and self.parent.mid.right is not None:
                                self.parent.mid.left.parent = self.parent.mid
                                self.parent.mid.right.parent = self.parent.mid

                            self.parent.insert(midden, True)
                            del self

                        elif self.parent.right == self:
                            self.parent.right = Node()
                            self.parent.right.parent = self.parent
                            self.parent.right.root = [self.root[2]]
                            self.parent.right.left = self.right2
                            self.parent.right.right = self.right
                            if self.parent.right.left is not None and self.parent.right.right is not None:
                                self.parent.right.left.parent = self.parent.right
                                self.parent.right.right.parent = self.parent.right

                            self.parent.mid = Node()
                            self.parent.mid.parent = self.parent
                            self.parent.mid.root = [self.root[0]]
                            self.parent.mid.left = self.left
                            self.parent.mid.right = self.left2
                            if self.parent.mid.left is not None and self.parent.mid.right is not None:
                                self.parent.mid.left.parent = self.parent.mid
                                self.parent.mid.right.parent = self.parent.mid


                            self.parent.insert(midden, True)
                            del self

                    else: # if len = 2
                        midden = self.root[1]
                        if self.parent.left == self:
                            self.parent.left = Node()
                            self.parent.left2 = Node()
                            self.parent.right2 = Node()

                            self.parent.left.parent = self.parent
                            self.parent.left.root = [self.root[0]]
                            self.parent.left.left = self.left
                            self.parent.left.right = self.left2
                            if self.parent.left.left is not None and self.parent.left.right is not None:
                                self.parent.left.left.parent = self.parent.left
                                self.parent.left.right.parent = self.parent.left

                            self.parent.left2.parent = self.parent
                            self.parent.left2.root = [self.root[2]]
                            self.parent.left2.left = self.right2
                            self.parent.left2.right = self.right
                            if self.parent.left2.left is not None and self.parent.left2.right is not None:
                                self.parent.left2.left.parent = self.parent.left2
                                self.parent.left2.right.parent = self.parent.left2

                            self.parent.right2.parent = self.parent
                            self.parent.right2.root = self.parent.mid.root
                            self.parent.right2.left = self.parent.mid.left
                            self.parent.right2.right = self.parent.mid.right
                            self.parent.right2.mid = self.parent.mid.mid
                            if self.parent.right2.left is not None and self.parent.right2.right is not None:
                                self.parent.right2.left.parent = self.parent.right2
                                self.parent.right2.right.parent = self.parent.right2
                            if self.parent.right2.mid is not None:
                                self.parent.right2.mid.parent = self.parent.right2

                            self.parent.mid = None

                            self.parent.insert(midden, True)

                        elif self.parent.mid == self:
                            self.parent.left2 = Node()
                            self.parent.right2 = Node()

                            self.parent.left2.parent = self.parent
                            self.parent.left2.root = [self.root[0]]
                            self.parent.left2.left = self.left
                            self.parent.left2.right = self.left2
                            if self.parent.left2.left is not None and self.parent.left2.right is not None:
                                self.parent.left2.left.parent = self.parent.left2
                                self.parent.left2.right.parent = self.parent.left2

                            self.parent.right2.parent = self.parent
                            self.parent.right2.root = [self.root[2]]
                            self.parent.right2.left = self.right2
                            self.parent.right2.right = self.right
                            if self.parent.right2.left is not None and self.parent.right2.right is not None:
                                self.parent.right2.left.parent = self.parent.right2
                                self.parent.right2.right.parent = self.parent.right2

                            self.parent.mid = None

                            self.parent.insert(midden, True)

                        elif self.parent.right == self:
                            self.parent.right = Node()
                            self.parent.left2 = Node()
                            self.parent.right2 = Node()

                            self.parent.right.parent = self.parent
                            self.parent.right.root = [self.root[2]]
                            self.parent.right.right = self.right
                            self.parent.right.left = self.right2
                            if self.parent.right.right is not None and self.parent.right.left is not None:
                                self.parent.right.right.parent = self.parent.right
                                self.parent.right.left.parent = self.parent.right

                            self.parent.right2.parent = self.parent
                            self.parent.right2.root = [self.root[0]]
                            self.parent.right2.right = self.left2
                            self.parent.right2.left = self.left
                            if self.parent.right2.right is not None and self.parent.right2.left is not None:
                                self.parent.right2.right.parent = self.parent.right2
                                self.parent.right2.left.parent = self.parent.right2

                            self.parent.left2.parent = self.parent
                            self.parent.left2.root = self.parent.mid.root
                            self.parent.left2.left = self.parent.mid.left
                            self.parent.left2.right = self.parent.mid.right
                            self.parent.left2.mid = self.parent.mid.mid
                            if self.parent.left2.left is not None and self.parent.left2.right is not None:
                                self.parent.left2.left.parent = self.parent.left2
                                self.parent.left2.right.parent = self.parent.left2
                            if self.parent.left2.mid is not None:
                                self.parent.left2.mid.parent = self.parent.left2

                            self.parent.mid = None

                            self.parent.insert(midden, True)
                            del self
        #RECURSIE TOT BLAD
        else:
            if len(self.root) == 1:
                if value.searchkey < self.root[0].searchkey:
                    self.left.insert(value)
                else:
                    self.right.insert(value)
            else:
                if len(self.root) == 2:
                    if value.searchkey < self.root[0].searchkey:
                        self.left.insert(value)
                    elif value.searchkey < self.root[1].searchkey:
                        self.mid.insert(value)
                    else:
                        self.right.insert(value)

    def delete(self, key, t):
        if len(self.root) == 1:                                                 # Element zit in een 2-node
            if self.root[0].searchkey == key:
                if self.left is None and self.right is None:
                    if len(self.parent.root) == 2:
                        if self.parent.left == self:
                            if len(self.parent.mid.root) == 1:
                                self.root = [self.parent.root[0], self.parent.mid.root[0]]
                                self.parent.mid = None
                                self.parent.root = [self.parent.root[1]]
                            elif len(self.parent.mid.root) == 2:
                                self.root = [self.parent.root[0]]
                                self.parent.root = [self.parent.mid.root[0], self.parent.root[1]]
                                self.parent.mid.root = [self.parent.mid.root[1]]

                        elif self.parent.mid == self:
                            if len(self.parent.left.root) == 1:
                                self.parent.left.root = [self.parent.left.root[0], self.parent.root[0]]
                                self.parent.root = [self.parent.root[1]]
                                self.parent.mid = None
                            elif len(self.parent.left.root) == 2:
                                self.root = [self.parent.root[0]]
                                self.parent.root = [self.parent.left.root[1], self.parent.root[1]]
                                self.parent.left.root = [self.parent.left.root[0]]

                        elif self.parent.right == self:
                            if len(self.parent.mid.root) == 1:
                                self.root = [self.parent.mid.root[0], self.parent.root[1]]
                                self.parent.root = [self.parent.root[0]]
                                self.parent.mid = None
                            elif len(self.parent.mid.root) == 2:
                                self.root = [self.parent.root[1]]
                                self.parent.root = [self.parent.root[0], self.parent.mid.root[1]]
                                self.parent.mid.root = [self.parent.mid.root[0]]

                    elif len(self.parent.root) == 1:
                        if self.parent.left == self:
                            if len(self.parent.right.root) == 2:
                                self.root = [self.parent.root[0]]
                                self.parent.root = [self.parent.right.root[0]]
                                self.parent.right.root = [self.parent.right.root[1]]
                            elif len(self.parent.right.root) == 1:
                                if self.parent.parent is None:
                                    self.parent.root = [self.parent.root[0], self.parent.right.root[0]]
                                    self.parent.left = None
                                    self.parent.right = None
                                    #
                                else:
                                    if self.parent.parent.parent is None:
                                        if len(self.parent.parent.root) == 1:
                                            if self.parent.parent.right == self.parent:
                                                if len(self.parent.parent.left.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.left.root[0], self.parent.parent.root[0]]
                                                    new.left = self.parent.parent.left.left
                                                    new.mid = self.parent.parent.left.right
                                                    new.right = self.parent.right
                                                    new.right.root = [self.parent.root[0], new.right.root[0]]
                                                    new.left.parent = new
                                                    new.right.parent = new
                                                    new.mid.parent = new
                                                    t.root = new

                                                elif len(self.parent.parent.left.root) == 2:
                                                    new = Node()
                                                    new.root = [self.parent.parent.left.root[1]]
                                                    # //
                                                    new.left = Node()
                                                    new.left.parent = new
                                                    new.left.root = [self.parent.parent.left.root[0]]
                                                    #
                                                    new.left.left = Node()
                                                    new.left.left.root = self.parent.parent.left.left.root
                                                    new.left.left.parent = new.left
                                                    #
                                                    new.left.right = Node()
                                                    new.left.right.root = self.parent.parent.left.mid.root
                                                    new.left.right.parent = new.left
                                                    # //
                                                    new.right = Node()
                                                    new.right.parent = new
                                                    new.right.root = [self.parent.parent.root[0]]
                                                    #
                                                    new.right.left = Node()
                                                    new.right.left.root = self.parent.parent.left.right.root
                                                    new.right.left.parent = new.right
                                                    #
                                                    new.right.right = Node()
                                                    new.right.right.root = [self.parent.root[0], self.parent.right.root[0]]
                                                    new.right.right.parent = new.right
                                                    t.root = new

                                            elif self.parent.parent.left == self.parent:
                                                if len(self.parent.parent.right.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.root[0], self.parent.parent.right.root[0]]
                                                    new.right = self.parent.parent.right.right
                                                    new.mid = self.parent.parent.right.left
                                                    new.left = self.parent.right
                                                    new.left.root = [self.parent.root[0], new.left.root[0]]
                                                    new.left.parent = new
                                                    new.right.parent = new
                                                    new.mid.parent = new
                                                    t.root = new

                                                elif len(self.parent.parent.right.root) == 2:
                                                    new = Node()
                                                    new.root = [self.parent.parent.right.root[0]]
                                                    # //
                                                    new.right = Node()
                                                    new.right.parent = new
                                                    new.right.root = [self.parent.parent.right.root[1]]
                                                    #
                                                    new.right.right = Node()
                                                    new.right.right.root = self.parent.parent.right.right.root
                                                    new.right.right.parent = new.right
                                                    #
                                                    new.right.left = Node()
                                                    new.right.left.root = self.parent.parent.right.mid.root
                                                    new.right.left.parent = new.right
                                                    # //
                                                    new.left = Node()
                                                    new.left.parent = new.left
                                                    new.left.root =  [self.parent.parent.root[0]]
                                                    #
                                                    new.left.right = Node()
                                                    new.left.right.root = self.parent.parent.right.left.root
                                                    new.left.right.parent = new.left
                                                    #
                                                    new.left.left = Node()
                                                    new.left.left.root = [self.parent.root[0], self.parent.right.root[0]]
                                                    new.left.left.parent = new.left
                                                    t.root = new

                                        elif len(self.parent.parent.root) == 2:
                                            if self.parent.parent.left == self.parent:
                                                if len(self.parent.parent.mid.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.root[0], self.parent.parent.mid.root[0]]
                                                    new.left = Node()
                                                    new.left.root = [self.parent.root[0], self.parent.right.root[0]]
                                                    new.left.parent = new
                                                    #
                                                    new.mid = Node()
                                                    new.mid.root = self.parent.parent.mid.left.root
                                                    new.mid.parent = new
                                                    #
                                                    new.right = Node()
                                                    new.right.root = self.parent.parent.mid.right.root
                                                    new.right.parent = new
                                                    t.root.root = [t.root.root[1]]
                                                    t.root.mid = None
                                                    t.root.left = new
                                                    t.root.left.parent = t.root
                                                elif len(self.parent.parent.mid.root) == 2:
                                                    newleft = Node()
                                                    newleft.root = [self.parent.parent.root[0]]
                                                    newleft.left = Node()
                                                    newleft.left.root = [self.parent.root[0], self.parent.right.root[0]]
                                                    newleft.left.parent = newleft
                                                    newleft.right = Node()
                                                    newleft.right.root = self.parent.parent.mid.left.root
                                                    newleft.right.parent = newleft

                                                    newmid = Node()
                                                    newmid.root = [self.parent.parent.mid.root[1]]
                                                    newmid.left = Node()
                                                    newmid.left.root = self.parent.parent.mid.mid.root
                                                    newmid.left.parent = newmid
                                                    newmid.right = Node()
                                                    newmid.right.root = self.parent.parent.mid.right.root
                                                    newmid.right.parent = newmid

                                                    t.root.root = [t.root.mid.root[0], t.root.root[1]]
                                                    t.root.left = newleft
                                                    t.root.mid = newmid
                                                    t.root.left.parent = t.root
                                                    t.root.mid.parent = t.root

                                            elif self.parent.parent.mid == self.parent:
                                                if len(self.parent.parent.left.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.left.root[0], self.parent.parent.root[0]]
                                                    new.right = Node()
                                                    new.right.root = [self.parent.root[0], self.parent.right.root[0]]
                                                    new.right.parent = new
                                                    new.mid = Node()
                                                    new.mid.root = self.parent.parent.left.right.root
                                                    new.mid.parent = new
                                                    new.left = Node()
                                                    new.left.root = self.parent.parent.left.left.root
                                                    new.left.parent = new
                                                    t.root.root = [t.root.root[1]]
                                                    t.root.mid = None
                                                    t.root.left = new
                                                    t.root.left.parent = t.root
                                                elif len(self.parent.parent.left.root) == 2:
                                                    newmid = Node()
                                                    newmid.root = [self.parent.parent.root[0]]
                                                    newmid.right = Node()
                                                    newmid.right.root = [self.parent.root[0], self.parent.right.root[0]]
                                                    newmid.right.parent = newmid
                                                    newmid.left = Node()
                                                    newmid.left.root = self.parent.parent.left.right.root
                                                    newmid.left.parent = newmid

                                                    newleft = Node()
                                                    newleft.root = [self.parent.parent.left.root[0]]
                                                    newleft.left = Node()
                                                    newleft.left.root = self.parent.parent.left.left.root
                                                    newleft.left.parent = newleft
                                                    newleft.right = Node()
                                                    newleft.right.root = self.parent.parent.left.mid.root
                                                    newleft.right.parent = newleft

                                                    t.root.root = [t.root.left.root[1], t.root.root[1]]
                                                    t.root.left = newleft
                                                    t.root.mid = newmid
                                                    t.root.left.parent = t.root
                                                    t.root.mid.parent = t.root

                                            elif self.parent.parent.right == self.parent:
                                                if len(self.parent.parent.mid.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.mid.root[0], self.parent.parent.root[1]]
                                                    new.right = Node()
                                                    new.right.root = [self.parent.root[0], self.parent.right.root[0]]
                                                    new.right.parent = new
                                                    #
                                                    new.mid = Node()
                                                    new.mid.root = self.parent.parent.mid.right.root
                                                    new.mid.parent = new
                                                    #
                                                    new.left = Node()
                                                    new.left.root = self.parent.parent.mid.left.root
                                                    new.left.parent = new
                                                    #
                                                    t.root.root = [t.root.root[0]]
                                                    t.root.mid = None
                                                    t.root.right = new
                                                    t.root.right.parent = t.root
                                                elif len(self.parent.parent.mid.root) == 2:
                                                    newright = Node()
                                                    newright.root = [self.parent.parent.root[1]]
                                                    newright.right = Node()
                                                    newright.right.root = [self.parent.root[0], self.parent.right.root[0]]
                                                    newright.right.parent = newright
                                                    newright.left = Node()
                                                    newright.left.root = self.parent.parent.mid.right.root
                                                    newright.left.parent = newright

                                                    newmid = Node()
                                                    newmid.root = [self.parent.parent.mid.root[0]]
                                                    newmid.left = Node()
                                                    newmid.left.root = self.parent.parent.mid.left.root
                                                    newmid.left.parent = newmid
                                                    newmid.right = Node()
                                                    newmid.right.root = self.parent.parent.mid.mid.root
                                                    newmid.right.parent = newmid
                                                    t.root.root = [t.root.root[0], t.root.mid.root[1]]
                                                    t.root.mid = newmid
                                                    t.root.right = newright
                                                    t.root.mid.parent = t.root
                                                    t.root.right.parent = t.root

                        elif self.parent.right == self:
                            if len(self.parent.left.root) == 2:
                                self.root = [self.parent.root[0]]
                                self.parent.root = [self.parent.left.root[1]]
                                self.parent.left.root = [self.parent.left.root[0]]
                            elif len(self.parent.left.root) == 1:
                                if self.parent.parent is None:
                                    self.parent.root = [self.parent.left.root[0], self.parent.root[0]]
                                    self.parent.left = None
                                    self.parent.right = None
                                else:
                                    if self.parent.parent.parent is None:
                                        if len(self.parent.parent.root) == 1:
                                            if self.parent.parent.right == self.parent:
                                                if len(self.parent.parent.left.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.left.root[0], self.parent.parent.root[0]]
                                                    new.left = self.parent.parent.left.left
                                                    new.mid = self.parent.parent.left.right
                                                    new.right = self.parent.left
                                                    new.right.root = [new.right.root[0], self.parent.root[0]]
                                                    new.left.parent = new
                                                    new.right.parent = new
                                                    new.mid.parent = new
                                                    t.root = new

                                                elif len(self.parent.parent.left.root) == 2:
                                                    new = Node()
                                                    new.root = [self.parent.parent.left.root[1]]
                                                    # //
                                                    new.left = Node()
                                                    new.left.parent = new
                                                    new.left.root = [self.parent.parent.left.root[0]]
                                                    #
                                                    new.left.left = Node()
                                                    new.left.left.root = self.parent.parent.left.left.root
                                                    new.left.left.parent = new.left
                                                    #
                                                    new.left.right = Node()
                                                    new.left.right.root = self.parent.parent.left.mid.root
                                                    new.left.right.parent = new.left
                                                    # //
                                                    new.right = Node()
                                                    new.right.parent = new
                                                    new.right.root = [self.parent.parent.root[0]]
                                                    #
                                                    new.right.left = Node()
                                                    new.right.left.root = self.parent.parent.left.right.root
                                                    new.right.left.parent = new.right
                                                    #
                                                    new.right.right = Node()
                                                    new.right.right.root = [self.parent.left.root[0], self.parent.root[0]]
                                                    new.right.right.parent = new.right
                                                    t.root = new

                                            elif self.parent.parent.left == self.parent:
                                                if len(self.parent.parent.right.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.root[0], self.parent.parent.right.root[0]]
                                                    new.right = self.parent.parent.right.right
                                                    new.mid = self.parent.parent.right.left
                                                    new.left = self.parent.left
                                                    new.left.root = [new.left.root[0], self.parent.root[0]]
                                                    new.left.parent = new
                                                    new.right.parent = new
                                                    new.mid.parent = new
                                                    t.root = new

                                                elif len(self.parent.parent.right.root) == 2:
                                                    new = Node()
                                                    new.root = [self.parent.parent.right.root[0]]
                                                    # //
                                                    new.right = Node()
                                                    new.right.parent = new
                                                    new.right.root = [self.parent.parent.right.root[1]]
                                                    #
                                                    new.right.right = Node()
                                                    new.right.right.root = self.parent.parent.right.right.root
                                                    new.right.right.parent = new.right
                                                    #
                                                    new.right.left = Node()
                                                    new.right.left.root = self.parent.parent.right.mid.root
                                                    new.right.left.parent = new.right
                                                    # //
                                                    new.left = Node()
                                                    new.left.parent = new.left
                                                    new.left.root =  [self.parent.parent.root[0]]
                                                    #
                                                    new.left.right = Node()
                                                    new.left.right.root = self.parent.parent.right.left.root
                                                    new.left.right.parent = new.left
                                                    #
                                                    new.left.left = Node()
                                                    new.left.left.root = [self.parent.left.root[0], self.parent.root[0]]
                                                    new.left.left.parent = new.left
                                                    t.root = new

                                        elif len(self.parent.parent.root) == 2:
                                            if self.parent.parent.left == self.parent:
                                                if len(self.parent.parent.mid.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.root[0], self.parent.parent.mid.root[0]]
                                                    new.left = Node()
                                                    new.left.root = [self.parent.left.root[0], self.parent.root[0]]
                                                    new.left.parent = new
                                                    #
                                                    new.mid = Node()
                                                    new.mid.root = self.parent.parent.mid.left.root
                                                    new.mid.parent = new
                                                    #
                                                    new.right = Node()
                                                    new.right.root = self.parent.parent.mid.right.root
                                                    new.right.parent = new
                                                    t.root.root = [t.root.root[1]]
                                                    t.root.mid = None
                                                    t.root.left = new
                                                    t.root.left.parent = t.root
                                                elif len(self.parent.parent.mid.root) == 2:
                                                    newleft = Node()
                                                    newleft.root = [self.parent.parent.root[0]]
                                                    newleft.left = Node()
                                                    newleft.left.root = [self.parent.left.root[0], self.parent.root[0]]
                                                    newleft.left.parent = newleft
                                                    newleft.right = Node()
                                                    newleft.right.root = self.parent.parent.mid.left.root
                                                    newleft.right.parent = newleft

                                                    newmid = Node()
                                                    newmid.root = [self.parent.parent.mid.root[1]]
                                                    newmid.left = Node()
                                                    newmid.left.root = self.parent.parent.mid.mid.root
                                                    newmid.left.parent = newmid
                                                    newmid.right = Node()
                                                    newmid.right.root = self.parent.parent.mid.right.root
                                                    newmid.right.parent = newmid

                                                    t.root.root = [t.root.mid.root[0], t.root.root[1]]
                                                    t.root.left = newleft
                                                    t.root.mid = newmid
                                                    t.root.left.parent = t.root
                                                    t.root.mid.parent = t.root

                                            elif self.parent.parent.mid == self.parent:
                                                if len(self.parent.parent.left.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.left.root[0], self.parent.parent.root[0]]
                                                    new.right = Node()
                                                    new.right.root = [self.parent.left.root[0], self.parent.root[0]]
                                                    new.right.parent = new
                                                    new.mid = Node()
                                                    new.mid.root = self.parent.parent.left.right.root
                                                    new.mid.parent = new
                                                    new.left = Node()
                                                    new.left.root = self.parent.parent.left.left.root
                                                    new.left.parent = new
                                                    t.root.root = [t.root.root[1]]
                                                    t.root.mid = None
                                                    t.root.left = new
                                                    t.root.left.parent = t.root
                                                elif len(self.parent.parent.left.root) == 2:
                                                    newmid = Node()
                                                    newmid.root = [self.parent.parent.root[0]]
                                                    newmid.right = Node()
                                                    newmid.right.root = [self.parent.left.root[0], self.parent.root[0]]
                                                    newmid.right.parent = newmid
                                                    newmid.left = Node()
                                                    newmid.left.root = self.parent.parent.left.right.root
                                                    newmid.left.parent = newmid

                                                    newleft = Node()
                                                    newleft.root = [self.parent.parent.left.root[0]]
                                                    newleft.left = Node()
                                                    newleft.left.root = self.parent.parent.left.left.root
                                                    newleft.left.parent = newleft
                                                    newleft.right = Node()
                                                    newleft.right.root = self.parent.parent.left.mid.root
                                                    newleft.right.parent = newleft

                                                    t.root.root = [t.root.left.root[1], t.root.root[1]]
                                                    t.root.left = newleft
                                                    t.root.mid = newmid
                                                    t.root.left.parent = t.root
                                                    t.root.mid.parent = t.root

                                            elif self.parent.parent.right == self.parent:
                                                if len(self.parent.parent.mid.root) == 1:
                                                    new = Node()
                                                    new.root = [self.parent.parent.mid.root[0], self.parent.parent.root[1]]
                                                    new.right = Node()
                                                    new.right.root = [self.parent.left.root[0], self.parent.root[0]]
                                                    new.right.parent = new
                                                    #
                                                    new.mid = Node()
                                                    new.mid.root = self.parent.parent.mid.right.root
                                                    new.mid.parent = new
                                                    #
                                                    new.left = Node()
                                                    new.left.root = self.parent.parent.mid.left.root
                                                    new.left.parent = new
                                                    #
                                                    t.root.root = [t.root.root[0]]
                                                    t.root.mid = None
                                                    t.root.right = new
                                                    t.root.right.parent = t.root
                                                elif len(self.parent.parent.mid.root) == 2:
                                                    newright = Node()
                                                    newright.root = [self.parent.parent.root[1]]
                                                    newright.right = Node()
                                                    newright.right.root = [self.parent.left.root[0], self.parent.root[0]]
                                                    newright.right.parent = newright
                                                    newright.left = Node()
                                                    newright.left.root = self.parent.parent.mid.right.root
                                                    newright.left.parent = newright

                                                    newmid = Node()
                                                    newmid.root = [self.parent.parent.mid.root[0]]
                                                    newmid.left = Node()
                                                    newmid.left.root = self.parent.parent.mid.left.root
                                                    newmid.left.parent = newmid
                                                    newmid.right = Node()
                                                    newmid.right.root = self.parent.parent.mid.mid.root
                                                    newmid.right.parent = newmid
                                                    t.root.root = [t.root.root[0], t.root.mid.root[1]]
                                                    t.root.mid = newmid
                                                    t.root.right = newright
                                                    t.root.mid.parent = t.root
                                                    t.root.right.parent = t.root



                # Vervanging met inorder sucessor
                elif self.left is not None and self.right is not None:
                    temp = self.root[0]
                    self.root = [self.right.goleft().root[0]]
                    if len(self.right.goleft().root) == 2:
                        self.right.goleft().root = [temp, self.right.goleft().root[1]]
                    else:
                        self.right.goleft().root = [temp]
                    self.right.goleft().delete(key, t)

            else:      # Recursie tot juiste node
                if self.root[0].searchkey > key:
                    self.left.delete(key, t)
                else:
                    self.right.delete(key, t)

        elif len(self.root) == 2:
            if self.root[0].searchkey == key or self.root[1].searchkey == key:
                if self.root[0].searchkey == key:                                                  # X 1
                    if self.left is None and self.right is None and self.mid is None:
                        self.root = [self.root[1]]
                    # Vervanging met inorder successor
                    else:
                        temp = self.root[0]
                        self.root = [self.mid.goleft().root[0], self.root[1]]
                        if len(self.mid.goleft().root) == 2:
                            self.mid.goleft().root = [temp, self.mid.goleft().root[1]]
                        else:
                            self.mid.goleft().root = [temp]
                        self.mid.goleft().delete(key, t)
                elif self.root[1].searchkey == key:
                    if self.left is None and self.right is None and self.mid is None:
                        self.root = [self.root[0]]
                    # Vervanging met inorder successor
                    else:
                        temp = self.root[1]
                        self.root = [self.root[0], self.right.goleft().root[0]]
                        if len(self.right.goleft().root) == 2:
                            self.right.goleft().root = [temp, self.right.goleft().root[1]]
                        else:
                            self.right.goleft().root = [temp]
                        self.right.goleft().delete(key, t)

            # Recursie tot juiste node
            else:
                if self.root[0].searchkey > key:
                    self.left.delete(key, t)
                elif self.root[1].searchkey > key:
                    self.mid.delete(key, t)
                else:
                    self.right.delete(key, t)

    def print(self):
        if len(self.root) == 1:
            if self.left is not None and self.left2 is None and self.mid is None and self.right2 is None and self.right is not None:
                if len(self.left.root) == 1:
                    print(self.root[0].searchkey, "--", self.left.root[0].searchkey)
                else:
                    print(self.root[0].searchkey, "--", '"' + str(self.left.root[0].searchkey) + " | " + str(self.left.root[1].searchkey) + '"')
                if len(self.right.root) == 1:
                    print(self.root[0].searchkey, "--", self.right.root[0].searchkey)
                else:
                    print(self.root[0].searchkey, "--", '"' + str(self.right.root[0].searchkey) + " | " + str(self.right.root[1].searchkey) + '"')
                self.left.print()
                self.right.print()

        elif len(self.root) == 2:
            if self.left is not None and self.left2 is None and self.mid is not None and self.right2 is None and self.right is not None:
                temp = '"' + str(self.root[0].searchkey) + " | " + str(self.root[1].searchkey) + '"'
                if len(self.left.root) == 1:
                    print(temp, "--", self.left.root[0].searchkey)
                else:
                    print(temp, "--", '"' + str(self.left.root[0].searchkey) + " | " + str(self.left.root[1].searchkey) + '"')

                if len(self.mid.root) == 1:
                    print(temp, "--", self.mid.root[0].searchkey)
                else:
                    print(temp, "--", '"' + str(self.mid.root[0].searchkey) + " | " + str(self.mid.root[1].searchkey) + '"')

                if len(self.right.root) == 1:
                    print(temp, "--", self.right.root[0].searchkey)
                else:
                    print(temp, "--", '"' + str(self.right.root[0].searchkey) + " | " + str(self.right.root[1].searchkey) + '"')
                self.left.print()
                self.mid.print()
                self.right.print()

    def createDot(self, f):
        if len(self.root) == 1:
            if self.left is not None and self.left2 is None and self.mid is None and self.right2 is None and self.right is not None:
                if len(self.left.root) == 1:
                    f.write(str(self.root[0].searchkey) + " -- " + str(self.left.root[0].searchkey) + "\n")
                else:
                    f.write(str(self.root[0].searchkey) + " -- " + '"' + str(self.left.root[0].searchkey) + " | " + str(self.left.root[1].searchkey) + '"\n')
                if len(self.right.root) == 1:
                    f.write(str(self.root[0].searchkey) + " -- " + str(self.right.root[0].searchkey) + "\n")
                else:
                    f.write(str(self.root[0].searchkey) + " -- " + '"' + str(self.right.root[0].searchkey) + " | " + str(self.right.root[1].searchkey) + '"\n')
                self.left.createDot(f)
                self.right.createDot(f)

        elif len(self.root) == 2:
            if self.left is not None and self.left2 is None and self.mid is not None and self.right2 is None and self.right is not None:
                temp = '"' + str(self.root[0].searchkey) + " | " + str(self.root[1].searchkey) + '"'
                if len(self.left.root) == 1:
                    f.write(temp + " -- " + str(self.left.root[0].searchkey) + "\n")
                else:
                    f.write(temp + " -- " + '"' + str(self.left.root[0].searchkey) + " | " + str(self.left.root[1].searchkey) + '"\n')

                if len(self.mid.root) == 1:
                    f.write(temp + " -- " + str(self.mid.root[0].searchkey) + "\n")
                else:
                    f.write(temp + " -- " + '"' + str(self.mid.root[0].searchkey) + " | " + str(self.mid.root[1].searchkey) + '"\n')

                if len(self.right.root) == 1:
                    f.write(temp + " -- " + str(self.right.root[0].searchkey) + "\n")
                else:
                    f.write(temp + " -- " + '"' + str(self.right.root[0].searchkey) + " | " + str(self.right.root[1].searchkey) + '"\n')
                self.left.createDot(f)
                self.mid.createDot(f)
                self.right.createDot(f)

    def inorder(self):
        if len(self.root) == 1:
            if self.left:
                self.left.inorder()
            print(self.root[0])
            if self.right:
                self.right.inorder()
        elif len(self.root) == 2:
            if self.left:
                self.left.inorder()
            print(self.root[0])
            if self.mid:
                self.mid.inorder()
            print(self.root[1])
            if self.right:
                self.right.inorder()

    def inorderDot(self, f):
        if len(self.root) == 1:
            if self.left:
                self.left.inorderDot(f)
            f.write(" -> " + str(self.root[0]))
            if self.right:
                self.right.inorderDot(f)
        elif len(self.root) == 2:
            if self.left:
                self.left.inorderDot(f)
            f.write(" -> " + str(self.root[0]))
            if self.mid:
                self.mid.inorderDot(f)
            f.write(" -> " + str(self.root[1]))
            if self.right:
                self.right.inorderDot(f)

    def goleft(self):
        if self.left is None:
            return self
        return self.left.goleft()

class Tree:
    def __init__(self):
        self.root = None
        self.dotindex = 1
        self.dotinorderindex = 1

    def __str__(self):
        print("_____________________________________________________")
        self.printTree()
        return "_____________________________________________________"

    def isEmpty(self):
        if self.root:
            return False
        return True

    def insertItem(self, value):
        if isinstance(value, int) or isinstance(value, float):
            value = Test(value)
        if self.root is None:
            self.root = Node()
            self.root.root = [value]
            return True
        else:
            if self.retrieveItem(value.searchkey) is None:
                self.root.insert(value)
                return True
            else:
                return False

    def retrieveItem(self, key):
        if self.root is None:
            return None
        else:
            return self.root.find(key)

    def deleteItem(self, key):
        bestaat = self.retrieveItem(key)
        if bestaat:
            self.root.delete(key, self)
        return bestaat

    def printTree(self):
        print("Graph G {")
        if not self.isEmpty():
            if self.root.left is None and self.root.mid is None and self.root.right is None:
                if len(self.root.root) == 1:
                    print(self.root.searchkey)
                else:
                    print('"' + str(self.root.root[0].searchkey), "|", str(self.root.root[1].searchkey) + '"')
            else:
                self.root.print()
        print("}")

    def createDot(self):
        f = open("23-" + str(self.dotindex) + ".dot", "w")
        f.write("Graph G {\n")
        if not self.isEmpty():
            if self.root.left is None and self.root.mid is None and self.root.right is None:
                if len(self.root.root) == 1:
                    f.write(str(self.root.searchkey) + "\n")
                else:
                    f.write('"' + str(self.root.root[0].searchkey) + " | " + str(self.root.root[1].searchkey) + '"\n')
            else:
                self.root.createDot(f)
        f.write("}\n")
        self.dotindex += 1

    def inorderDot(self):
        f = open("23-inorder-" + str(self.dotinorderindex) + ".dot", "w")
        f.write("digraph G {\n")
        f.write("Inorder")
        self.root.inorderDot(f)
        f.write("\nrankdir=LR\n")
        f.write("}\n")
        self.dotinorderindex += 1

    def inorder(self):
        print("_____________________________________________________")
        print("Inorder:")
        self.root.inorder()
        print("_____________________________________________________")


class Test:
    def __init__(self, key):
        self.searchkey = key

    def __str__(self):
        return str(self.searchkey)

