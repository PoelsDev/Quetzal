class Bestelling:
    def __init__(self, credits, gebruikersid, timestamp, chocolademelk_id, afgehaald, next=None):
        self.credits = credits
        self.gebruikersid = gebruikersid
        self.timestamp = timestamp
        self.chocolademelk_id = chocolademelk_id
        self.afgehaald = afgehaald
        self.next = next

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
