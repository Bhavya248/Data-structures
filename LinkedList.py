#Implementation of LinkedList

class node:
    def __init__(self,_index,_data = None):
        self.index = _index
        self.data = _data
        self.next = None

class LinkedList :
    def __init__(self,_name):
        self.name = _name
        self.Head = None
        self.prev = None
        self.counter = 0
        
    def addNode(self,_data):
        self.counter += 1
        _temp = node(self.counter,_data)
        if (self.Head == None):
            self.Head = _temp
            self.prev = _temp
        else:
            self.prev.next = _temp
            self.prev = _temp
        
        
    def getAllElements(self):
        """ This function implements Traversing operation within linked list"""
        i = self.Head
        _data = []
        while (i != None):
            _data.append((i.index,i.data))
            i = i.next
            
        return _data

    def getElementByIndex(self,_index):
        """ This function implements Indexing an element within linked list"""
        if (_index <= self.counter):
            i = self.Head
            while(i != None):
                if (i.index == _index):
                    return i.data
                i = i.next

    def SearchElement(self,E):
        """ This function implements searching operation within linked list"""
        i = self.Head
        while(i != None):
            if (i.data == E):
                return True
            else:
                i = i.next
        return False

    def deleteNode(self,_index):
        """ This function implements removing a node from a linked list """
        i = self.Head
        while(i != None):
            if (i.index == _index-1):
                _prev = i
            if (i.index == _index):
                _node = i
            if (i.index == _index+1):
                _next = i
                break
            i = i.next
        _prev.next = _node.next
        _next.index -= 1
        del _node

    def Insert(self,_index,_data):
        """This function inserts(prepending) node at given index in linked list"""
        _temp = node(_index,_data)
        i = self.Head
        while (i != None):
            if (i.index == _index - 1):
                _prev = i
            if (i.index == _index):
                _next = i
            if (i.index >= _index):
                i.index += 1
            i = i.next
        _prev.next = _temp
        _temp.next = _next
                
            
"""a = LinkedList("My Linked List")
a.addNode(100)
a.addNode(200)
a.addNode(300)
print(a.getAllElements())
print(a.getElementByIndex(2))
print(a.SearchElement(200))
a.Insert(2,500)
print(a.getAllElements())"""

