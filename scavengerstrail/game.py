
from character import Player
from actions import *


def play():
    player = Player('Bill')
    bad = Player('Baddy')
    bad.inventory('add',  {u'description': 'GUN4',
                           u'dmg': [1, 2, 3],
                           u'load': 3,
                           u'name': u'P3distol 4',
                           u'reqs': u'Needs more fun',
                           u'title': u'TITLE4',
                           u'value': 6})
    bad.inventory('add',  {u'description': 'GUN4',
                           u'dmg': [1, 2, 3],
                           u'load': 3,
                           u'name': u'3distol 4',
                           u'reqs': u'Needs more fun',
                           u'title': u'ITLE4',
                           u'value': 67})
    player.inventory('add',  {u'description': 'GUNt4',
                              u'dmg': [1, 2, 3],
                              u'load': 3,
                              u'name': u'tt3distol 4',
                              u'reqs': u'Needs more fun',
                              u'title': u'tITLEtt4',
                              u'value': 666})
    player.inventory('add',  {u'description': 'GUaaasdasdNt4',
                              u'dmg': [1, 2, 3],
                              u'load': 3,
                              u'name': u'tt3distol 4',
                              u'reqs': u'Needs more fun',
                              u'title': u'tITLEtt4',
                              u'value': 6})
    player.inventory('add',  {u'description': 'wGUNt4',
                              u'dmg': [1, 2, 3],
                              u'load': 3,
                              u'name': u't4t3distol 5',
                              u'reqs': u'Needs more fun',
                              u'title': u'tITLEtt4',
                              u'value': 66})
    player.inventory('add',  {u'description': 'wGUNt4',
                              u'dmg': [1, 2, 3],
                              u'load': 3,
                              u'name': u't4t3distol 5',
                              u'reqs': u'Needs more fun',
                              u'title': u'tITLEtt4',
                              u'value': 66})

    playermove = Do.roll()
    print playermove
    act = Fight(player,bad)
    return act.combat()

        #trade = Trade(player,bad)
        #return trade.turn()

if __name__ == '__main__':
    play()