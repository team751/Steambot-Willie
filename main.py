import server
from random import random
from twisted.internet import task, reactor

def moveToGear(xOffset, yOffset, orientation):
    
    pass

def testSendoff():
    for i in range(10):
        left = random()
        right = random()
        print("Left: " + str(left) + ", Right: " + str(right))
        server.sendJoystickData(left, right)

if __name__ == '__main__':
    server.listen()
    reactor.callLater(3.5, testSendoff)
    #l = task.LoopingCall(testSendoff)
    #l.start(1.0) # call every second
    reactor.run()
    
    