class Vault:
    def __init__(self,galleon = 0,sickle = 0,knut = 0):
        self.galleon = galleon
        self.sickle = sickle
        self.knut = knut


    def __str__(self):
        return f"Galleons: {self.galleon}, Sickle: {self.sickle}, Knut: {self.knut}"


    def __add__(self,other):
        galleons = self.galleon + other.galleon
        sickles = self.sickle + other.sickle
        knuts = self.knut +  other.knut
        return Vault(galleons,sickles,knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)