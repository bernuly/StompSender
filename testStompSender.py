from StompSender import *

char_name = "FuseCharacter"
stompSender = StompSender()
stompSender.init_network()
str_text = "hi, my name is "
msg = "<bml><speech>" + str_text + "</speech>"
msg_xml = stompSender.add_xml(msg)

stompSender.send_BML(char_name, msg_xml)
print("sending: " + msg_xml)
time.sleep(2)
# cmd = ""
# stompSender.send_SB(char_name, cmd)
# print("sending: " + cmd)
# time.sleep(2)
stompSender.finit_network()


# to test, run
# c:\Python27\Scripts>..\python.exe stomp
# subscribe /topic/DEFAULT_SCOPE
