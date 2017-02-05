from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class EncoderListenDatagramProtocol(DatagramProtocol):
    def datagramReceived(self, datagram, host):
        print('Datagram received: ' + repr(datagram))

class JoystickControlDatagramProtocol(DatagramProtocol):
    def __init__(self):
        super(JoystickControlDatagramProtocol, self).__init__()
    def sendDatagram(self, message):
        datagram = bytes(message, 'utf-8')
        self.transport.write(datagram, ('127.0.0.1', 8000)) # <- write to broadcast address here

joystick_protocol = JoystickControlDatagramProtocol() # so don't need to reinitialize all the time
reactor.listenUDP(8001, joystick_protocol) #soooooo yeah you need to bind it to a random port idk why but hey it works

def sendJoystickData(horizontal_axis, vertical_axis):
    joystick_protocol.sendDatagram("[" + str(horizontal_axis) + "," + str(vertical_axis) + "]")

def listen():
    encoder_protocol = EncoderListenDatagramProtocol()
    #0 means any port
    t = reactor.listenUDP(8000, encoder_protocol)
