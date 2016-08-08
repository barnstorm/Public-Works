import random
from character import *

class Do(object):
    def __init__(self, pro, con, proAD=4, conAD=4):
        self.pro = pro
        self.con = con
        self.proAD = proAD
        self.conAD = conAD
        self.round = round
    @staticmethod
    def roll(start=1, max=6, count=1):
        result = [random.randint(start, max) for i in range(count)]
        return result

class Fight(Do):
    def __init__(self, pro, con, proAD=4, conAD=4):
        self.pro = pro
        self.con = con
        self.proAD = proAD
        self.conAD = conAD
        self.victory = 0
        self.round = 4
    def combat(self):
        attack = sum(Do.roll(self.proAD)) + self.pro.attack
        attackDMG = self.pro.fight()
        defense = sum(Do.roll(self.conAD)) + self.con.attack
        defenseDMG = self.con.fight()
        while self.round > 0:
            if attack > defense:
                self.con.hp = self.con.hp - attackDMG
                if self.con.isAlive():
                    self.conAD = self.conAD - 1
                    print self.con.name + " took " + str(attackDMG) +" damage"
                    self.victory = self.victory + 1
                    retry = raw_input("Try again for the same?[1] ")
                    if retry == '1':
                        self.round = self.round - 1
                        if self.round == 0 and self.victory >= 3:
                            print 'you win'
                            self.randDrop(self.con,self.pro)
                        else:
                            self.combat()
                else:
                    print self.con.name + " has DIED!"
                    return self.randDrop(self.con, self.pro)
            if defense > attack:
                self.pro.hp = self.pro.hp - defenseDMG
                if self.pro.isAlive():
                    self.proAD = self.proAD - 1
                    print self.pro.name + " took " + str(defenseDMG) +" damage"
                    retry = raw_input("Try again for the same?[1] ")
                    if retry == '1':
                        self.round = self.round - 1
                        if self.round == 0 and self.victory < 2:
                            print 'you lost'
                            self.randDrop(self.pro,self.con)
                        else:
                            self.combat()
                else:
                    print self.pro.name + " has DIED!"
                    return 'GAME OVER'
            if defense == attack:
                print "Miss"
                retry = raw_input("Try again for the same?[1] ")
                if retry == '1':
                    self.round = self.round - 1
                    if self.round == 0 and self.victory < 2:
                        print 'you lost'
                        self.randDrop(self.pro,self.con)
                    else:
                        self.combat()
    def randDrop(self,combatant, victor):
            charinv = combatant.inventory('show')
            inv = {charinv.index(i): i for i in charinv}
            m = int(len(charinv) - 1)
            if m > 0:
                #print inv
                dropnum = random.randint(0, m)
                print dropnum
                item = inv[dropnum]
                combatant.inventory('drop', item), victor.inventory('add', item)
                print combatant.name + " dropped " + str(item)
                return combatant.name + " dropped " + str(item)
            elif m == 0:
                item = inv[0]
                combatant.inventory('drop', item), victor.inventory('add', item)
                print combatant.name + " dropped " + str(item)
            else:
                return



class Trade(Do):
    def __init__(self, pro, con, proAD=4, conAD=4):
        self.pro = pro
        self.con = con
        self.proAD = proAD
        self.conAD = conAD
        self.round = 2
        self.tradeitems = {}
    def tradeNegotiate(self):
        conitem = self.tradeitems[self.con.name]
        sell = sum(Do.roll(self.proAD)) + self.pro.cunning + self.pro.reputation
        buy = sum(Do.roll(self.conAD)) + self.con.cunning + self.pro.reputation
        if self.proAD > 0:
            if self.round > 0:
                if sell > buy:
                    self.conAD = self.conAD - 1
                    self.pro.inventory('add', conitem)
                    self.con.inventory('drop', conitem)
                    self.pro.reputation = self.pro.reputation + 1
                    print "Using his superior trading skills (cunning: " + str(sell) + \
                          " vs. " + str(buy) + ") " + self.pro.name + " traded " + str(conitem) + " with " + self.con.name
                    return "Traded"
                if buy > sell:
                    self.proAD = self.proAD - 1
                    print self.pro.name + " WAS DENIED"
                    print self.con.name + " (cunning: " + str(buy) + " vs. " + str(sell) + ")"
                    retry = raw_input("Try again for the same?[1] Try for a new trade?[2] ")
                    if retry == '1':
                        self.round = self.round - 1
                        self.tradeNegotiate()
                    elif retry == '2':
                        self.round = self.round = 2
                        self.turn()
                    else:
                        print "quitter"
                        return "quit"
                    return self.pro.name + " WAS DENIED"
                if buy == sell:
                    self.proAD = self.proAD - 1
                    self.conAD = self.conAD - 1
                    print "It's a draw. " + str(self.pro.name) + " and " + str(self.con.name) + " got " + str(sell)
                    retry = raw_input("Try again for the same?[1] Try for a new trade?[2] ")
                    if retry == '1':
                        self.round = self.round - 1
                        self.tradeNegotiate()
                    elif retry == '2':
                        self.round = self.round = 2
                        self.turn()
                    return "its a draw"
            else:
                print self.pro.name + " has run out of luck inner"
        else:
            print self.pro.name + " has run out of luck outer"
            return self.pro.name + " has run out of luck"
    def tradeOffer(self,tradeitems):
        conitem = tradeitems[self.con.name]
        if tradeitems[self.pro.name]['value'] > tradeitems[self.con.name]['value']:
            self.pro.inventory('add', conitem)
            self.con.inventory('drop', conitem)
            print "Fair Trade"
        elif tradeitems[self.pro.name]['value'] < tradeitems[self.con.name]['value']:
            self.tradeNegotiate()
    def turn(self):
        while self.round > 0:
            if self.round >= 2:
                charinv = self.pro.inventory('show')
                inv = {charinv.index(i): i for i in charinv}
                print inv
                self.round = self.round - 1
                self.selectItems(self.pro.name, inv)
            elif self.round >= 1:
                charinv = self.con.inventory('show')
                inv = {charinv.index(i): i for i in charinv}
                print inv
                self.selectItems(self.con.name, inv)
                self.tradeOffer(self.tradeitems)
                return self.tradeitems
            else:
                return
    def selectItems(self, owner, inv):
        itemnum = input("choose item number from " + owner + "'s Inventory: ")
        item = inv[itemnum]
        return self.tradeitems.update({str(owner): item})


