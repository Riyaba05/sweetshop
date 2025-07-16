from src.sweet import Sweet

class SweetShop:
    def __init__(self):
        self.sweets = []
        self.next_id = 1000

    def add_sweet(self, name, category, price, quantity):
        self.next_id += 1
        sweet = Sweet(self.next_id, name, category, price, quantity)
        self.sweets.append(sweet)

    def get_all_sweets(self):
        return self.sweets
