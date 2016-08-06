import random
import character

class Do(object):
    def __init__(self, pro, con=Player('null'), proAD=4, conAD=4):
        self.pro = pro
        self.con = con
        self.proAD = proAD
        self.conAD = conAD
    @staticmethod
    def roll(start=1, max=6, count=1):
        result = [random.randint(start, max) for i in range(count)]
        return result
    def combat(self):
        attack = sum(Do.roll(self.proAD)) + self.pro.attack
        attackDMG = self.pro.fight()
        defense = sum(Do.roll(self.conAD)) + self.con.attack
        defenseDMG = self.con.fight()
        if self.proAD > 0:
            if attack > defense:
                self.con.hp = self.con.hp - attackDMG
                if self.con.isAlive():
                    self.conAD = self.conAD - 1
                    return self.con.name + " took " + str(attackDMG) +" damage"
                else:
                    return self.con.name + " has DIED!"
            if defense > attack:
                self.pro.hp = self.pro.hp - defenseDMG
                if self.pro.isAlive():
                    self.proAD = self.proAD - 1
                    return self.pro.name + " took " + str(defenseDMG) +" damage"
                else:
                    return self.pro.name + " has DIED!"
        else:
            return "Stunned", "dropped items"
    def selectItems(self):
        localinv = [i for i in self.pro.inventory.showInventory()]
        remoteinv = [i for i in self.con.inventory.showInventory()]
        for i in localinv:
            for l in i.iteritems():

    def tradeNegotiate(self):
        sell = sum(Do.roll(self.proAD)) + self.pro.cunning
        attackDMG = self.pro.fight()
        buy = sum(Do.roll(self.conAD)) + self.con.cunning
        defenseDMG = self.con.fight()
        if self.proAD > 0:
            if sell > buy:
                self.conAD = self.conAD - 1
                return self.con.name + " took " + str(attackDMG) +" damage"
            if buy > sell:
                self.proAD = self.proAD - 1
                return self.pro.name + " WAS DENIED"
        else:
            return self.pro.name + " has run out of luck"
    def tradeOffer(self,proitem,conitem):
        if proitem['value'] > conitem['value']:
            self.pro.inventory('add', conitem)
            self.con.inventory('drop', conitem)
        elif proitem['value'] < conitem['value']:
            self.trade.negotiate()



class Move(object):
    def __init__(self):
        """
        :param:
        :return:
        """
        pass
class Victory(object):
    def __init__(self):
        """
        :param:
        :return:
        """
        pass
class Quit(object):
    def __init__(self):
        """
        :param:
        :return:
        """
        pass
