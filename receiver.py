import asyncio

UDP_IP = "127.0.0.1"
UDP_PORT = 5005 # 6000 probs

leftEncoder = 0.0
rightEncoder = 0.0    
    
class EchoServerProtocol:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode('utf-8')
        comma_location = message.find(',')
        leftEncoder = float(message[1:comma_location])
        rightEncoder = float(message[comma_location+1:-1])
        print("Left: " + str(leftEncoder) + ", Right: " + str(rightEncoder))

def listen():
    loop = asyncio.get_event_loop()
    print("Starting UDP server")
    # One protocol instance will be created to serve all client requests
    listen = loop.create_datagram_endpoint(
        EchoServerProtocol, local_addr=(UDP_IP, UDP_PORT))
    transport, protocol = loop.run_until_complete(listen)
    
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    
    transport.close()
    loop.close()
    print("server started")