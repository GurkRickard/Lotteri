import random

class Lotteri:
    def __init__(self):
        
        self.list_vinster = [
        "Solstol",
        "Röd Porsche",
        "Handduk",
        "10 Liter Tvål",
        "BMX Cykel",
        "Surf Bräda",
        "Burton Snowboard",
        "Ocklebo 500",
        "Lyx Yacht",
        "Iphone 2"
        ]

        def get_vinst(self):
            slumptal = random.randint(0, 9)
            return self.list_vinster[slumptal]
        