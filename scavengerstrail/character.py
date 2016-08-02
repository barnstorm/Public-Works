
class Character(object):
    def __init__(self, name, description, attack, defense, load, maxload, hp):
        self.name = name
        self.description = description
        self.attack = attack
        self.defense = defense
        self.load = load
        self.maxload = maxload
        self.hp = hp
        self.inv = list()
    class Inventory(object):
        def __init__(self):
            for i in inv:

            free = self.maxload - self.load

        def addInventory(self,item):
            if avail > item[u'load']:
                self.inv.append(item)
                print('added ' + item[u'load'] + ' to inventory')

    def isAlive(self):
        return self.hp > 0

    def dropInventory(self):




class Trader(Character):
    def __init__(self, cunning, reputation):
        self.cunning = cunning
        self.reputation = reputation

class Player(Trader):