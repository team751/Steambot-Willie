import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def listen():
    data, address = sock.recvfrom(1024) # buffer size is 1024 bytes
    message = data.decode('utf-8')
    print("received message: " + message)
    
if __name__ == '__main__':
    listen()