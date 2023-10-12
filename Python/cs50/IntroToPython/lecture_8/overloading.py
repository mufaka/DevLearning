class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts 
    
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    # overload + operator (look at special method names in python)
    def __add__(self, other):
        added = Vault(self.galleons, self.sickles, self.knuts)
        added.galleons += other.galleons
        added.sickles += other.sickles
        added.knuts += other.knuts 
        return added 


potter = Vault(100, 50, 25)
weasley = Vault(25, 50, 100)
combined = potter + weasley 

print(potter)
print(weasley)
print(combined)
