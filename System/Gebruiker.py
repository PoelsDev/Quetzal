class Gebruiker:
    def __init__(self, ID, voornaam, achternaam, email):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.email = email
        self.ID = ID
        self.searchkey = ID


    def getKey(self):
        """
        Returned de searchkey
        :return: searchkey
        """
        return self.searchkey
