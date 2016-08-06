import json
class Item(object):
    def __init__(self, name, title, description, load, value):
        self.name = name
        self.title = title
        self.description = description
        self.load = load
        self.value = value



class Consumable(Item):
    def __init__(self, **itemDict):
        self.count = itemDict[u'count']
        self.title = itemDict[u'title']
        self.reqs = itemDict[u'reqs']


class Weapon(Item):
    def __init__(self, **weapDict):
        self.title = weapDict[u'title']
        self.reqs = weapDict[u'reqs']
        self.dmg = weapDict[u'dmg']
        self.name = weapDict[u'name']
        self.description = weapDict[u'description']
        self.load = weapDict[u'load']
        self.value = weapDict[u'value']

class JsonObj(object):
    def __init__(self, j):
        if type(j) is str:
            self.__dict__ = json.loads(j)
        elif type(j) is dict:
            self.__str__ = json.dumps(j)
