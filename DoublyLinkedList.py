#Implementing Doubly Linked List

class Node:
    def __init__(self,_data):
        self.prev = None
        self.data = _data
        self.next = None

    def delete(self):
        del self

class DoublyLinkedLists:
    def __init__(self,_name):
        self.name = _name
        self.head = None
        self.prev = None
        
    def addNode(self,_data):
        '''This function is used to add elements to the end of list'''
        _temp = Node(_data)
        if (self.head == None):
            (self.head , self.prev) = (_temp,_temp)
            (_temp.prev ,_temp.next) = (None,None)
        else:
            (_temp.prev ,_temp.next) = (self.prev,None)
            (self.prev.next, self.prev) = (_temp,_temp)
        del _temp

    def getAllElements(self):
        '''This function will return all the elements in Linked List'''
        i = self.head
        _data = []
        while(i != None):
            _data.append(i.data)
            i = i.next
        del i
        return _data    

    def insertAt(self,_index,_data):
        '''This function is used to insert in linked list, indexing Starts from 0'''
        _temp = Node(_data)
        i = self.head
        _counter = 0
        while(_counter <= _index and i!= None):
            if (_counter == _index):
                _prev = i.prev
                _node = i
                _prev.next = _temp
                _temp.prev = _prev
                _node.prev = _temp 
                _temp.next = _node
                del _prev,_node,_temp
                break
            i = i.next
            _counter += 1    

    def deleteAt(self,_index):
        '''This function is used to delete from linked list, indexing Starts from 0'''
        _counter = 0
        i = self.head
        while(_counter <= _index and i != None):
            if (_counter == _index):
                _prev = i.prev
                _next = i.next
                _prev.next ,_next.prev = _next , _prev
                i.delete()
                del i
                break
            _counter += 1
            i = i.next

    
        
        
ll = DoublyLinkedLists("My Doubly Linked List")
ll.addNode(100)
ll.addNode(200)
ll.addNode(300)
ll.addNode(400)
print(ll.getAllElements())
ll.insertAt(3,600)
print(ll.getAllElements())
ll.addNode(500)
print(ll.getAllElements())
ll.deleteAt(3)
print(ll.getAllElements())
        
