# README for StompSender class
The StompSender class allows to send control messages to SmartBody via ActiveMQ (using the STOMP protocol).<br/>
The class assumes default port and password of the ActiveMQ server.

## Installation
The StompSender requires the stomp.py library (https://github.com/jasonrbriggs/stomp.py). <br/>
On most systems, the library can be installed with<br/>
`pip install stomp.py`

## Testing
To test the code use the `testStompSender.py` script.
To monitor the incoming messages you can use the `stomp` command that is part of stomp.py:
e.g.<br/>
`cd c:\Python27\Scripts`<br/>
`..\python.exe stomp`<br/>
`subscribe /topic/DEFAULT_SCOPE`



`
