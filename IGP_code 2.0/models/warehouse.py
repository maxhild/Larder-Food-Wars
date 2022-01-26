import random
#mit dieser KLasse soll ein externes lagerhaus simuliert werden. Der stock kann nicht vom admin einfach so verändert werden sondern
#hängt von der rückmeldung des Lagerhauses ab, um Fehleingaben des Admins zu vermeiden
class Warehouse:

    def __init__(self):

        self.stock = random.randint(1, 50)

    def view_stock(self):

       print("Stock:", self.stock)




