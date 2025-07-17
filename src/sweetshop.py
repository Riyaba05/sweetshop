from src.sweet import Sweet

class SweetShop:
    def __init__(self):
        self.sweets = {}

    def add_sweet(self, sweet):
        self.sweets[sweet.id] = sweet

    def delete_sweet(self, sweet_id):
        if sweet_id in self.sweets:
            del self.sweets[sweet_id]

    def get_all_sweets(self):
        return list(self.sweets.values())

