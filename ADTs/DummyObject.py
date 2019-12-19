class DummyObject:
    def __init__(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def __str__(self):
        return str(self.key)
