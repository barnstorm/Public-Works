
from character import Player
from actions import Do

def play():
    player = Player('Bill')
    while player.isAlive():
        fight = Do(player)
        return fight.combat()


if __name__ == '__main__':
    play()