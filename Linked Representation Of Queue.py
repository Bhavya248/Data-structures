#implement Queue Using LinkedList
from LinkedList import node,LinkedList

class Queue(LinkedList):
    def __init__(self,_name):
        self.name = _name
        self.Head = None
        self.prev = None
        self.counter = 0

    def deleteNode(self):
        _temp = self.Head
        self.Head = _temp.next
        del _temp
        i = self.Head
        while(i != None):
            i.index -= 1
            i = i.next
            
a = Queue("My Linked List")
a.addNode(100)
a.addNode(200)
a.addNode(300)
print(a.getAllElements())
a.deleteNode()
print(a.getAllElements())
a.deleteNode()
print(a.getAllElements())
a.deleteNode()
print(a.getAllElements())

