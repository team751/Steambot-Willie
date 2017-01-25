import socket

UDP_IP = "127.0.0.1"
UDP_IP_BYTES = bytes(UDP_IP, 'UTF-8')
UDP_PORT = 5005
MESSAGE = "Hello, World!"
MESSAGE_BYTES = bytes(MESSAGE, 'UTF-8')

def send():
    print("UDP target IP: " + UDP_IP)
    print("UDP target port: " + str(UDP_PORT))
    print("message: " + MESSAGE)
    
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE_BYTES, (UDP_IP, UDP_PORT))
    print("sent")
    
if __name__ == '__main__':
    send()