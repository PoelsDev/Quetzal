class Bestelling:
    def __init__(self, gebruikersid, timestamp, ingredienten):
        self.credits = 5 + len(ingredienten)
        self.gebruikersid = gebruikersid
        self.timestamp = timestamp
        self.ID = gebruikersid + str(self.credits)
        self.afgehaald = False
        self.ingredients = ingredienten
        self.prijs = 2
        for ingredient in ingredienten:
            if ingredient.type == "melk" or ingredient.type == "zwart" or ingredient.type == "wit" or ingredient.type == "bruin":
                self.prijs += 1
            elif ingredient.type == "honing":
                self.prijs += 0.5
            elif ingredient.type == "chili":
                self.prijs += 0.25
            elif ingredient.type == "marshmallow":
                self.prijs += 0.75



    # def add_Next(self, bestelling):
    #     """
    #     add_Next() voegt een (volgende) bestelling toe die toevallig dezelfde is op vlak van bestelling en tijdstip.
    #     :param bestelling: Bestelling met zelfde waarden die als next wordt toegevoegd.
    #     :return:
    #     """
    #     if self.next is None:
    #         self.next = bestelling
    #     else:
    #         self.next.add_Next(bestelling)

    def getKey(self):
        """
        +getKey(): integer
        Deze functie geeft van het object de timestamp attribuut terug.
        :return: self.timestamp
        Pre-condities: geen
        Post-condities: de attribuut "timestamp" zal teruggegeven worden.
        """
        return self.timestamp

    def __str__(self):
        return f'Bestelling | Credits: {self.credits}, GebruikersID: {self.gebruikersid}, Timestamp: {self.timestamp}, ChocolademelkID: {self.chocolademelk_id}, Afgehaald(True/False): {self.afgehaald}.'
