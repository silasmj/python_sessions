class S:

    def __init__(self):
        self.cards = ['A', 'K', 39, 102] # public

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        return self.cards + other.cards

    def __repr__(self):
        return f'{self.__dict__}'
    
    def __str__(self):
        return f'Cards: {self.cards}'
    
    def __setitem__(self, key, item):
        self.cards[key] = item

    def __getitem__(self, key):
        return self.cards[key]
    
    def __delitem__(self, key):
        del(self.cards[key])
