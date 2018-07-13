import json
from StompSender4Unity import *


char_name = "FuseCharacter"
stompSender = StompSender4Unity()
stompSender.init_network()
str_text = "hi, my name is "
msg = "<speech>" + str_text + "</speech>"
#msg_xml = stompSender.add_xml(msg)
#print("sending: " + msg_xml)
#stompSender.send_BML(char_name, msg_xml)

time.sleep(2)

while(1):
    #cmd = "tick: " + str(time.time());

    for ii in range(1, 100):
        cmd = json.dumps({'character': char_name, 'blendshape_ctrl': {'mesh': 'Tops','blendshapes_names': [ 'Tops_BreatheChest', 'Tops_BreatheStomach' ], 'blendshapes_weights': [ii,ii]}}, separators=(',',':'))
        print("sending: " + cmd)
        stompSender.send_JSON(cmd)
        time.sleep(.02)

    for ii in range(100, 1, -1):
        cmd = json.dumps({'character': char_name, 'blendshape_ctrl': {'mesh': 'Tops','blendshapes_names': [ 'Tops_BreatheChest', 'Tops_BreatheStomach' ], 'blendshapes_weights': [ii,ii]}}, separators=(',',':'))
        print("sending: " + cmd)
        stompSender.send_JSON(cmd)
        time.sleep(.02)

    #print("sending: " + msg_xml)
    #stompSender.send_BML(char_name, msg_xml)
    #time.sleep(2)

stompSender.finit_network()

# to test, run
# c:\Python27\Scripts>..\python.exe stomp
# subscribe /topic/DEFAULT_SCOPE
