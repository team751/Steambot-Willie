import receiver # listen, then
import sender # receive
import fileinput
from random import random

def moveToGear(xOffset, yOffset, orientation):
    
    pass

if __name__ == '__main__':
    receiver.listen()
    
    for i in range(10):
        left = random()
        right = random()
        print("Left: " + str(left) + ", Right: " + str(right))
        sender.sendMockEncoderData(left, right)
    