class node:
    def __init__(self,key,priority):
        self.key = key
        self.priority = priority

class PriorityQueue:
    def __init__(self,name = None):
        self.name = name
        self.index = -1
        self.items = []
    
    def enqueue(self,value,priority):
        temp = node(value,priority)
        self.items.append(temp)
        self.index += 1
    
    def peak(self):
        ind = 0
        if (self.index == -1):
            return -1
        else:
            for i in range(self.index+1):
                if (self.items[ind].priority < self.items[i].priority):
                    ind = i
        return ind

    def dequeue(self):
        ind = self.peak()
        if (ind >= 0):
            del self.items[ind]
        else:
            print("Priority Queue Is empty")
        self.index -= 1
    
    def getElements(self):
        return [self.items[i].key for i in range(len(self.items))]

PQ = PriorityQueue('New')
PQ.enqueue(1,10)
PQ.enqueue(2,8)
PQ.enqueue(3,9)
PQ.enqueue(4,1)
PQ.enqueue(5,5)
print(PQ.getElements())
PQ.dequeue()
print(PQ.getElements())
PQ.dequeue()
print(PQ.getElements())
PQ.dequeue()
print(PQ.getElements())
PQ.dequeue()
print(PQ.getElements())
PQ.dequeue()
print(PQ.getElements())
PQ.dequeue()
print(PQ.getElements())
