class Hero:
    def __init__(self, name, ability):
        self.name=name
        self.ability=ability

class Hero_super(Hero):
    def __init__(self, name, ability):
        super().__init__(name, ability)

    def __str__(self):
        return f'{self.name} is hero'

    def fraze(self):
        print('it is super_hero')

h=Hero('lam', 'fly')
hs=Hero_super('gan', 'very high damage')
