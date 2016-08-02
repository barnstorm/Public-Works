class Item(object):
    def __init__(self, name, description, load, value):
        self.name = name
        self.description = description
        self.load = load
        self.value = value


class Consumable(Item):
    def __init__(self, **itemDict):
        self.title = itemDict[u'title']
        self.reqs = itemDict[u'reqs']
        super(Consumable,self).__init__(name=itemDict[u'name'],description=itemDict[u'description'],load=itemDict[u'load'],value=itemDict[u'value'])


class Weapon(Consumable):
    def __init__(self, **weapDict):
        self.title = itemDict[u'title']
        self.reqs = itemDict[u'reqs']
        super(Weapon,self).__init__(name=itemDict[u'name'],description=itemDict[u'description'],load=itemDict[u'load'],value=itemDict[u'value'])


