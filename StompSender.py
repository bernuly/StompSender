import time
import sys
import urllib

import stomp

class StompSender():
    headers = {}

    def __init__(self):
        self.headers['ELVISH_SCOPE'] = 'DEFAULT_SCOPE'
        self.headers['MESSAGE_PREFIX'] = 'vrSpeak'
        self.conn = stomp.Connection()

    def init_network(self):
        self.conn.start()
        self.conn.connect('admin', 'password', wait=True)
        self.conn.auto_content_length = False

    def finit_network(self):
        self.conn.disconnect()

    def add_xml(self, msg):
        """ convenience function to add xml prefix and suffix to message """
        return "<?xml version=\"1.0\" ?><act><bml>" + msg + "</bml></act>"

    def send_BML(self, char_name, msg):
        """ add BML message. Assumes message is complete xml statement including prefix/suffix """
        self.send_msg("vrSpeak", char_name, msg)

    def send_SB(self, char_name, msg):
        """ send SmartBody python command """
        self.send_msg("sb", char_name, msg)

    def send_msg(self, prefix, char_name, msg):
        msg = prefix + " " + urllib.quote_plus(char_name + " " + msg)
        self.conn.send(body=msg, headers=self.headers, destination='/topic/DEFAULT_SCOPE')

# msgBML = "FuseCharacter ALL bml_25722044 <?xml version='1.0' ?><act><bml><face au='9' type='facs' side='BOTH' start='0' end='0.4' amount='0.2'/><face au='27' type='facs' side='BOTH' start='0' end='0.4' amount='0.2'/></bml></act>"
#msg = "FuseCharacter+ALL+bml_25722044+%3c%3fxml+version%3d%221.0%22+%3f%3e%3cact%3e%3cbml%3e%3cface+au%3d%229%22+type%3d%22facs%22+side%3d%22BOTH%22+start%3d%220%22+end%3d%220.4%22+amount%3d%220.2%22%2f%3e%3cface+au%3d%2227%22+type%3d%22facs%22+side%3d%22BOTH%22+start%3d%220%22+end%3d%220.4%22+amount%3d%220.2%22%2f%3e%3c%2fbml%3e%3c%2fact%3e+"
#        print(msg)
