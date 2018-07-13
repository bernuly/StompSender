
import time
import sys
import urllib
import random
import datetime
import stomp


class StompSender4Unity():
    headers = {}

    def __init__(self):
        self.headers['ELVISH_SCOPE'] = 'UNITY_BML'
        self.headers['MESSAGE_PREFIX'] = 'vrSpeak'
        host_and_ports = [('localhost', 61613)]
        self.conn = stomp.Connection(host_and_ports=host_and_ports)

    def init_network(self):
        self.conn.start()
        self.conn.connect(username='admin', passcode='password', wait=True)
        self.conn.auto_content_length = False

    def finit_network(self):
        self.conn.disconnect()

    def add_xml(self, char_name, msg):
        """ convenience function to add xml prefix and suffix to message """
        random.seed(time.time())
        ID="%03d%s" % (random.randint(0,999), '{:%M%S}'.format(datetime.datetime.now()))
        return "<xml><bml id=\"" + ID + "\" characterId=\"" + char_name + "\">" + msg + "</bml></xml>"
        #return "<?xml version=\"1.0\" ?><act><bml>" + msg + "</bml></act>"

    def send_BML(self, char_name, msg):
        """ send BML message. Assumes message is complete xml statement including prefix/suffix """
        self.conn.send(body=msg, headers=self.headers, destination='/topic/UNITY_BML')

    def send_JSON(self, msg):
        """ send SmartBody python command """
        self.conn.send(body=msg, headers=self.headers, destination='/topic/UNITY_JSON')

    def send_msg(self, prefix, msg):
        msg = prefix + " " + urllib.quote_plus(msg)
        #print(msg)
        self.conn.send(body=msg, headers=self.headers, destination='/topic/DEFAULT_SCOPE')
