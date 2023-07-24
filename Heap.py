class max_heap:
    def __init__(self, name,size):
        self.name = name
        self.size = -1
        self.items = [None]*size

    def getParent(self, index):
        if (index == 0):
            return -1
        elif (index % 2 == 0):
            return (index - 2)//2
        elif (index % 2 == 1):
            return (index - 1)//2
        else:
            return -1

    def heapify(self, ind):
        child = self.items[ind]
        parentIND = self.getParent(ind)
        parent = self.items[parentIND]
        print(parent)
        while (self.size > 0 and parentIND >= 0):
            if (parent < child):
                print(self.items[ind], self.items[parentIND])
                self.items[ind], self.items[parentIND] = self.items[parentIND], self.items[ind]
                print(self.items[ind], self.items[parentIND])
            ind, child, parentIND, parent = (
                parentIND, parent, self.getParent(ind), self.items[parentIND])

    def insert(self, value):
        self.size += 1
        self.items[self.size] = value
        self.heapify(self.size)
    
    def getElements(self):
        return self.items

myheap = max_heap('B',6)
myheap.insert(10)
myheap.insert(20)
myheap.insert(5)
myheap.insert(1)
myheap.insert(11)
myheap.insert(15)
print(myheap.getElements())
