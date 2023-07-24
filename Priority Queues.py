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
