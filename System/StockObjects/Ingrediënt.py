

class Ingredient:
    def __init__(self, type, vervaldatum):
        self.vervaldatum = int(vervaldatum)
        self.type = type
        if type == "chili":
            self.prijs = 0.25
        elif type == "honing":
            self.prijs = 0.5
        elif type == "marshmallow":
            self.prijs = 0.75

