import json
from StompSender import *


char_name = "FuseCharacter"
stompSender = StompSender()
stompSender.init_network()
str_text = "hi, my name is "
msg = "<speech>" + str_text + "</speech>"

ID="%03d%s" % (random.randint(0,999), '{:%M%S}'.format(datetime.datetime.now()))
msg = "<face id=\"" + ID + "\" type=\"FACS\" au=\"1\" amount=\"1.0\"  start=\"0\"/>"
msg = "<faceFacs id=\"" + ID + "\" au='2'  side=\"BOTH  \" amount=\"0\" start=\"0\" end=\"5\"/>"
#msg = "<gaze id=\"" + ID + "\" target=\"Cube\" start=\"0\"/>"



msg_xml = stompSender.add_xml(char_name, msg)
print("sending: " + msg_xml)
stompSender.send_BML(char_name, msg_xml)


stompSender.finit_network()

# to test, run
# c:\Python27\Scripts>..\python.exe stomp
# subscribe /topic/DEFAULT_SCOPE
