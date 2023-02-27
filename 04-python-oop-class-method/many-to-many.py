class Bar:
    def __init__(self, name):
        self.name = name
        self.cocktails = []


class Cocktail:
    def __init__(self, name):
        self.name: name
        self.bars = []


if __name__ == '__main__':
    bar1 = Bar('White Horse')
    bar2 = Bar('Barcelona Bar')

    c1 = Cocktail('Gin & Tonic')
    c2 = Cocktail('Whiskey Sour')
    c3 = Cocktail('Espresso Martini')

    bar1.cocktails = [c1, c2, c3]
    bar2.cocktails = [c1, c2]

    #link the bars to the cocktails
    c1.bars = [bar1, bar2]
    c2.bars = [bar1, bar2]
    c3.bars = [bar1]