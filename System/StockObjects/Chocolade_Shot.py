class Cshot:
    def __init__(self, type, vervaldatum, searchkey):
        self.type = type
        self.vervaldatum = vervaldatum
        self.basisprijs = 1.0
        self.searchkey = searchkey

    def getKey(self):
        return self.searchkey
