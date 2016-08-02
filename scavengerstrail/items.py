class Item(object):
    def __init__(self, name, description, load, value):
        self.name = name
        self.description = description
        self.load = load
        self.value = value


class Consumable(Item):
    def __init__(self, **itemDict):
        self.count = itemDict[u'count']
        self.title = itemDict[u'title']
        self.reqs = itemDict[u'reqs']
        super(Consumable,self).__init__(name=itemDict[u'name'],description=itemDict[u'description'],load=itemDict[u'load'],value=itemDict[u'value'])


class Weapon(Consumable):
    def __init__(self, **weapDict):
        self.title = weapDict[u'title']
        self.reqs = weapDict[u'reqs']
        super(Weapon,self).__init__(name=weapDict[u'name'],description=weapDict[u'description'],load=weapDict[u'load'],value=weapDict[u'value'])


