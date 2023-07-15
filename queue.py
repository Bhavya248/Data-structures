#Implementing Simple Queue

class Queue:
    def __init__(self):
        self.items = []
        self.head = 0
        self.tail = 0

    def push(self,item): #enqueue operation
        self.items.append(item)
        self.tail += 1

    def pop(self):  #dequeue operation
        self.items[self.head] = ''
        self.head += 1

    def getElements(self):
        return self.items

    def isEmpty(self):
        if (self.head == self.tail):
            return True
        else:
            return False

    def length(self):
        return len(self.items)

Q = Queue()
print(Q.isEmpty())
Q.push(100)
print(Q.getElements())

#Implementing Circular Queue

class QueueOverflowError(Exception):
    pass

class Cqueue:
    def __init__(self,n):
        self.items = ['' for i in range(n)]
        self.head = -1
        self.tail = -1
        
    def enqueue(self,item):
        try :
            self.tail += 1
            if (self.tail == len(self.items)):
                self.tail = 0
            if (self.head == -1):
                    self.head = 0
            if (self.items[self.tail] == ''):
                self.items[self.tail] = item
            else:
                raise QueueOverflowError
            
        except QueueOverflowError :
            print("No Empty Space In Queue, Try Dequeue operation")
            self.tail -= 1
            
    def dequeue(self):
        self.items[self.head] = ''
        self.head += 1
        if (self.head == len(self.items)):
            self.head = 0

    def getElements(self):
        return self.items

    def isEmpty(self):
        if(self.head == self.tail): return True
        else: return False

'''CQ = Cqueue(3)
print(CQ.isEmpty())
CQ.enqueue(100)
CQ.enqueue(200)
CQ.enqueue(300)
CQ.enqueue(400)
print(CQ.getElements())
CQ.dequeue()
print(CQ.head,CQ.tail)
CQ.enqueue(400)
print(CQ.head,CQ.tail)
print(CQ.getElements())'''

