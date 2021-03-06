from System.UserObjects.hulpFunctie import *


class Bestelling:
    def __init__(self, gebruikersid, timestamp, ingredienten, stock):
        self.credits = 5 + len(ingredienten)
        self.gebruikersid = gebruikersid
        self.timestamp = timestamp
        self.ID = gebruikersid + str(self.credits)
        self.afgehaald = False
        self.ingredients = ingredienten  # vector of which and how much ingredients that is needed to make the order
        self.prijs = 2  # standard price of an order
        self.enoughstock = True  # true when there is enough of the ingredients in stock to process the order (bestelling)
        # Checks if there is enough in stock of the ingredients that is needed for the order (bestelling)
        for ingredient in ingredienten:
            if ingredient == "honing" or ingredient == "marshmallow" or ingredient == "chili":
                if len(stock.ingredient[ingredient].traverse()) < ingredienten.count(ingredient):
                    self.enoughstock = False
            elif ingredient == "wit" or ingredient == "zwart" or ingredient == "bruin" or ingredient == "melk":
                if len(stock.shot[ingredient].traverse()) < ingredienten.count(ingredient):
                    self.enoughstock = False
        # If there is indeed enough in stock to process the order the stock will be updated and the price as well
        if self.enoughstock:
            for ingredient in ingredienten:
                if ingredient == "melk":
                    self.prijs += 1
                    stock.melk.delete() # deletes one instant of the ingredient from the stock
                elif ingredient == "zwart":
                    self.prijs += 1
                    stock.zwart.delete()
                elif ingredient == "wit":
                    self.prijs += 1
                    stock.wit.delete()
                elif ingredient == "bruin":
                    self.prijs += 1
                    stock.bruin.delete()
                elif ingredient == "honing":
                    self.prijs += 0.5
                    stock.honing.delete()
                elif ingredient == "chili":
                    self.prijs += 0.25
                    stock.chili.delete()
                elif ingredient == "marshmallow":
                    self.prijs += 0.75
                    stock.marshmallow.delete()



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
        return self.ID

    def __str__(self):
        return f'Bestelling | Credits: {self.credits}, GebruikersID: {self.gebruikersid}, Timestamp: {self.timestamp}, ChocolademelkID: {self.chocolademelk_id}, Afgehaald(True/False): {self.afgehaald}.'
