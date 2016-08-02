
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
    def isAlive(self):
        return self.hp > 0
    def inventory(self, action,item=''):
        myinv = Inventory(self.inv, self.maxload)
        if action == 'add':
            if item == '':
                return 'nothing to add'
            return myinv.addInventory(item)
        if action == 'drop':
            if item == '':
                return 'nothing to drop'
            return myinv.dropInventory(item)
        if action == 'show':
            return myinv.showInventory()

class Inventory(object):
    def __init__(self, inv, maxload):
        self.inv = inv
        self.maxload = maxload
        self.load = sum(i[u'load'] for i in self.inv)
        self.avail = self.maxload - self.load
    def addInventory(self,item):
        if self.avail == 0:
            return 'you cannot carry anymore'
        if self.avail >= item[u'load']:
            self.inv.append(item)
            return 'added ' + str(item[u'name']) + ' to inventory'
        else:
            return 'You only have ' + str(self.avail) + ' load available'
    def showInventory(self):
        return self.inv
    def dropInventory(self, dropitem):
        self.inv.remove(dropitem)
        return dropitem['name'] + 'Dropped'

class Trader(Character):
    def __init__(self, cunning, reputation):
        self.cunning = cunning
        self.reputation = reputation
        super(Trader,self).__init__(attack=7,defense=5,hp=3,description='desc',name='Char',maxload=200, load=0)

class Player(Trader):