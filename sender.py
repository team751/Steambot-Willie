import socket
import asyncio

UDP_IP = "127.0.0.1"
UDP_PORT = 5005 # 6001 probs

class EchoClientProtocol:
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('Send:', self.message)
        self.transport.sendto(self.message.encode())

    def datagram_received(self, data, addr):
        print("Received:", data.decode())

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Socket closed, stop the event loop")
        loop = asyncio.get_event_loop()
        loop.stop()

def sendData(message):
    loop = asyncio.get_event_loop()
    connect = loop.create_datagram_endpoint(
        lambda:EchoClientProtocol(message, loop), 
        remote_addr=(UDP_IP, UDP_PORT))
    transport, protocol = loop.run_until_complete(connect)
    loop.run_forever()
    transport.close()
    loop.close()

def sendMotorData(horizontalJoystick, verticalJoystick):
    # open a connection for one and only one. Potentially wasteful but whatever
    message = "[" + horizontalJoystick + "," + verticalJoystick + "]"
    sendData(message)

def sendMockEncoderData(left, right):
    message = "[" + str(left) + "," + str(right) + "]"
    sendData(message)
    