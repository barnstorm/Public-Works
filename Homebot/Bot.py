import xmpp
import time
import re
import os
import json
from Worker import *

class Dict2Obj(object):
    """
    Turns a dictionary into a class
    """
    def __init__(self, dictionary):
        """Constructor"""
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def __repr__(self):
        """"""
        return "<Dict2Obj: %s>" % self.__dict__

class Chat(object):
    def __init__(self, username='user', password='passwd', server=(server, 5223)):
        self.username = username
        self.password = password
        self.server = server

    def message_handler(self, connect_object, message_node):
        us = str(message_node.getFrom()).split('/')[0]
        if us == 'bill@armstravaganza.com':
            us = us[0:4]
            print str(message_node)
            s= str(message_node.getBody()).replace("\n", "\t")
            if s != 'None' :
                mp3 = re.compile('#getaudio$')
                vid = re.compile('#getvideo$')
                toamazon = re.compile('#toamazon$')
                print "MESSAGE: " + s
                if mp3.findall(s):
                    url = mp3.split(s)[0]
                    res = "transcoding " + url
                    connect_object.send(xmpp.Message( message_node.getFrom() , res, typ='chat' ))
                    title = getaudio(url)
                    finished = "Finished " + res + title
                    connect_object.send(xmpp.Message( message_node.getFrom() , finished, typ='chat' ))
                else:
                    nothing = 'Nothing to do with:\n' + s
                    print "Nothing"
                    connect_object.send(xmpp.Message( message_node.getFrom() ,nothing, typ='chat' ))

    def communicator(self):
        jid = xmpp.JID(self.username)
        connection = xmpp.Client(jid.getDomain())
        connection.connect(self.server)
        result = connection.auth(jid.getNode(), password )
        connection.RegisterHandler('message', self.message_handler)
        connection.sendInitPresence()
        while connection.Process(1):
            pass

if __name__ == '__main__':
    username="homebot@armstravaganza.com"
    password="!@qwASzx"
    server=('talk.google.com', 5223)