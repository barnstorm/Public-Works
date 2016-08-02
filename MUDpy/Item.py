'''
Created on Jan 25, 2016

@author: barmstrong
'''

class Item():
    '''
    the basic item class!
    '''


    def __init__(self, name, description, value):
        '''
        Constructor
        '''
        self.name = name
        self.description = description
        self.value = value
        
    def __str__(self):
        return "{}\n====\n{}\Value: {}\n".format(self.name, self.description, self.value)
    
    
class Gold(Item):
    def __init__(self, amt):
        super().__init__(name="Gold",
                             description="A round coin with {} stamped on it",
                             value=self.amt)
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
            
        def __str__(self):
            return "{}\n=====\n{}Value: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
        
        
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A ROCK BITCH",
                         value=0,
                         damage=5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="a stabby thing",
                         value=10,
                         damager=10)    
                