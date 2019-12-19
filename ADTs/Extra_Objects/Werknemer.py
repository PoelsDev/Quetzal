class Werknemer:
    def __init__(self, id, voornaam, achternaam, workload):
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.workload = workload
        self.currentOrder = None
        self.load = 0

    def giveOrder(self, order):
        """
        +giveOrder(in bestelling:Bestelling): boolean
        Als de werknemer met een bestelling bezig is refereert deze functie naar deze bestelling (zodat beide tijdelijk gelinkt zijn)
        :param bestelling: De bestelling waarmee de werknemer bezig is.
        :return: True als het gelukt is, anders False
        Pre-condities: De parameter moet een instantie zijn van de klasse Bestelling
        Post-condities: De attribuut currentOrder van de werknemer zal ingevuld worden.
        """
        if self.currentOrder is None:
            self.currentOrder = order
            self.load = order.credits
            return True
        return False

    def workOrder(self):
        """
        +workOrder(): boolean
        Als de load van de werknemer niet 0 is wordt de attribuut workload afgetrokken van de load attribuut. Als het wel 0 is dan
        wordt de currentOrder attribuut vrij gemaakt.
        :return: True als de currentOrder leeg is gemaakt, anders False
        Pre-condities: Er moet een load groter dan 0 aanwezig zijn.
        Post-condities: De workload is afgetrokken van de load attribuut.
        """
        pass

    def __str__(self):
        return f'Werknemer | ID: {self.id}, Naam: {self.voornaam} {self.achternaam}, Workload: {self.workload}.'

    def getKey(self):
        """
        +getKey(out workload: integer)
        Deze functie geeft van het object de workload attribuut terug.
        :return: self.workload
        Pre-condities: geen
        Post-condities: de attribuut "timestamp" zal teruggegeven worden.
        """
        return self.workload
