from actions import Victory
import random
import math
from actions import Do

class Character(object):
    def __init__(self, name, description, attack, defense, load, maxload, hp, attempt):
        self.name = name
        self.description = description
        self.attack = attack
        self.defense = defense
        self.load = load
        self.maxload = maxload
        self.hp = hp
        self.inv = []
        self.equipped = {}
        self.attempt = attempt
    def isAlive(self):
        return self.hp > 0
    def inventory(self, action, item=''):
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
    def fight(self):
        if 'weapon' in self.equipped:
            return sum(Do.roll(self.equipped['weapon']['dmg']))
        else:
            return sum(Do.roll(1,6,1))

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


class Player(Character):
    def __init__(self, name):
        self.name = name
        self.attack = sum([random.randint(6, 15), 5])
        self.cunning= sum([random.randint(20, 30), -self.attack], 5)
        self.defense = int(sum([self.cunning , self.attack])/2)
        self.hp = int(sum([self.attack, self.defense, self.cunning])/3 + 5)
        self.description = 'The Player Character'
        self.maxload = int(sum([self.attack, self.defense])/2 * 5)
        self.inv = list()
        self.equipped = {}
        self.reputation=0
        self.load=0
        self.attempt=4




